import re


class Token:
    def __init__(self, type_, value, line, column):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, {self.value}, {self.line}:{self.column})"


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.column = 1
        self.errors = []

    def advance(self):
        ch = self.text[self.pos]
        self.pos += 1
        if ch == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        return ch

    def peek(self):
        return self.text[self.pos] if self.pos < len(self.text) else None

    def skip_ws(self):
        while self.peek() and self.peek().isspace():
            self.advance()

    def string_literal(self):
        start_line = self.line
        start_col = self.column
        self.advance()  # skip opening "

        value = ""
        while True:
            ch = self.peek()
            if ch is None:  # EOF
                self.errors.append((start_line, start_col, "Unterminated string literal"))
                return Token("STR", value, start_line, start_col)

            if ch == '"':
                self.advance()  # consume closing "
                return Token("STR", value, start_line, start_col)

            value += self.advance()

    def number(self):
        start_line, start_col = self.line, self.column
        num = ""

        while self.peek() and self.peek().isdigit():
            num += self.advance()

        if self.peek() == '.':
            num += self.advance()
            while self.peek() and self.peek().isdigit():
                num += self.advance()

        return Token("NUM", num, start_line, start_col)

    def identifier(self):
        start_line, start_col = self.line, self.column
        ident = ""

        # Только латиница + цифры + _
        if not re.match(r'[a-zA-Z_]', self.peek()):
            self.errors.append((start_line, start_col, f"Invalid identifier start '{self.peek()}'"))
            invalid_tok = Token("INVALID_ID", self.peek(), start_line, start_col)
            self.advance()  # recovery
            return invalid_tok

        while self.peek() and re.match(r'[a-zA-Z0-9_]', self.peek()):
            ident += self.advance()

        if ident == "cout":
            return Token("COUT", ident, start_line, start_col)
        return Token("ID", ident, start_line, start_col)

    def tokenize(self):
        tokens = []

        while self.peek() is not None:
            self.skip_ws()

            ch = self.peek()
            if ch is None:
                break

            # Строка
            if ch == '"':
                tokens.append(self.string_literal())
                continue

            # Число
            if ch.isdigit():
                tokens.append(self.number())
                continue

            # Идентификатор / cout
            if ch.isalpha() or ch == "_":    # <--- Теперь ловит Unicode буквы
                tokens.append(self.identifier())
                continue

            # SHIFT <<
            if ch == '<' and self.pos + 1 < len(self.text) and self.text[self.pos + 1] == '<':
                tokens.append(Token("SHIFT", "<<", self.line, self.column))
                self.advance()
                self.advance()
                continue

            # SEMICOLON
            if ch == ';':
                tokens.append(Token("SEMICOLON", ';', self.line, self.column))
                self.advance()
                continue

            # ❗ Неизвестный символ
            self.errors.append((self.line, self.column, f"Unknown symbol '{ch}'"))
            self.advance()
            continue

        tokens.append(Token("EOF", None, self.line, self.column))
        return tokens
