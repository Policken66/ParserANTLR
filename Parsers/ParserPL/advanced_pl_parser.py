from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from Parsers.ParserPL.PLLexer import PLLexer
from Parsers.ParserPL.PLParser import PLParser
from Parsers.ParserPL.PLVisitor import PLVisitor


class PLMultiErrorListener(ErrorListener):
    """
    Собирает все синтаксические ошибки.
    """
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


class AdvancedPLInterpreter(PLVisitor):
    """
    Интерпретатор подмножества PL.
    Хранит переменные и позволяет получать их значения.
    """
    def __init__(self):
        self.variables = {}
        self.output = []  # можно использовать, если хотим выводить что-то

    # program -> statement_list EOF
    def visitProgram(self, ctx:PLParser.ProgramContext):
        return self.visitChildren(ctx)

    # statement_list -> statement ';' statement_list | ε
    def visitStatement_list(self, ctx:PLParser.Statement_listContext):
        return self.visitChildren(ctx)

    # statement -> var_decl | expr
    def visitStatement(self, ctx:PLParser.StatementContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        elif ctx.expr():
            return self.visit(ctx.expr())
        return None

    # var_decl -> 'var' ID var_decl_tail
    def visitVar_decl(self, ctx:PLParser.Var_declContext):
        var_name = ctx.ID().getText()
        tail_ctx = ctx.var_decl_tail()
        if tail_ctx.expr():
            value = self.visit(tail_ctx.expr())
            self.variables[var_name] = value
        else:
            # если просто список идентификаторов
            self.variables[var_name] = None
        return var_name

    # var_decl_tail -> '=' expr | id_list_tail
    def visitVar_decl_tail(self, ctx:PLParser.Var_decl_tailContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.id_list_tail():
            return self.visit(ctx.id_list_tail())
        return None

    # id_list_tail -> ',' ID id_list_tail | ε
    def visitId_list_tail(self, ctx:PLParser.Id_list_tailContext):
        ids = []
        if ctx.ID():
            ids.append(ctx.ID().getText())
        if ctx.id_list_tail():
            ids.extend(self.visit(ctx.id_list_tail()))
        return ids

    # expr -> call | ID | NUMBER | STRING
    def visitExpr(self, ctx:PLParser.ExprContext):
        if ctx.call():
            return self.visit(ctx.call())
        elif ctx.ID():
            name = ctx.ID().getText()
            return self.variables.get(name, f"<{name}>")
        elif ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        return None

    # call -> ID '(' arg_list ')'
    def visitCall(self, ctx:PLParser.CallContext):
        func_name = ctx.ID().getText()
        args = []
        if ctx.arg_list() and ctx.arg_list().expr():
            args.append(self.visit(ctx.arg_list().expr()))
        # можно здесь расширять вызовы функций
        return f"{func_name}({', '.join(map(str, args))})"

    # arg_list -> expr arg_list_tail | ε
    def visitArg_list(self, ctx:PLParser.Arg_listContext):
        args = []
        if ctx.expr():
            args.append(self.visit(ctx.expr()))
        if ctx.arg_list_tail():
            args.extend(self.visit(ctx.arg_list_tail()))
        return args

    # arg_list_tail -> ',' expr arg_list_tail | ε
    def visitArg_list_tail(self, ctx:PLParser.Arg_list_tailContext):
        args = []
        if ctx.expr():
            args.append(self.visit(ctx.expr()))
        if ctx.arg_list_tail():
            args.extend(self.visit(ctx.arg_list_tail()))
        return args


def parse_with_all_errors(code):
    """
    Парсит код на подмножестве PL и возвращает:
        success (bool), message / result, variables (dict)
    """
    input_stream = InputStream(code)
    lexer = PLLexer(input_stream)

    # Обработчик ошибок
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
            errors_text = "\n".join([
                f"Ошибка {i + 1} на позиции {err['line']}:{err['column']} - {err['msg']}"
                for i, err in enumerate(error_listener.get_errors())
            ])
            raise Exception(f"Найдены ошибки:\n{errors_text}")

        interpreter = AdvancedPLInterpreter()
        interpreter.visit(tree)
        return True, "Парсинг успешно завершен", interpreter.variables

    except Exception as e:
        return False, str(e), None
