from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from Parsers.ParserPL.PLLexer import PLLexer
from Parsers.ParserPL.PLParser import PLParser
from Parsers.ParserPL.PLVisitor import PLVisitor


class PLMultiErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append({
            'line': line,
            'column': column,
            'msg': msg,
            'offendingSymbol': offendingSymbol
        })

    def has_errors(self):
        return len(self.errors) > 0

    def get_errors(self):
        return self.errors


class AdvancedPLInterpreter(PLVisitor):
    """
    Интерпретатор подмножества PL (новая грамматика).
    """
    def __init__(self):
        self.variables = {}

    # program : (statement ';')* EOF ;
    def visitProgram(self, ctx: PLParser.ProgramContext):
        return self.visitChildren(ctx)

    # statement : var_decl | expr ;
    def visitStatement(self, ctx: PLParser.StatementContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        return self.visit(ctx.expr())

    # var_decl : 'var' ID ( '=' expr | (',' ID)* ) ;
    def visitVar_decl(self, ctx: PLParser.Var_declContext):
        first_id = ctx.ID(0).getText()

        # вариант: var x = expr
        if ctx.expr():
            value = self.visit(ctx.expr())
            self.variables[first_id] = value

        # вариант: var x, y, z
        else:
            for id_token in ctx.ID():
                self.variables[id_token.getText()] = None

        return None

    # expr :
    #   ID ('(' arg_list ')')?
    # | NUMBER
    # | STRING
    def visitExpr(self, ctx: PLParser.ExprContext):
        if ctx.ID():
            name = ctx.ID().getText()

            # вызов функции
            if ctx.arg_list():
                args = self.visit(ctx.arg_list())
                return f"{name}({', '.join(map(str, args))})"

            # просто идентификатор
            return self.variables.get(name, f"<{name}>")

        if ctx.NUMBER():
            return float(ctx.NUMBER().getText()) if '.' in ctx.NUMBER().getText() else int(ctx.NUMBER().getText())

        if ctx.STRING():
            return ctx.STRING().getText()[1:-1]

        return None

    # arg_list : expr (',' expr)* ;
    def visitArg_list(self, ctx: PLParser.Arg_listContext):
        return [self.visit(expr) for expr in ctx.expr()]


def parse_with_all_errors(code):
    input_stream = InputStream(code)
    lexer = PLLexer(input_stream)

    error_listener = PLMultiErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    token_stream = CommonTokenStream(lexer)

    parser = PLParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    try:
        tree = parser.program()

        if error_listener.has_errors():
            errors_text = "\n".join(
                f"Ошибка {i + 1} на позиции {e['line']}:{e['column']} — {e['msg']}"
                for i, e in enumerate(error_listener.get_errors())
            )
            raise Exception(errors_text)

        interpreter = AdvancedPLInterpreter()
        interpreter.visit(tree)

        return True, "Парсинг успешно завершён", interpreter.variables

    except Exception as e:
        return False, str(e), None
