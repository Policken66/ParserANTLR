grammar PL;

// PARSER

model : (statement)* EOF;
statement : declaration | equation | call_stmt | control_statement
          | routine_definition | directive | script_block | block;

declaration : var_decl | const_decl | input_decl
            | output_decl | init_decl;
var_decl : VAR var_item (COMMA var_item)* SEMI;
var_item : lvalue (COLON type_name)? (ASSIGN expression)?;
type_name : ID;
const_decl : CONST const_item (COMMA const_item)* SEMI;
const_item : ID ASSIGN expression;
input_decl : INPUT ident_list SEMI;
output_decl : OUTPUT output_item (COMMA output_item)* SEMI;
output_item : lvalue;
lvalue : ID (LBRACK expression RBRACK)*;
init_decl : INIT init_item (COMMA init_item)* SEMI;
init_item : lvalue (ASSIGN expression)?;
ident_list : ident (COMMA ident)*;
ident : ID;

equation : lhs ASSIGN expression SEMI;
lhs : ID (derivative_mark)? (LBRACK expression RBRACK)*;
derivative_mark : QUOTE1+;

expression : or_expr;
or_expr : and_expr (OR_OP and_expr)*;
and_expr : eq_expr (AND_OP eq_expr)*;
eq_expr : rel_expr ((ASSIGN | EQUAL | NOTEQUAL) rel_expr)?;
rel_expr : add_expr ((LT | GT | LE | GE) add_expr)*;
add_expr : mul_expr ((ADD | SUB) mul_expr)*;
mul_expr : pow_expr ((MUL | DIV) pow_expr)*;
pow_expr : unary_expr (POW pow_expr)?;
unary_expr : (ADD | SUB | NOT_OP | BANG) unary_expr | primary;
primary : literal | lvalue | func_call
        | array_literal | LPAREN expression RPAREN;
func_call : ident LPAREN arg_list? RPAREN;
arg_list : expression (COMMA expression)*;
literal : NUMBER | STRING;
array_literal : LBRACK expression (COMMA expression)* RBRACK;

control_statement : if_stmt | while_stmt | for_stmt
                  | repeat_stmt | switch_stmt | exit_stmt
                  | goto_stmt | label_stmt | inline_stmt;
if_stmt : IF expression THEN stmt_or_block (ELSE stmt_or_block)?;
stmt_or_block : equation | call_stmt | control_statement | block;
block : BEGIN statement* END SEMI;
while_stmt : WHILE expression DO stmt_or_block;
for_stmt : FOR ident ASSIGN expression (TO | DOWNTO) expression DO stmt_or_block
         | FOR LPAREN for_init COMMA expression (COMMA expression)? RPAREN stmt_or_block SEMI?;
for_init : ident ASSIGN expression;
repeat_stmt : REPEAT stmt_or_block+ UNTIL expression SEMI;
switch_stmt : SWITCH LPAREN expression RPAREN BEGIN switch_case+ (ELSE stmt_or_block)? END SEMI;
switch_case : expr_list COLON stmt_or_block SEMI;
expr_list : expression (COMMA expression)*;
exit_stmt : EXIT SEMI;
goto_stmt : GOTO ident SEMI;
label_stmt : ident COLON stmt_or_block;
call_stmt : func_call SEMI;
inline_stmt : INLINE SEMI;

routine_definition : function_def | procedure_def;
function_def : FUNCTION ident formal_params? (COLON type_name)? routine_body END SEMI;
procedure_def : PROCEDURE ident formal_params? routine_body END SEMI;
formal_params : LPAREN param (COMMA param)* RPAREN;
param : (OUT)? ident (COLON type_name)? (ASSIGN expression)?;
routine_body : statement*;

directive : define_dir | include_dir | ifdef_dir
                       | ifndef_dir | undefine_dir;
define_dir : DEFINE ID ASSIGN expression SEMI;
include_dir : INCLUDE STRING SEMI;
ifdef_dir : IFDEF ID statement* ENDIF;
ifndef_dir : IFNDEF ID statement* ENDIF;
undefine_dir : UNDEFINE ID SEMI;

script_block : SECTION script_body ENDSCRIPT
             | APPLYNOW script_body ENDSCRIPT;
script_body : statement*;


// LEXER

VAR : 'var'; CONST : 'const'; INIT : 'init';
INPUT : 'input'; OUTPUT : 'output';

IF : 'if'; THEN : 'then'; ELSE : 'else';
WHILE : 'while'; DO : 'do';
FOR : 'for'; TO : 'to'; DOWNTO : 'downto';
REPEAT : 'repeat'; UNTIL : 'until';
EXIT : 'exit';
SWITCH : 'switch';
GOTO : 'goto';

OUT : 'out'; INLINE : 'inline';
BEGIN : 'begin'; END : 'end';
FUNCTION : 'function'; PROCEDURE : 'procedure';
DEFINE : 'define'; INCLUDE : 'include';
IFDEF : 'ifdef'; IFNDEF : 'ifndef';
UNDEFINE : 'undefine'; ENDIF : 'endif';
SECTION : 'section';
APPLYNOW : 'applynow';
ENDSCRIPT: 'endscript';

EQUAL : '=='; NOTEQUAL : '!=';
LE : '<='; GE : '>='; ASSIGN : '=';
LT : '<'; GT : '>';
ADD : '+'; SUB : '-'; MUL : '*'; DIV : '/';
POW: '^'; BANG : '!'; QUOTE1 : '\'';
OR_OP : 'or'  | 'OR'  | '||';
AND_OP : 'and' | 'AND' | '&&';
NOT_OP : 'not' | 'NOT';
LPAREN : '('; RPAREN : ')';
LBRACK : '['; RBRACK : ']';
COMMA : ','; SEMI : ';'; COLON : ':';

NUMBER : DIGIT+ ('.' DIGIT+)? EXP? | '.' DIGIT+ EXP?;
fragment EXP : [eE] [+\-]? DIGIT+ ;
fragment DIGIT : [0-9] ;
STRING : '"' ( '\\"' | ~["\r\n] )* '"';
ID : [a-zA-Z_] [a-zA-Z0-9_]*;
WS : [ \t\r\n]+ -> skip;
LINE_COMMENT : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/*' .*? '*/' -> skip;
