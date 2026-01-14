from PySide6.QtWidgets import QMainWindow, QMessageBox

from Parsers.MyParser.lexer import Lexer
from Parsers.MyParser.parser import Parser
from Parsers.ParserANTLR.advanced_cout_parser import parse_with_all_errors
from Parsers.ParserPL import advanced_pl_parser
from UI.MainWindow import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, main_window):
        super().setupUi(main_window)

        self.plainTextEdit_log.setReadOnly(True)
        self.action_start.triggered.connect(self.action_start_triggered)
        self.action_text.triggered.connect(self.action_text_triggered)
        self.action_reference.triggered.connect(self.action_reference_triggered)
        self.action_correction.triggered.connect(self.action_correction_triggered)
        self.comboBox_parser_name.addItem("Мой парсер")
        self.comboBox_parser_name.addItem("Парсер ANTLR")
        self.comboBox_parser_name.addItem("ANTLER PL")

    def action_correction_triggered(self):
        self.plainTextEdit_input.clear()
        self.plainTextEdit_log.clear()
    def action_start_triggered(self):
        text = self.plainTextEdit_input.toPlainText()
        output_str = ""
        if self.comboBox_parser_name.currentText() == "Парсер ANTLR":
            success, result, output = parse_with_all_errors(text)
            if success:
                output_str = f"✓ УСПЕХ: {output}"
            else:
                output_str = f"✗ ОШИБКИ: {result}"

        if self.comboBox_parser_name.currentText() == "Мой парсер":
            lexer = Lexer(text)
            tokens = lexer.tokenize()

            parser = Parser(tokens)
            errors = lexer.errors + parser.parse()

            if not errors:
                output_str = "✓ УСПЕХ"
            else:
                output_lines = []
                for line, col, msg in errors:
                    output_lines.append(f"{line}:{col} — {msg}")
                output_str = f"✗ ОШИБКИ: \n" + "\n".join(output_lines)

        if self.comboBox_parser_name.currentText() == "ANTLER PL":
            success, result, output = advanced_pl_parser.parse_with_all_errors(text)
            if success:
                output_str = f"✓ УСПЕХ: {output}"
            else:
                output_str = f"✗ ОШИБКИ: {result}"

        self.plainTextEdit_log.setPlainText(output_str)

    def action_text_triggered(self):
        text_info = (
            "Вариант: №17 – оператор потокового вывода << языка C++\n\n"
            "Оператор << используется для передачи значений в поток cout.\n"
            "Пример использования:\n"
            "cout << \"Value = \" << x;\n\n"
            "Грамматика:\n"
            "S → Output ;\n"
            "Output → cout << Item (<< Item)*\n"
            "Item → ID | STR | NUM\n\n"
            "Ограничения модели:\n"
            "1. cout – единственный поток вывода.\n"
            "2. Правый операнд – идентификатор, строковый или числовой литерал.\n"
            "3. Завершается символом ;"
        )
        QMessageBox.information(self, "Текст варианта", text_info)

    def action_reference_triggered(self):
        help_text = (
            "Это лабораторная работа по синтаксическому анализу.\n"
            "Реализуется парсер для оператора потокового вывода << языка C++.\n"
            "Парсер анализирует ограниченный подъязык с единственным потоком вывода cout.\n"
        )
        QMessageBox.information(self, "Справка", help_text)