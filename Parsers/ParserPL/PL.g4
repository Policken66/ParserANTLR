// PL.g4
grammar PL;

program        : statement_list EOF ;

statement_list : statement ';' statement_list
               | ;

statement      : var_decl
               | expr ;

var_decl       : 'var' ID var_decl_tail ;

var_decl_tail  : '=' expr
               | id_list_tail ;

id_list_tail   : ',' ID id_list_tail
               | ;

expr           : call
               | ID
               | NUMBER
               | STRING ;

call           : ID '(' arg_list ')' ;

arg_list       : expr arg_list_tail
               | ;

arg_list_tail  : ',' expr arg_list_tail
               | ;


ID     : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER : '-'? [0-9]+ ('.' [0-9]+)? ;
STRING : '"' (~["\r\n])* '"' ;
WS     : [ \t\r\n]+ -> skip ;

