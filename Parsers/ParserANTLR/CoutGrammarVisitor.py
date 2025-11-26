# Generated from CoutGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CoutGrammarParser import CoutGrammarParser
else:
    from CoutGrammarParser import CoutGrammarParser

# This class defines a complete generic visitor for a parse tree produced by CoutGrammarParser.

class CoutGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CoutGrammarParser#s.
    def visitS(self, ctx:CoutGrammarParser.SContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoutGrammarParser#output.
    def visitOutput(self, ctx:CoutGrammarParser.OutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CoutGrammarParser#item.
    def visitItem(self, ctx:CoutGrammarParser.ItemContext):
        return self.visitChildren(ctx)



del CoutGrammarParser