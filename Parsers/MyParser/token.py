from enum import Enum, auto

class TokenType(Enum):
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()
    COUT = auto()
    LPAREN = auto()
    RPAREN = auto()
    SEMI = auto()
    ERROR = auto()
    EOF = auto()

class Token:
    def __init__(self, type, text, line, col):
        self.type = type
        self.text = text
        self.line = line
        self.col = col

    @property
    def position(self):
        return f"{self.line}:{self.col}"
