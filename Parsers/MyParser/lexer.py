from Parsers.MyParser.token import Token, TokenType


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.col = 0
        self.errors = []

    def peek(self):
        if self.pos >= len(self.text):
            return None
        return self.text[self.pos]

    def advance(self):
        ch = self.peek()
        self.pos += 1
        self.col += 1
        return ch

    def tokenize(self):
        tokens = []

        while True:
            ch = self.peek()
            if ch is None:
                break

            if ch.isspace():
                self.advance()
                continue

            start_col = self.col

            # Идентификатор
            if ch.isalpha():
                ident = ""
                while self.peek() and self.peek().isalnum():
                    ident += self.advance()

                if ident == "cout":
                    tokens.append(Token(TokenType.COUT, ident, self.line, start_col))
                else:
                    tokens.append(Token(TokenType.IDENTIFIER, ident, self.line, start_col))
                continue

            # Число
            if ch.isdigit():
                num = ""
                while self.peek() and self.peek().isdigit():
                    num += self.advance()
                tokens.append(Token(TokenType.NUMBER, num, self.line, start_col))
                continue

            # Строка
            if ch == '"':
                self.advance()
                text = ""
                while self.peek() not in ('"', None):
                    text += self.advance()
                if self.peek() == '"':
                    self.advance()
                    tokens.append(Token(TokenType.STRING, text, self.line, start_col))
                else:
                    self.errors.append(f"Ошибка {self.line}:{start_col}: не закрытая строка")
                continue

            # Односимвольные токены
            one_char = {
                '(': TokenType.LPAREN,
                ')': TokenType.RPAREN,
                ';': TokenType.SEMI
            }

            if ch in one_char:
                self.advance()
                tokens.append(Token(one_char[ch], ch, self.line, start_col))
                continue

            # Ошибка
            self.errors.append(f"token recognition error at: '{ch}' ({self.line}:{start_col})")
            tokens.append(Token(TokenType.ERROR, ch, self.line, start_col))
            self.advance()

        tokens.append(Token(TokenType.EOF, "<EOF>", self.line, self.col))
        return tokens
