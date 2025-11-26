from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from Parsers.ParserANTLR.CoutGrammarLexer import CoutGrammarLexer
from Parsers.ParserANTLR.CoutGrammarParser import CoutGrammarParser
from Parsers.ParserANTLR.CoutGrammarVisitor import CoutGrammarVisitor


class CoutMultiErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append({
            'line': line,
            'column': column,
            'msg': msg,
            'offendingSymbol': offendingSymbol
        })

    def get_errors(self):
        return self.errors

    def has_errors(self):
        return len(self.errors) > 0


class AdvancedCoutInterpreter(CoutGrammarVisitor):
    def __init__(self):
        self.variables = {}
        self.output = []

    def visitS(self, ctx):
        return self.visit(ctx.output())

    def visitOutput(self, ctx):
        items = []
        for item_ctx in ctx.item():
            value = self.visit(item_ctx)
            items.append(str(value))

        output_line = ' '.join(items)
        self.output.append(output_line)
        return output_line

    def visitItem(self, ctx):
        if ctx.ID():
            var_name = ctx.ID().getText()
            return self.variables.get(var_name, f"<{var_name}>")
        elif ctx.STR():
            text = ctx.STR().getText()
            return text[1:-1]
        elif ctx.NUM():
            return ctx.NUM().getText()

    def get_output(self):
        return '\n'.join(self.output)


def parse_with_all_errors(code):
    """
    Парсит код и собирает ВСЕ ошибки
    """
    input_stream = InputStream(code)
    lexer = CoutGrammarLexer(input_stream)

    # Убираем стандартный обработчик ошибок и добавляем наш
    error_listener = CoutMultiErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    stream = CommonTokenStream(lexer)

    parser = CoutGrammarParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    try:
        tree = parser.s()

        # Если есть ошибки, выбрасываем исключение со всеми ошибками
        if error_listener.has_errors():
            errors_text = "\n".join([
                f"Ошибка {i + 1} на позиции {err['line']}:{err['column']} - {err['msg']}"
                for i, err in enumerate(error_listener.get_errors())
            ])
            raise Exception(f"Найдены ошибки:\n{errors_text}")

        # Если ошибок нет, выполняем интерпретацию
        interpreter = AdvancedCoutInterpreter()
        result = interpreter.visit(tree)
        return True, result, interpreter.get_output()

    except Exception as e:
        return False, str(e), None


def analyze_tokens(code):
    """
    Анализирует токены для отладки
    """
    input_stream = InputStream(code)
    lexer = CoutGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill()

    print("Токены:")
    print("-" * 50)
    for token in stream.tokens:
        if token.type != -1:  # Пропускаем EOF токен
            token_name = lexer.symbolicNames[token.type]
            print(f"  {token_name:10} -> '{token.text}'")
    print("-" * 50)


# Тестирование
if __name__ == '__main__':
    test_cases = [
        # Корректные примеры
        'cout << "Hello" << "World";',
        'cout << 42 << 3.14;',

        # Пример с множественными ошибками
        'cout << "Hello" <<< \n 1as << b << "s" << cout <<<;',

        # Другие примеры с ошибками
        'cout << "NoSemicolon"',
        'cout "Hello" << "World";',
        '<< "Only operator";',
    ]

    print("ПАРСЕР C++ cout С ОБРАБОТКОЙ ВСЕХ ОШИБОК")
    print("=" * 60)

    for i, test_case in enumerate(test_cases, 1):
        print(f"\nТЕСТ {i}: {test_case}")
        print("-" * 40)

        # Анализ токенов
        analyze_tokens(test_case)

        # Парсинг с сбором всех ошибок
        success, result, output = parse_with_all_errors(test_case)

        if success:
            print(f"✓ УСПЕХ: {output}")
        else:
            print(f"✗ ОШИБКИ: {result}")