import sys
from antlr4 import *
from CoutGrammarLexer import CoutGrammarLexer
from CoutGrammarParser import CoutGrammarParser
from CoutGrammarVisitor import CoutGrammarVisitor


class CoutInterpreter(CoutGrammarVisitor):
    def __init__(self):
        self.variables = {}
        self.output = []

    def visitS(self, ctx):
        return self.visit(ctx.output())

    def visitOutput(self, ctx):
        results = []
        for item_ctx in ctx.item():
            result = self.visit(item_ctx)
            results.append(str(result))

        output_line = ' '.join(results)
        self.output.append(output_line)
        return output_line

    def visitItem(self, ctx):
        if ctx.ID():
            var_name = ctx.ID().getText()
            return self.variables.get(var_name, f"<undefined variable '{var_name}'>")
        elif ctx.STR():
            # Убираем кавычки
            text = ctx.STR().getText()
            return text[1:-1]  # удаляем первые и последние кавычки
        elif ctx.NUM():
            return ctx.NUM().getText()

    def get_output(self):
        return '\n'.join(self.output)


def parse_cout_code(code, interpreter=None):
    input_stream = InputStream(code)
    lexer = CoutGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CoutGrammarParser(stream)

    tree = parser.s()

    if interpreter is None:
        interpreter = CoutInterpreter()

    interpreter.visit(tree)
    return interpreter


def main():
    # Примеры корректных выражений
    test_cases = [
        'cout << "Hello" << "World";',
        'cout << 42 << 3.14;',
        'cout << variable_name << "text";',
        'cout << 100;',
        'cout << sa"Single";',
    ]

    interpreter = CoutInterpreter()

    print("Тестирование парсера cout:")
    print("=" * 50)

    for i, test_case in enumerate(test_cases, 1):
        print(f"\nТест {i}: {test_case}")
        try:
            result = parse_cout_code(test_case, interpreter)
            print(f"Результат: {interpreter.get_output().splitlines()[-1]}")
        except Exception as e:
            print(f"Ошибка: {e}")

    # Интерактивный режим
    print("\n" + "=" * 50)
    print("Интерактивный режим (для выхода введите 'exit'):")

    while True:
        try:
            user_input = input(">>> ").strip()
            if user_input.lower() == 'exit':
                break
            if not user_input:
                continue

            parse_cout_code(user_input, interpreter)
            print(interpreter.get_output().splitlines()[-1])

        except Exception as e:
            print(f"Ошибка синтаксиса: {e}")


if __name__ == '__main__':
    main()