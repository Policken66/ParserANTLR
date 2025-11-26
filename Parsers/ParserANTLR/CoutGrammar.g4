grammar CoutGrammar;

// Parser rules
s: output ';' EOF;

output: 'cout' '<<' item ('<<' item)*;

item: ID | STR | NUM;

// Lexer rules
COUT: 'cout';
END: ';';
OUT_OP: '<<';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
STR: '"' (~["\\\r\n] | '\\' .)* '"';
NUM: [0-9]+ ('.' [0-9]+)?;

WS: [ \t\r\n]+ -> skip;