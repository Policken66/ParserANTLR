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
            "line": line,
            "column": column,
            "msg": msg,
            "offendingSymbol": offendingSymbol
        })

    def has_errors(self):
        return len(self.errors) > 0

    def get_errors(self):
        return self.errors


class AdvancedPLInterpreter(PLVisitor):
    """
    Сборщик структуры (для тестирования парсинга) под текущую грамматику PL.g4.
    Ничего "не вычисляет" — в основном восстанавливает строки.
    """
    def __init__(self):
        self.variables = {}   # var/init (lvalue_str -> value_str or None)
        self.consts = {}      # const (ID -> value_str)
        self.inputs = []      # input identifiers
        self.outputs = []     # output lvalues as strings
        self.equations = []   # list of (lhs_str, rhs_str) ; rhs_str может быть None для call_stmt

    # model : (statement)* EOF;
    def visitModel(self, ctx: PLParser.ModelContext):
        return self.visitChildren(ctx)

    # statement : declaration | equation | call_stmt | control_statement | routine_definition | directive | script_block | block;
    def visitStatement(self, ctx: PLParser.StatementContext):
        # ровно одна альтернатива -> можно просто visitChildren
        return self.visitChildren(ctx)

    # -------- Declarations --------

    # declaration : var_decl | const_decl | input_decl | output_decl | init_decl;
    def visitDeclaration(self, ctx: PLParser.DeclarationContext):
        return self.visitChildren(ctx)

    # var_decl : VAR var_item (COMMA var_item)* SEMI;
    # var_item : lvalue (COLON type_name)? (ASSIGN expression)?;
    def visitVar_decl(self, ctx: PLParser.Var_declContext):
        for item in ctx.var_item():
            name = self.visit(item.lvalue())
            value = self.visit(item.expression()) if item.expression() else None
            self.variables[name] = value
        return None

    # const_decl : CONST const_item (COMMA const_item)* SEMI;
    # const_item : ID ASSIGN expression;
    def visitConst_decl(self, ctx: PLParser.Const_declContext):
        for item in ctx.const_item():
            name = item.ID().getText()
            value = self.visit(item.expression())
            self.consts[name] = value
        return None

    # input_decl : INPUT ident_list SEMI;
    def visitInput_decl(self, ctx: PLParser.Input_declContext):
        for ident_ctx in ctx.ident_list().ident():
            self.inputs.append(ident_ctx.ID().getText())
        return None

    # output_decl : OUTPUT output_item (COMMA output_item)* SEMI;
    # output_item : lvalue;
    def visitOutput_decl(self, ctx: PLParser.Output_declContext):
        for item in ctx.output_item():
            self.outputs.append(self.visit(item.lvalue()))
        return None

    # init_decl : INIT init_item (COMMA init_item)* SEMI;
    # init_item : lvalue (ASSIGN expression)?;
    def visitInit_decl(self, ctx: PLParser.Init_declContext):
        for item in ctx.init_item():
            name = self.visit(item.lvalue())
            value = self.visit(item.expression()) if item.expression() else None
            self.variables[name] = value
        return None

    # lvalue : ID (LBRACK expression RBRACK)*;
    def visitLvalue(self, ctx: PLParser.LvalueContext):
        base = ctx.ID().getText()
        res = base
        # индексы
        for idx_expr in ctx.expression():
            res += f"[{self.visit(idx_expr)}]"
        return res

    # -------- Equations / Calls --------

    # equation : lhs ASSIGN expression SEMI;
    def visitEquation(self, ctx: PLParser.EquationContext):
        lhs_str = self.visit(ctx.lhs())
        rhs_str = self.visit(ctx.expression())
        self.equations.append((lhs_str, rhs_str))
        return None

    # lhs : lvalue derivative_mark? (LBRACK expression RBRACK)*;
    # (у тебя lvalue уже содержит [..], но оставляем поддержку "хвоста" как в грамматике)
    def visitLhs(self, ctx: PLParser.LhsContext):
        parts = []

        # 1) базовый lvalue
        if ctx.lvalue():
            parts.append(self.visit(ctx.lvalue()))
        else:
            # на всякий случай
            parts.append(ctx.getChild(0).getText())

        # 2) производная (апострофы)
        if ctx.derivative_mark():
            parts[-1] = parts[-1] + ctx.derivative_mark().getText()

        # 3) дополнительная индексация (если реально используется)
        # В LhsContext expression() вернёт и выражения внутри lvalue, и хвостовые.
        # Чтобы не "удваивать" индексы, добавляем хвост только если в дереве есть LBRACK после derivative_mark.
        text = ctx.getText()
        # грубо: если встречается "]['" не характерно; но проще: доверим синтаксису — хвост добавим,
        # только когда количество LBRACK в ctx больше, чем в lvalue().
        lval_text = ctx.lvalue().getText() if ctx.lvalue() else ""
        if text.count('[') > lval_text.count('['):
            # хвостовые выражения в дереве идут отдельными expression() после lvalue/derivative_mark,
            # но ANTLR не разделяет их удобно; поэтому просто восстановим как в исходном тексте:
            # берём кусок после lvalue(+derivative) и добавляем.
            base = parts[-1]
            # удалим из full-text префикс lvalue (+ derivative_mark если есть)
            prefix = ctx.lvalue().getText()
            if ctx.derivative_mark():
                prefix += ctx.derivative_mark().getText()
            suffix = text[len(prefix):]
            parts[-1] = base + suffix

        return "".join(parts)

    # call_stmt : func_call SEMI;
    def visitCall_stmt(self, ctx: PLParser.Call_stmtContext):
        call_str = self.visit(ctx.func_call())
        self.equations.append((call_str, None))
        return None

    # -------- Expressions (stringify) --------

    # expression : or_expr;
    def visitExpression(self, ctx: PLParser.ExpressionContext):
        return self.visit(ctx.or_expr())

    # or_expr : and_expr (OR_OP and_expr)*;
    def visitOr_expr(self, ctx: PLParser.Or_exprContext):
        s = self.visit(ctx.and_expr(0))
        for i in range(1, len(ctx.and_expr())):
            op = ctx.OR_OP(i - 1).getText()
            s = f"{s} {op} {self.visit(ctx.and_expr(i))}"
        return s

    # and_expr : eq_expr (AND_OP eq_expr)*;
    def visitAnd_expr(self, ctx: PLParser.And_exprContext):
        s = self.visit(ctx.eq_expr(0))
        for i in range(1, len(ctx.eq_expr())):
            op = ctx.AND_OP(i - 1).getText()
            s = f"{s} {op} {self.visit(ctx.eq_expr(i))}"
        return s

    # eq_expr : rel_expr ((ASSIGN | EQUAL | NOTEQUAL) rel_expr)?;
    def visitEq_expr(self, ctx: PLParser.Eq_exprContext):
        left = self.visit(ctx.rel_expr(0))
        if len(ctx.rel_expr()) == 1:
            return left
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.rel_expr(1))
        return f"{left} {op} {right}"

    # rel_expr : add_expr ((LT | GT | LE | GE) add_expr)*;
    def visitRel_expr(self, ctx: PLParser.Rel_exprContext):
        s = self.visit(ctx.add_expr(0))
        i = 1
        while i + 1 < ctx.getChildCount():
            op = ctx.getChild(i).getText()
            rhs = self.visit(ctx.getChild(i + 1))
            s = f"{s} {op} {rhs}"
            i += 2
        return s

    # add_expr : mul_expr ((ADD | SUB) mul_expr)*;
    def visitAdd_expr(self, ctx: PLParser.Add_exprContext):
        s = self.visit(ctx.mul_expr(0))
        i = 1
        while i + 1 < ctx.getChildCount():
            op = ctx.getChild(i).getText()
            rhs = self.visit(ctx.getChild(i + 1))
            s = f"{s} {op} {rhs}"
            i += 2
        return s

    # mul_expr : pow_expr ((MUL | DIV) pow_expr)*;
    def visitMul_expr(self, ctx: PLParser.Mul_exprContext):
        s = self.visit(ctx.pow_expr(0))
        for i in range(1, len(ctx.pow_expr())):
            op = ctx.getChild(2 * i - 1).getText()  # между pow_expr стоят операторы
            rhs = self.visit(ctx.pow_expr(i))
            s = f"{s} {op} {rhs}"
        return s

    # pow_expr : unary_expr (POW pow_expr)?;
    def visitPow_expr(self, ctx: PLParser.Pow_exprContext):
        left = self.visit(ctx.unary_expr())
        if ctx.pow_expr():
            return f"{left}^{self.visit(ctx.pow_expr())}"
        return left

    # unary_expr : (ADD | SUB | NOT_OP | BANG) unary_expr | primary;
    def visitUnary_expr(self, ctx: PLParser.Unary_exprContext):
        if ctx.primary():
            return self.visit(ctx.primary())
        op = ctx.getChild(0).getText()
        rhs = self.visit(ctx.unary_expr())
        # без пробела, чтобы "-1" не превращалось в "- 1"
        return f"{op}{rhs}"

    # primary : literal | lvalue | func_call | array_literal | '(' expression ')';
    def visitPrimary(self, ctx: PLParser.PrimaryContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.lvalue():
            return self.visit(ctx.lvalue())
        if ctx.func_call():
            return self.visit(ctx.func_call())
        if ctx.array_literal():
            return self.visit(ctx.array_literal())
        if ctx.expression():
            return f"({self.visit(ctx.expression())})"
        return ctx.getText()

    # func_call : ident '(' arg_list? ')';
    def visitFunc_call(self, ctx: PLParser.Func_callContext):
        name = ctx.ident().ID().getText()
        if ctx.arg_list():
            args = self.visit(ctx.arg_list())
            return f"{name}({', '.join(args)})"
        return f"{name}()"

    # arg_list : expression (',' expression)*;
    def visitArg_list(self, ctx: PLParser.Arg_listContext):
        return [self.visit(e) for e in ctx.expression()]

    # literal : NUMBER | STRING;
    def visitLiteral(self, ctx: PLParser.LiteralContext):
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        if ctx.STRING():
            return ctx.STRING().getText()
        return ctx.getText()

    # array_literal : '[' expression (',' expression)* ']';
    def visitArray_literal(self, ctx: PLParser.Array_literalContext):
        elems = [self.visit(ctx.expression(0))]
        for i in range(1, len(ctx.expression())):
            elems.append(self.visit(ctx.expression(i)))
        return f"[{', '.join(elems)}]"


def parse_with_all_errors(code: str):
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
        tree = parser.model()

        if error_listener.has_errors():
            errors_text = "\n".join(
                f"Ошибка {i + 1} на позиции {e['line']}:{e['column']} — {e['msg']}"
                for i, e in enumerate(error_listener.get_errors())
            )
            raise Exception(errors_text)

        interpreter = AdvancedPLInterpreter()
        interpreter.visit(tree)

        return True, "Парсинг успешно завершён", {
            "variables": interpreter.variables,
            "consts": interpreter.consts,
            "inputs": interpreter.inputs,
            "outputs": interpreter.outputs,
            "equations": interpreter.equations,
        }

    except Exception as e:
        return False, str(e), None
