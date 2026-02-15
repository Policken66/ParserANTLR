# Generated from PL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PLParser import PLParser
else:
    from PLParser import PLParser

# This class defines a complete listener for a parse tree produced by PLParser.
class PLListener(ParseTreeListener):

    # Enter a parse tree produced by PLParser#model.
    def enterModel(self, ctx:PLParser.ModelContext):
        pass

    # Exit a parse tree produced by PLParser#model.
    def exitModel(self, ctx:PLParser.ModelContext):
        pass


    # Enter a parse tree produced by PLParser#statement.
    def enterStatement(self, ctx:PLParser.StatementContext):
        pass

    # Exit a parse tree produced by PLParser#statement.
    def exitStatement(self, ctx:PLParser.StatementContext):
        pass


    # Enter a parse tree produced by PLParser#declaration.
    def enterDeclaration(self, ctx:PLParser.DeclarationContext):
        pass

    # Exit a parse tree produced by PLParser#declaration.
    def exitDeclaration(self, ctx:PLParser.DeclarationContext):
        pass


    # Enter a parse tree produced by PLParser#var_decl.
    def enterVar_decl(self, ctx:PLParser.Var_declContext):
        pass

    # Exit a parse tree produced by PLParser#var_decl.
    def exitVar_decl(self, ctx:PLParser.Var_declContext):
        pass


    # Enter a parse tree produced by PLParser#var_item.
    def enterVar_item(self, ctx:PLParser.Var_itemContext):
        pass

    # Exit a parse tree produced by PLParser#var_item.
    def exitVar_item(self, ctx:PLParser.Var_itemContext):
        pass


    # Enter a parse tree produced by PLParser#type_name.
    def enterType_name(self, ctx:PLParser.Type_nameContext):
        pass

    # Exit a parse tree produced by PLParser#type_name.
    def exitType_name(self, ctx:PLParser.Type_nameContext):
        pass


    # Enter a parse tree produced by PLParser#const_decl.
    def enterConst_decl(self, ctx:PLParser.Const_declContext):
        pass

    # Exit a parse tree produced by PLParser#const_decl.
    def exitConst_decl(self, ctx:PLParser.Const_declContext):
        pass


    # Enter a parse tree produced by PLParser#const_item.
    def enterConst_item(self, ctx:PLParser.Const_itemContext):
        pass

    # Exit a parse tree produced by PLParser#const_item.
    def exitConst_item(self, ctx:PLParser.Const_itemContext):
        pass


    # Enter a parse tree produced by PLParser#input_decl.
    def enterInput_decl(self, ctx:PLParser.Input_declContext):
        pass

    # Exit a parse tree produced by PLParser#input_decl.
    def exitInput_decl(self, ctx:PLParser.Input_declContext):
        pass


    # Enter a parse tree produced by PLParser#output_decl.
    def enterOutput_decl(self, ctx:PLParser.Output_declContext):
        pass

    # Exit a parse tree produced by PLParser#output_decl.
    def exitOutput_decl(self, ctx:PLParser.Output_declContext):
        pass


    # Enter a parse tree produced by PLParser#output_item.
    def enterOutput_item(self, ctx:PLParser.Output_itemContext):
        pass

    # Exit a parse tree produced by PLParser#output_item.
    def exitOutput_item(self, ctx:PLParser.Output_itemContext):
        pass


    # Enter a parse tree produced by PLParser#lvalue.
    def enterLvalue(self, ctx:PLParser.LvalueContext):
        pass

    # Exit a parse tree produced by PLParser#lvalue.
    def exitLvalue(self, ctx:PLParser.LvalueContext):
        pass


    # Enter a parse tree produced by PLParser#init_decl.
    def enterInit_decl(self, ctx:PLParser.Init_declContext):
        pass

    # Exit a parse tree produced by PLParser#init_decl.
    def exitInit_decl(self, ctx:PLParser.Init_declContext):
        pass


    # Enter a parse tree produced by PLParser#init_item.
    def enterInit_item(self, ctx:PLParser.Init_itemContext):
        pass

    # Exit a parse tree produced by PLParser#init_item.
    def exitInit_item(self, ctx:PLParser.Init_itemContext):
        pass


    # Enter a parse tree produced by PLParser#ident_list.
    def enterIdent_list(self, ctx:PLParser.Ident_listContext):
        pass

    # Exit a parse tree produced by PLParser#ident_list.
    def exitIdent_list(self, ctx:PLParser.Ident_listContext):
        pass


    # Enter a parse tree produced by PLParser#ident.
    def enterIdent(self, ctx:PLParser.IdentContext):
        pass

    # Exit a parse tree produced by PLParser#ident.
    def exitIdent(self, ctx:PLParser.IdentContext):
        pass


    # Enter a parse tree produced by PLParser#equation.
    def enterEquation(self, ctx:PLParser.EquationContext):
        pass

    # Exit a parse tree produced by PLParser#equation.
    def exitEquation(self, ctx:PLParser.EquationContext):
        pass


    # Enter a parse tree produced by PLParser#lhs.
    def enterLhs(self, ctx:PLParser.LhsContext):
        pass

    # Exit a parse tree produced by PLParser#lhs.
    def exitLhs(self, ctx:PLParser.LhsContext):
        pass


    # Enter a parse tree produced by PLParser#derivative_mark.
    def enterDerivative_mark(self, ctx:PLParser.Derivative_markContext):
        pass

    # Exit a parse tree produced by PLParser#derivative_mark.
    def exitDerivative_mark(self, ctx:PLParser.Derivative_markContext):
        pass


    # Enter a parse tree produced by PLParser#expression.
    def enterExpression(self, ctx:PLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PLParser#expression.
    def exitExpression(self, ctx:PLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PLParser#or_expr.
    def enterOr_expr(self, ctx:PLParser.Or_exprContext):
        pass

    # Exit a parse tree produced by PLParser#or_expr.
    def exitOr_expr(self, ctx:PLParser.Or_exprContext):
        pass


    # Enter a parse tree produced by PLParser#and_expr.
    def enterAnd_expr(self, ctx:PLParser.And_exprContext):
        pass

    # Exit a parse tree produced by PLParser#and_expr.
    def exitAnd_expr(self, ctx:PLParser.And_exprContext):
        pass


    # Enter a parse tree produced by PLParser#eq_expr.
    def enterEq_expr(self, ctx:PLParser.Eq_exprContext):
        pass

    # Exit a parse tree produced by PLParser#eq_expr.
    def exitEq_expr(self, ctx:PLParser.Eq_exprContext):
        pass


    # Enter a parse tree produced by PLParser#rel_expr.
    def enterRel_expr(self, ctx:PLParser.Rel_exprContext):
        pass

    # Exit a parse tree produced by PLParser#rel_expr.
    def exitRel_expr(self, ctx:PLParser.Rel_exprContext):
        pass


    # Enter a parse tree produced by PLParser#add_expr.
    def enterAdd_expr(self, ctx:PLParser.Add_exprContext):
        pass

    # Exit a parse tree produced by PLParser#add_expr.
    def exitAdd_expr(self, ctx:PLParser.Add_exprContext):
        pass


    # Enter a parse tree produced by PLParser#mul_expr.
    def enterMul_expr(self, ctx:PLParser.Mul_exprContext):
        pass

    # Exit a parse tree produced by PLParser#mul_expr.
    def exitMul_expr(self, ctx:PLParser.Mul_exprContext):
        pass


    # Enter a parse tree produced by PLParser#pow_expr.
    def enterPow_expr(self, ctx:PLParser.Pow_exprContext):
        pass

    # Exit a parse tree produced by PLParser#pow_expr.
    def exitPow_expr(self, ctx:PLParser.Pow_exprContext):
        pass


    # Enter a parse tree produced by PLParser#unary_expr.
    def enterUnary_expr(self, ctx:PLParser.Unary_exprContext):
        pass

    # Exit a parse tree produced by PLParser#unary_expr.
    def exitUnary_expr(self, ctx:PLParser.Unary_exprContext):
        pass


    # Enter a parse tree produced by PLParser#primary.
    def enterPrimary(self, ctx:PLParser.PrimaryContext):
        pass

    # Exit a parse tree produced by PLParser#primary.
    def exitPrimary(self, ctx:PLParser.PrimaryContext):
        pass


    # Enter a parse tree produced by PLParser#func_call.
    def enterFunc_call(self, ctx:PLParser.Func_callContext):
        pass

    # Exit a parse tree produced by PLParser#func_call.
    def exitFunc_call(self, ctx:PLParser.Func_callContext):
        pass


    # Enter a parse tree produced by PLParser#arg_list.
    def enterArg_list(self, ctx:PLParser.Arg_listContext):
        pass

    # Exit a parse tree produced by PLParser#arg_list.
    def exitArg_list(self, ctx:PLParser.Arg_listContext):
        pass


    # Enter a parse tree produced by PLParser#literal.
    def enterLiteral(self, ctx:PLParser.LiteralContext):
        pass

    # Exit a parse tree produced by PLParser#literal.
    def exitLiteral(self, ctx:PLParser.LiteralContext):
        pass


    # Enter a parse tree produced by PLParser#array_literal.
    def enterArray_literal(self, ctx:PLParser.Array_literalContext):
        pass

    # Exit a parse tree produced by PLParser#array_literal.
    def exitArray_literal(self, ctx:PLParser.Array_literalContext):
        pass


    # Enter a parse tree produced by PLParser#control_statement.
    def enterControl_statement(self, ctx:PLParser.Control_statementContext):
        pass

    # Exit a parse tree produced by PLParser#control_statement.
    def exitControl_statement(self, ctx:PLParser.Control_statementContext):
        pass


    # Enter a parse tree produced by PLParser#if_stmt.
    def enterIf_stmt(self, ctx:PLParser.If_stmtContext):
        pass

    # Exit a parse tree produced by PLParser#if_stmt.
    def exitIf_stmt(self, ctx:PLParser.If_stmtContext):
        pass


    # Enter a parse tree produced by PLParser#stmt_or_block.
    def enterStmt_or_block(self, ctx:PLParser.Stmt_or_blockContext):
        pass

    # Exit a parse tree produced by PLParser#stmt_or_block.
    def exitStmt_or_block(self, ctx:PLParser.Stmt_or_blockContext):
        pass


    # Enter a parse tree produced by PLParser#block.
    def enterBlock(self, ctx:PLParser.BlockContext):
        pass

    # Exit a parse tree produced by PLParser#block.
    def exitBlock(self, ctx:PLParser.BlockContext):
        pass


    # Enter a parse tree produced by PLParser#while_stmt.
    def enterWhile_stmt(self, ctx:PLParser.While_stmtContext):
        pass

    # Exit a parse tree produced by PLParser#while_stmt.
    def exitWhile_stmt(self, ctx:PLParser.While_stmtContext):
        pass


    # Enter a parse tree produced by PLParser#for_stmt.
    def enterFor_stmt(self, ctx:PLParser.For_stmtContext):
        pass

    # Exit a parse tree produced by PLParser#for_stmt.
    def exitFor_stmt(self, ctx:PLParser.For_stmtContext):
        pass


    # Enter a parse tree produced by PLParser#for_init.
    def enterFor_init(self, ctx:PLParser.For_initContext):
        pass

    # Exit a parse tree produced by PLParser#for_init.
    def exitFor_init(self, ctx:PLParser.For_initContext):
        pass


    # Enter a parse tree produced by PLParser#repeat_stmt.
    def enterRepeat_stmt(self, ctx:PLParser.Repeat_stmtContext):
        pass

    # Exit a parse tree produced by PLParser#repeat_stmt.
    def exitRepeat_stmt(self, ctx:PLParser.Repeat_stmtContext):
        pass


    # Enter a parse tree produced by PLParser#switch_stmt.
    def enterSwitch_stmt(self, ctx:PLParser.Switch_stmtContext):
        pass

    # Exit a parse tree produced by PLParser#switch_stmt.
    def exitSwitch_stmt(self, ctx:PLParser.Switch_stmtContext):
        pass


    # Enter a parse tree produced by PLParser#switch_case.
    def enterSwitch_case(self, ctx:PLParser.Switch_caseContext):
        pass

    # Exit a parse tree produced by PLParser#switch_case.
    def exitSwitch_case(self, ctx:PLParser.Switch_caseContext):
        pass


    # Enter a parse tree produced by PLParser#expr_list.
    def enterExpr_list(self, ctx:PLParser.Expr_listContext):
        pass

    # Exit a parse tree produced by PLParser#expr_list.
    def exitExpr_list(self, ctx:PLParser.Expr_listContext):
        pass


    # Enter a parse tree produced by PLParser#exit_stmt.
    def enterExit_stmt(self, ctx:PLParser.Exit_stmtContext):
        pass

    # Exit a parse tree produced by PLParser#exit_stmt.
    def exitExit_stmt(self, ctx:PLParser.Exit_stmtContext):
        pass


    # Enter a parse tree produced by PLParser#goto_stmt.
    def enterGoto_stmt(self, ctx:PLParser.Goto_stmtContext):
        pass

    # Exit a parse tree produced by PLParser#goto_stmt.
    def exitGoto_stmt(self, ctx:PLParser.Goto_stmtContext):
        pass


    # Enter a parse tree produced by PLParser#label_stmt.
    def enterLabel_stmt(self, ctx:PLParser.Label_stmtContext):
        pass

    # Exit a parse tree produced by PLParser#label_stmt.
    def exitLabel_stmt(self, ctx:PLParser.Label_stmtContext):
        pass


    # Enter a parse tree produced by PLParser#call_stmt.
    def enterCall_stmt(self, ctx:PLParser.Call_stmtContext):
        pass

    # Exit a parse tree produced by PLParser#call_stmt.
    def exitCall_stmt(self, ctx:PLParser.Call_stmtContext):
        pass


    # Enter a parse tree produced by PLParser#inline_stmt.
    def enterInline_stmt(self, ctx:PLParser.Inline_stmtContext):
        pass

    # Exit a parse tree produced by PLParser#inline_stmt.
    def exitInline_stmt(self, ctx:PLParser.Inline_stmtContext):
        pass


    # Enter a parse tree produced by PLParser#routine_definition.
    def enterRoutine_definition(self, ctx:PLParser.Routine_definitionContext):
        pass

    # Exit a parse tree produced by PLParser#routine_definition.
    def exitRoutine_definition(self, ctx:PLParser.Routine_definitionContext):
        pass


    # Enter a parse tree produced by PLParser#function_def.
    def enterFunction_def(self, ctx:PLParser.Function_defContext):
        pass

    # Exit a parse tree produced by PLParser#function_def.
    def exitFunction_def(self, ctx:PLParser.Function_defContext):
        pass


    # Enter a parse tree produced by PLParser#procedure_def.
    def enterProcedure_def(self, ctx:PLParser.Procedure_defContext):
        pass

    # Exit a parse tree produced by PLParser#procedure_def.
    def exitProcedure_def(self, ctx:PLParser.Procedure_defContext):
        pass


    # Enter a parse tree produced by PLParser#formal_params.
    def enterFormal_params(self, ctx:PLParser.Formal_paramsContext):
        pass

    # Exit a parse tree produced by PLParser#formal_params.
    def exitFormal_params(self, ctx:PLParser.Formal_paramsContext):
        pass


    # Enter a parse tree produced by PLParser#param.
    def enterParam(self, ctx:PLParser.ParamContext):
        pass

    # Exit a parse tree produced by PLParser#param.
    def exitParam(self, ctx:PLParser.ParamContext):
        pass


    # Enter a parse tree produced by PLParser#routine_body.
    def enterRoutine_body(self, ctx:PLParser.Routine_bodyContext):
        pass

    # Exit a parse tree produced by PLParser#routine_body.
    def exitRoutine_body(self, ctx:PLParser.Routine_bodyContext):
        pass


    # Enter a parse tree produced by PLParser#directive.
    def enterDirective(self, ctx:PLParser.DirectiveContext):
        pass

    # Exit a parse tree produced by PLParser#directive.
    def exitDirective(self, ctx:PLParser.DirectiveContext):
        pass


    # Enter a parse tree produced by PLParser#define_dir.
    def enterDefine_dir(self, ctx:PLParser.Define_dirContext):
        pass

    # Exit a parse tree produced by PLParser#define_dir.
    def exitDefine_dir(self, ctx:PLParser.Define_dirContext):
        pass


    # Enter a parse tree produced by PLParser#include_dir.
    def enterInclude_dir(self, ctx:PLParser.Include_dirContext):
        pass

    # Exit a parse tree produced by PLParser#include_dir.
    def exitInclude_dir(self, ctx:PLParser.Include_dirContext):
        pass


    # Enter a parse tree produced by PLParser#ifdef_dir.
    def enterIfdef_dir(self, ctx:PLParser.Ifdef_dirContext):
        pass

    # Exit a parse tree produced by PLParser#ifdef_dir.
    def exitIfdef_dir(self, ctx:PLParser.Ifdef_dirContext):
        pass


    # Enter a parse tree produced by PLParser#ifndef_dir.
    def enterIfndef_dir(self, ctx:PLParser.Ifndef_dirContext):
        pass

    # Exit a parse tree produced by PLParser#ifndef_dir.
    def exitIfndef_dir(self, ctx:PLParser.Ifndef_dirContext):
        pass


    # Enter a parse tree produced by PLParser#undefine_dir.
    def enterUndefine_dir(self, ctx:PLParser.Undefine_dirContext):
        pass

    # Exit a parse tree produced by PLParser#undefine_dir.
    def exitUndefine_dir(self, ctx:PLParser.Undefine_dirContext):
        pass


    # Enter a parse tree produced by PLParser#script_block.
    def enterScript_block(self, ctx:PLParser.Script_blockContext):
        pass

    # Exit a parse tree produced by PLParser#script_block.
    def exitScript_block(self, ctx:PLParser.Script_blockContext):
        pass


    # Enter a parse tree produced by PLParser#script_body.
    def enterScript_body(self, ctx:PLParser.Script_bodyContext):
        pass

    # Exit a parse tree produced by PLParser#script_body.
    def exitScript_body(self, ctx:PLParser.Script_bodyContext):
        pass



del PLParser