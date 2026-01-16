grammar PL;


program        : (statement ';')* EOF ;
statement      : var_decl | expr ;
var_decl       : 'var' ID ( '=' expr | (',' ID)* ) ;
expr           : ID ('(' arg_list ')')? | NUMBER | STRING ;
arg_list       : expr (',' expr)* ;


ID     : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER : '-'? [0-9]+ ('.' [0-9]+)? ;
STRING : '"' (~["\r\n])* '"' ;
WS     : [ \t\r\n]+ -> skip ;


