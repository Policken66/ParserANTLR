class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.errors = []

    def current(self):
        if self.pos >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[self.pos]

    def add_error(self, message):
        tok = self.current()
        self.errors.append((tok.line, tok.column, message))

    def eat(self, token_type):
        tok = self.current()
        if tok.type == token_type:
            self.pos += 1
            return True
        else:
            self.add_error(f"Ожидался {token_type}, получил {tok.type}")
            return False

    def skip_to_semicolon(self):
        while self.current().type not in ("SEMICOLON", "EOF"):
            self.pos += 1

    def parse(self):
        self.output()
        self.eat("SEMICOLON")
        return self.errors

    def output(self):

        # ---- COUT ----
        if not self.eat("COUT"):
            self.skip_to_semicolon()
            return  # ❗ прекращаем попытки парсить output

        # ---- OPERATOR ----
        if not self.eat("OPERATOR"):
            self.skip_to_semicolon()
            return

        # ---- item ----
        if not self.item():
            self.skip_to_semicolon()
            return

        # ---- repeated: << value ----
        while self.current().type == "OPERATOR":
            if not self.eat("OPERATOR"):
                self.skip_to_semicolon()
                return
            if not self.item():
                self.skip_to_semicolon()
                return

    def item(self):
        tok = self.current()
        if tok.type in ("ID", "STR", "NUM"):
            self.eat(tok.type)
            return True
        else:
            self.add_error(
                f"Ожидался ID, STR или NUM, получен {tok.type}"
            )
            return False
