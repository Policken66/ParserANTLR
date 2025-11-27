class ErrorCollector:
    def __init__(self):
        self.errors = []

    def add_error(self, message, position):
        self.errors.append(f"Ошибка на позиции {position} — {message}")

    def extend_errors(self, error_list):
        for err in error_list:
            self.errors.append(err)

    def to_string(self):
        if not self.errors:
            return ""
        res = "Найдены ошибки:\n"
        for i, err in enumerate(self.errors, 1):
            res += f"{i}. {err}\n"
        return res
