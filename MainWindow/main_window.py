from PySide6.QtWidgets import QMainWindow

from Parsers.MyParser.lexer import Lexer
from Parsers.MyParser.parser import Parser
from Parsers.MyParser.error_collector  import ErrorCollector
from Parsers.ParserANTLR.advanced_cout_parser import parse_with_all_errors
from UI.MainWindow import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, main_window):
        super().setupUi(main_window)

        self.plainTextEdit_log.setReadOnly(True)
        self.action_start.triggered.connect(self.action_start_triggered)
        self.comboBox_parser_name.addItem("Парсер ANTLR")
        self.comboBox_parser_name.addItem("Мой парсер")

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
            success, result = parser.parse()

            if success:
                output_str = "✓ УСПЕХ"
            else:
                output_str = f"✗ ОШИБКИ: {result}"

        self.plainTextEdit_log.setPlainText(output_str)

