from PySide6.QtWidgets import QMainWindow

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
            output_str = "мой парсер"

        self.plainTextEdit_log.setPlainText(output_str)

