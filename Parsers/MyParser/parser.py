from Parsers.MyParser.token import TokenType
from Parsers.MyParser.error_collector import ErrorCollector


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current = tokens[0]
        self.error_collector = ErrorCollector()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current = self.tokens[self.pos]
        else:
            self.current = self.tokens[-1]  # EOF fallback

    def error(self, msg):
        self.error_collector.add_error(
            msg, f"{self.current.line}:{self.current.col}"
        )

    def parse(self):
        self.parse_S()

        # добавляем ошибки ЛЕКСЕРА
        lexer_errors = [
            f"Ошибка {err}" for err in getattr(self.tokens, "lexer_errors", [])
        ]

        self.error_collector.extend_errors(lexer_errors)

        errors = self.error_collector.to_string()

        if errors.strip() == "":
            return True, ""
        return False, errors

    # ------------------- GRAMMAR -------------------
    # S : output ;
    def parse_S(self):
        self.parse_output()

    # output : item* ;
    def parse_output(self):
        while self.current.type != TokenType.EOF:
            self.parse_item()

    # item : IDENTIFIER | NUMBER | STRING | '(' item ')' | error
    def parse_item(self):

        # корректные атомы
        if self.current.type in (TokenType.IDENTIFIER, TokenType.NUMBER, TokenType.STRING):
            self.advance()
            return

        # ( item )
        if self.current.type == TokenType.LPAREN:
            self.advance()
            self.parse_item()
            if self.current.type == TokenType.RPAREN:
                self.advance()
            else:
                self.error(f"ожидалась ')', найдено '{self.current.text}'")
            return

        # Ошибка
        if self.current.type == TokenType.ERROR:
            self.error(f"некорректный токен '{self.current.text}'")
            self.advance()
            return

        # Всё остальное — ошибка синтаксиса
        self.error(f"mismatched input '{self.current.text}'")
        self.advance()
