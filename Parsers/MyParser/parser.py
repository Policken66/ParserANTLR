from Parsers.MyParser.lexer import Token

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.errors = []

    def current(self):
        if self.pos >= len(self.tokens):
            return self.tokens[-1]  # EOF
        return self.tokens[self.pos]

    def add_error(self, message):
        tok = self.current()
        self.errors.append((tok.line, tok.column, message))

    def eat(self, token_type):
        tok = self.current()
        if tok.type == token_type:
            self.pos += 1
        else:
            self.add_error(f"Ожидался {token_type}, получил {tok.type}")
            self.pos += 1  # recovery

    def parse(self):
        self.output()
        self.eat("SEMICOLON")
        return self.errors

    def output(self):
        self.eat("COUT")
        self.eat("SHIFT")
        self.item()

        while self.current().type != "EOF" and self.current().type == "SHIFT":
            self.eat("SHIFT")
            self.item()

    def item(self):
        tok = self.current()
        if tok.type in ("ID", "STR", "NUM"):
            self.eat(tok.type)
        else:
            self.add_error(f"Expected ID, STR or NUM, got {tok.type}")
            self.pos += 1  # recovery
