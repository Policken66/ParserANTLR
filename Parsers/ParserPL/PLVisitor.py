# Generated from PL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PLParser import PLParser
else:
    from PLParser import PLParser

# This class defines a complete generic visitor for a parse tree produced by PLParser.

class PLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLParser#model.
    def visitModel(self, ctx:PLParser.ModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#statement.
    def visitStatement(self, ctx:PLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#declaration.
    def visitDeclaration(self, ctx:PLParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#var_decl.
    def visitVar_decl(self, ctx:PLParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#var_item.
    def visitVar_item(self, ctx:PLParser.Var_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#type_name.
    def visitType_name(self, ctx:PLParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#const_decl.
    def visitConst_decl(self, ctx:PLParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#const_item.
    def visitConst_item(self, ctx:PLParser.Const_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#input_decl.
    def visitInput_decl(self, ctx:PLParser.Input_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#output_decl.
    def visitOutput_decl(self, ctx:PLParser.Output_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#output_item.
    def visitOutput_item(self, ctx:PLParser.Output_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#lvalue.
    def visitLvalue(self, ctx:PLParser.LvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#init_decl.
    def visitInit_decl(self, ctx:PLParser.Init_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#init_item.
    def visitInit_item(self, ctx:PLParser.Init_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#ident_list.
    def visitIdent_list(self, ctx:PLParser.Ident_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#ident.
    def visitIdent(self, ctx:PLParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#equation.
    def visitEquation(self, ctx:PLParser.EquationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#lhs.
    def visitLhs(self, ctx:PLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#derivative_mark.
    def visitDerivative_mark(self, ctx:PLParser.Derivative_markContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#expression.
    def visitExpression(self, ctx:PLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#or_expr.
    def visitOr_expr(self, ctx:PLParser.Or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#and_expr.
    def visitAnd_expr(self, ctx:PLParser.And_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#eq_expr.
    def visitEq_expr(self, ctx:PLParser.Eq_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#rel_expr.
    def visitRel_expr(self, ctx:PLParser.Rel_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#add_expr.
    def visitAdd_expr(self, ctx:PLParser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#mul_expr.
    def visitMul_expr(self, ctx:PLParser.Mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#pow_expr.
    def visitPow_expr(self, ctx:PLParser.Pow_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#unary_expr.
    def visitUnary_expr(self, ctx:PLParser.Unary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#primary.
    def visitPrimary(self, ctx:PLParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#func_call.
    def visitFunc_call(self, ctx:PLParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#arg_list.
    def visitArg_list(self, ctx:PLParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#literal.
    def visitLiteral(self, ctx:PLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#array_literal.
    def visitArray_literal(self, ctx:PLParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#control_statement.
    def visitControl_statement(self, ctx:PLParser.Control_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#if_stmt.
    def visitIf_stmt(self, ctx:PLParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#stmt_or_block.
    def visitStmt_or_block(self, ctx:PLParser.Stmt_or_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#block.
    def visitBlock(self, ctx:PLParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#while_stmt.
    def visitWhile_stmt(self, ctx:PLParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#for_stmt.
    def visitFor_stmt(self, ctx:PLParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#for_init.
    def visitFor_init(self, ctx:PLParser.For_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#repeat_stmt.
    def visitRepeat_stmt(self, ctx:PLParser.Repeat_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#switch_stmt.
    def visitSwitch_stmt(self, ctx:PLParser.Switch_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#switch_case.
    def visitSwitch_case(self, ctx:PLParser.Switch_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#expr_list.
    def visitExpr_list(self, ctx:PLParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#exit_stmt.
    def visitExit_stmt(self, ctx:PLParser.Exit_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#goto_stmt.
    def visitGoto_stmt(self, ctx:PLParser.Goto_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#label_stmt.
    def visitLabel_stmt(self, ctx:PLParser.Label_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#call_stmt.
    def visitCall_stmt(self, ctx:PLParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#inline_stmt.
    def visitInline_stmt(self, ctx:PLParser.Inline_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#routine_definition.
    def visitRoutine_definition(self, ctx:PLParser.Routine_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#function_def.
    def visitFunction_def(self, ctx:PLParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#procedure_def.
    def visitProcedure_def(self, ctx:PLParser.Procedure_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#formal_params.
    def visitFormal_params(self, ctx:PLParser.Formal_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#param.
    def visitParam(self, ctx:PLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#routine_body.
    def visitRoutine_body(self, ctx:PLParser.Routine_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#directive.
    def visitDirective(self, ctx:PLParser.DirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#define_dir.
    def visitDefine_dir(self, ctx:PLParser.Define_dirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#include_dir.
    def visitInclude_dir(self, ctx:PLParser.Include_dirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#ifdef_dir.
    def visitIfdef_dir(self, ctx:PLParser.Ifdef_dirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#ifndef_dir.
    def visitIfndef_dir(self, ctx:PLParser.Ifndef_dirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#undefine_dir.
    def visitUndefine_dir(self, ctx:PLParser.Undefine_dirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#script_block.
    def visitScript_block(self, ctx:PLParser.Script_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLParser#script_body.
    def visitScript_body(self, ctx:PLParser.Script_bodyContext):
        return self.visitChildren(ctx)



del PLParser