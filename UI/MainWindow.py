# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPlainTextEdit, QSizePolicy, QSpacerItem,
    QStatusBar, QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 400)
        self.action_start = QAction(MainWindow)
        self.action_start.setObjectName(u"action_start")
        self.action_start.setMenuRole(QAction.MenuRole.NoRole)
        self.action_file = QAction(MainWindow)
        self.action_file.setObjectName(u"action_file")
        self.action_file.setMenuRole(QAction.MenuRole.NoRole)
        self.action_correction = QAction(MainWindow)
        self.action_correction.setObjectName(u"action_correction")
        self.action_correction.setMenuRole(QAction.MenuRole.NoRole)
        self.action_text = QAction(MainWindow)
        self.action_text.setObjectName(u"action_text")
        self.action_text.setMenuRole(QAction.MenuRole.NoRole)
        self.action_reference = QAction(MainWindow)
        self.action_reference.setObjectName(u"action_reference")
        self.action_reference.setMenuRole(QAction.MenuRole.NoRole)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit_input = QPlainTextEdit(self.centralWidget)
        self.plainTextEdit_input.setObjectName(u"plainTextEdit_input")

        self.verticalLayout.addWidget(self.plainTextEdit_input)

        self.horizontalLayout_parser_name = QHBoxLayout()
        self.horizontalLayout_parser_name.setSpacing(6)
        self.horizontalLayout_parser_name.setObjectName(u"horizontalLayout_parser_name")
        self.label_parser_name = QLabel(self.centralWidget)
        self.label_parser_name.setObjectName(u"label_parser_name")

        self.horizontalLayout_parser_name.addWidget(self.label_parser_name)

        self.comboBox_parser_name = QComboBox(self.centralWidget)
        self.comboBox_parser_name.setObjectName(u"comboBox_parser_name")

        self.horizontalLayout_parser_name.addWidget(self.comboBox_parser_name)

        self.horizontalSpacer_parser_name = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_parser_name.addItem(self.horizontalSpacer_parser_name)


        self.verticalLayout.addLayout(self.horizontalLayout_parser_name)

        self.plainTextEdit_log = QPlainTextEdit(self.centralWidget)
        self.plainTextEdit_log.setObjectName(u"plainTextEdit_log")

        self.verticalLayout.addWidget(self.plainTextEdit_log)

        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.mainToolBar.addAction(self.action_file)
        self.mainToolBar.addAction(self.action_correction)
        self.mainToolBar.addAction(self.action_text)
        self.mainToolBar.addAction(self.action_start)
        self.mainToolBar.addAction(self.action_reference)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0441\u0435\u0440", None))
        self.action_start.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0441\u043a", None))
#if QT_CONFIG(tooltip)
        self.action_start.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a \u043f\u0430\u0440\u0441\u0435\u0440\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.action_file.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
#if QT_CONFIG(tooltip)
        self.action_file.setToolTip(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
#endif // QT_CONFIG(tooltip)
        self.action_correction.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043a\u0430", None))
        self.action_text.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442", None))
        self.action_reference.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.label_parser_name.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0441\u0435\u0440:", None))
    # retranslateUi

