# Generated from CoutGrammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,23,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,5,1,16,8,1,10,1,12,1,19,9,1,1,2,1,2,1,2,0,0,3,0,2,4,0,1,1,0,
        4,6,20,0,6,1,0,0,0,2,10,1,0,0,0,4,20,1,0,0,0,6,7,3,2,1,0,7,8,5,2,
        0,0,8,9,5,0,0,1,9,1,1,0,0,0,10,11,5,1,0,0,11,12,5,3,0,0,12,17,3,
        4,2,0,13,14,5,3,0,0,14,16,3,4,2,0,15,13,1,0,0,0,16,19,1,0,0,0,17,
        15,1,0,0,0,17,18,1,0,0,0,18,3,1,0,0,0,19,17,1,0,0,0,20,21,7,0,0,
        0,21,5,1,0,0,0,1,17
    ]

class CoutGrammarParser ( Parser ):

    grammarFileName = "CoutGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'cout'", "';'", "'<<'" ]

    symbolicNames = [ "<INVALID>", "COUT", "END", "OUT_OP", "ID", "STR", 
                      "NUM", "WS" ]

    RULE_s = 0
    RULE_output = 1
    RULE_item = 2

    ruleNames =  [ "s", "output", "item" ]

    EOF = Token.EOF
    COUT=1
    END=2
    OUT_OP=3
    ID=4
    STR=5
    NUM=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def output(self):
            return self.getTypedRuleContext(CoutGrammarParser.OutputContext,0)


        def END(self):
            return self.getToken(CoutGrammarParser.END, 0)

        def EOF(self):
            return self.getToken(CoutGrammarParser.EOF, 0)

        def getRuleIndex(self):
            return CoutGrammarParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = CoutGrammarParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.output()
            self.state = 7
            self.match(CoutGrammarParser.END)
            self.state = 8
            self.match(CoutGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COUT(self):
            return self.getToken(CoutGrammarParser.COUT, 0)

        def OUT_OP(self, i:int=None):
            if i is None:
                return self.getTokens(CoutGrammarParser.OUT_OP)
            else:
                return self.getToken(CoutGrammarParser.OUT_OP, i)

        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoutGrammarParser.ItemContext)
            else:
                return self.getTypedRuleContext(CoutGrammarParser.ItemContext,i)


        def getRuleIndex(self):
            return CoutGrammarParser.RULE_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput" ):
                return visitor.visitOutput(self)
            else:
                return visitor.visitChildren(self)




    def output(self):

        localctx = CoutGrammarParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_output)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(CoutGrammarParser.COUT)
            self.state = 11
            self.match(CoutGrammarParser.OUT_OP)
            self.state = 12
            self.item()
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 13
                self.match(CoutGrammarParser.OUT_OP)
                self.state = 14
                self.item()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CoutGrammarParser.ID, 0)

        def STR(self):
            return self.getToken(CoutGrammarParser.STR, 0)

        def NUM(self):
            return self.getToken(CoutGrammarParser.NUM, 0)

        def getRuleIndex(self):
            return CoutGrammarParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = CoutGrammarParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





