# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'anasayfa_tabeVParo.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 613)
        MainWindow.setStyleSheet(u"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: #3a3a3a;\n"
"	color: #fff;\n"
"	selection-background-color: #b78620;\n"
"	selection-color: #000;\n"
"\n"
"}\n"
"/*-----QTable----*/\n"
"QTableWidget\n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"\n"
"}\n"
"QTableWidget::item:selected {\n"
"background-color: #FFFF00; \n"
"color: #000000;\n"
"}\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"	border: 1px solid #000;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item \n"
"{\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected \n"
"{\n"
"	background-color: rgba(183, 134, 32, 20%);\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed \n"
"{\n"
"	back"
                        "ground-color: rgb(183, 134, 32);\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #222;\n"
"    padding: 4px;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"   	background-color: rgb(183, 134, 32);\n"
"	height: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #555;\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"	background-color: rgba(183, 134, 32, 20%);\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolBar-----*/\n"
"QToolBar\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2"
                        ":1, stop:0 rgba(69, 69, 69, 255),stop:1 rgba(58, 58, 58, 255));\n"
"	border-top: none;\n"
"	border-bottom: 1px solid #4f4f4f;\n"
"	border-left: 1px solid #4f4f4f;\n"
"	border-right: 1px solid #4f4f4f;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolBar::separator\n"
"{\n"
"	background-color: #2e2e2e;\n"
"	width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton \n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"	padding: 5px;\n"
"	padding-left: 8px;\n"
"	padding-right: 8px;\n"
"	margin-left: 1px;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover\n"
"{\n"
"	background-color: rgba(183, 134, 32, 20%);\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"	\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"	border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:checked\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba("
                        "57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"	border: 1px solid #222;\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"	color: #ffffff;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"	font: bold 12px;\n"
"}\n"
"\n"
"\n"
"QPushButton::flat\n"
"{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgba(183, 134, 32, 20%);\n"
"	border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49,"
                        " 49, 49, 255));\n"
"	border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::checked\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #131313;\n"
"	color : #eee;\n"
"	border: 1px solid #343434;\n"
"	border-radius: 3px;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"/*-----QTExtEdit-----*/\n"
"QTextEdit\n"
"{\n"
"	background-color: #000000;\n"
"	color : #fff;\n"
"	border: 1px solid #343434;\n"
"	border-radius: 4px;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"/*-----QTabBar-----*/\n"
"QTabBar::tab\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #666;\n"
"	border-bottom: none"
                        ";\n"
"	padding: 5px;\n"
"	padding-left: 15px;\n"
"	padding-right: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane \n"
"{\n"
"	background-color: red;\n"
"	border: 1px solid #666;\n"
"	top: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"	margin-right: 0; \n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
"	background-color: #0c0c0d;\n"
"	margin-left: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"	color: #b1b1b1;\n"
"	border-bottom-style: solid;\n"
"	background-color: #0c0c0d;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"	margin-bottom: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"	border-top-color: #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"    border: 1px solid #000;\n"
"    padding-left: 6px;\n"
"    color: #ffffff;\n"
"    height: 20px;\n"
"\n"
"}\n"
"\n"
""
                        "\n"
"QComboBox::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #b78620;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #383838;\n"
"    color: #ffffff;\n"
"    border: 1px solid black;\n"
"    selection-background-color: #b78620;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"\n"
"/*-----QSpinBox & QDateTimeEdit-----*/\n"
"QSpinBox,\n"
"QD"
                        "ateTimeEdit \n"
"{\n"
"    background-color: #131313;\n"
"	color : #eee;\n"
"	border: 1px solid #343434;\n"
"	padding: 3px;\n"
"	padding-left: 5px;\n"
"    border-radius : 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, \n"
"QDateTimeEdit::up-button\n"
"{\n"
"	border-top-right-radius:2px;\n"
"	background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover, \n"
"QDateTimeEdit::up-button:hover\n"
"{\n"
"	background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed, \n"
"QDateTimeEdit::up-button:pressed\n"
"{\n"
"	background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDateTimeEdit::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button, \n"
"QDateTimeEdit::down-button\n"
"{\n"
"	border-bottom-right-radius:2px;\n"
"	background-color: #777777;\n"
"    width: 16px; \n"
"    bord"
                        "er-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button:hover, \n"
"QDateTimeEdit::down-button:hover\n"
"{\n"
"	background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button:pressed, \n"
"QDateTimeEdit::down-button:pressed\n"
"{\n"
"	background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDateTimeEdit::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QGroupBox-----*/\n"
"QGroupBox \n"
"{\n"
"    border: 1px solid;\n"
"    border-color: #666666;\n"
"	border-radius: 5px;\n"
"    margin-top: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title  \n"
"{\n"
"    background-color: transparent;\n"
"    color: #eee;\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px;\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QHeaderView-----*/\n"
"QHeaderView::section\n"
"{\n"
"    background-color: qlineargrad"
                        "ient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"	border: 1px solid #000;\n"
"    color: #fff;\n"
"    text-align: left;\n"
"	padding: 4px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
" "
                        "   border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"	border: 1px solid #000;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeWidget-----*/\n"
"QTreeView\n"
"{\n"
"	show-decoration-selected: 1;\n"
"	alternate-background-color: #3a3a3a;\n"
"	selection-color: #fff;\n"
"	background-color: #2d2d2d;\n"
"	border: 1px solid gray;\n"
"	padding-top : 5px;\n"
"	color: #fff;\n"
"	font: 8pt;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected\n"
"{\n"
"	color:#fff;\n"
"	background-color: #b78620;\n"
"	border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"    background-color: #262626;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"	image: url(://tree-closed.png"
                        ");\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"	image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 83, 83, 255),stop:0.293269 rgba(81, 81, 81, 255),stop:0.634615 rgba(79, 79, 79, 255),stop:1 rgba(83, 83, 83, 255));\n"
"    border : none;\n"
"    color: white;\n"
"    show-decoration-selected: 1; \n"
"    outline: 0;\n"
"	border: 1px solid gray;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::disabled \n"
"{\n"
"	background-color: #656565;\n"
"	color: #1b1b1b;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item \n"
"{\n"
"	background-color: #2d2d2d;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:alternate \n"
"{\n"
"    background-color: #3a3a3a;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected \n"
"{\n"
"	background-color: #b78620;\n"
"	border: 1"
                        "px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:!active \n"
"{\n"
"	background-color: #b78620;\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:active \n"
"{\n"
"	background-color: #b78620;\n"
"	border: 1px solid #b78620;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #262626;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"	background-color: transparent;\n"
"    color: lightgray;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: #323232;\n"
"    border: 1px solid darkgray;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"	background-color: #b78620;\n"
"    border: 1px solid #3a546e;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"	borde"
                        "r: 1px solid #b78620; \n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QRadioButton-----*/\n"
"QRadioButton \n"
"{\n"
"	color: lightgray;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover \n"
"{\n"
"	background-color: lightgray;\n"
"	border: 2px solid #b78620;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked \n"
"{\n"
"	border: 2px solid #b78620;\n"
"	border-radius: 6px;\n"
"	background-color: rgba(183,134,32,20%);  \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSlider-----*/\n"
"QSlider::groove:horizontal \n"
"{\n"
"	background-color: transparent;\n"
"	height: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal \n"
"{\n"
"	background-color: #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizo"
                        "ntal \n"
"{\n"
"	background-color: #131313;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal \n"
"{\n"
"	background-color: #b78620;\n"
"	width: 14px;\n"
"	margin-top: -6px;\n"
"	margin-bottom: -6px;\n"
"	border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover \n"
"{\n"
"	background-color: #d89e25;\n"
"	border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal:disabled \n"
"{\n"
"	background-color: #bbb;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border: 1px solid #aaa;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #3d3d3d;\n"
"    height: 15px;\n"
"    margin: 0px 16px 0 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"	back"
                        "ground-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    width: 15px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-"
                        "arrow:horizontal\n"
"{\n"
"    image: url(://arrow-left.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #3d3d3d;\n"
"    width: 16px;\n"
"	border: 1px solid #2d2d2d;\n"
"    margin: 16px 0px 16px 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    height: 15px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-li"
                        "ne:vertical\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"	border: 1px solid #2d2d2d;\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"    border: 1px solid #666666;\n"
"    text-align: center;\n"
"	color: #000;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #b78620;\n"
"    width: 30px;\n"
"    margin: 0.5px;\n"
"\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(9, 9, 811, 601))
        self.tabWidget.setMaximumSize(QSize(826, 16777215))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(5, 5))
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frmTable = QFrame(self.tab)
        self.frmTable.setObjectName(u"frmTable")
        self.frmTable.setGeometry(QRect(10, 270, 800, 400))
        self.frmTable.setMinimumSize(QSize(800, 400))
        self.frmTable.setMaximumSize(QSize(1000, 360))
        self.frmTable.setFrameShape(QFrame.StyledPanel)
        self.frmTable.setFrameShadow(QFrame.Raised)
        self.tblKitap = QTableWidget(self.frmTable)
        self.tblKitap.setObjectName(u"tblKitap")
        self.tblKitap.setGeometry(QRect(0, 0, 800, 300))
        self.tblKitap.setMinimumSize(QSize(800, 300))
        self.tblKitap.setMaximumSize(QSize(790, 300))
        self.tblKitap.horizontalHeader().setCascadingSectionResizes(False)
        self.tblKitap.horizontalHeader().setMinimumSectionSize(40)
        self.tblKitap.verticalHeader().setMinimumSectionSize(30)
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_11 = QHBoxLayout(self.widget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frmGiris = QFrame(self.widget)
        self.frmGiris.setObjectName(u"frmGiris")
        self.frmGiris.setMaximumSize(QSize(250, 260))
        self.frmGiris.setFrameShape(QFrame.StyledPanel)
        self.frmGiris.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frmGiris)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(1, 2, 1, 2)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leKitapAdi = QLineEdit(self.frmGiris)
        self.leKitapAdi.setObjectName(u"leKitapAdi")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leKitapAdi.sizePolicy().hasHeightForWidth())
        self.leKitapAdi.setSizePolicy(sizePolicy)
        self.leKitapAdi.setMinimumSize(QSize(0, 26))
        self.leKitapAdi.setMaximumSize(QSize(222, 26))

        self.horizontalLayout.addWidget(self.leKitapAdi)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leYazar = QLineEdit(self.frmGiris)
        self.leYazar.setObjectName(u"leYazar")
        self.leYazar.setMinimumSize(QSize(0, 26))
        self.leYazar.setMaximumSize(QSize(222, 26))

        self.horizontalLayout_2.addWidget(self.leYazar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.leISBN = QLineEdit(self.frmGiris)
        self.leISBN.setObjectName(u"leISBN")
        self.leISBN.setMinimumSize(QSize(0, 26))
        self.leISBN.setMaximumSize(QSize(222, 26))

        self.horizontalLayout_4.addWidget(self.leISBN)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.leYayinEvi = QLineEdit(self.frmGiris)
        self.leYayinEvi.setObjectName(u"leYayinEvi")
        self.leYayinEvi.setMinimumSize(QSize(0, 26))
        self.leYayinEvi.setMaximumSize(QSize(222, 26))

        self.horizontalLayout_6.addWidget(self.leYayinEvi)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.leBasimYili = QLineEdit(self.frmGiris)
        self.leBasimYili.setObjectName(u"leBasimYili")
        self.leBasimYili.setMinimumSize(QSize(0, 26))
        self.leBasimYili.setMaximumSize(QSize(222, 26))

        self.horizontalLayout_7.addWidget(self.leBasimYili)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, -1, 2, -1)
        self.leSayfa = QLineEdit(self.frmGiris)
        self.leSayfa.setObjectName(u"leSayfa")
        self.leSayfa.setMinimumSize(QSize(0, 26))
        self.leSayfa.setMaximumSize(QSize(222, 26))

        self.horizontalLayout_3.addWidget(self.leSayfa)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(7, -1, 7, -1)
        self.lbRowCount = QLabel(self.frmGiris)
        self.lbRowCount.setObjectName(u"lbRowCount")
        self.lbRowCount.setMaximumSize(QSize(60, 26))
        font = QFont()
        font.setPointSize(7)
        self.lbRowCount.setFont(font)

        self.horizontalLayout_13.addWidget(self.lbRowCount)

        self.lbRowCount_2 = QLabel(self.frmGiris)
        self.lbRowCount_2.setObjectName(u"lbRowCount_2")
        self.lbRowCount_2.setMaximumSize(QSize(60, 26))
        self.lbRowCount_2.setFont(font)

        self.horizontalLayout_13.addWidget(self.lbRowCount_2)

        self.cboxRaf = QComboBox(self.frmGiris)
        self.cboxRaf.setObjectName(u"cboxRaf")
        self.cboxRaf.setMinimumSize(QSize(0, 26))
        self.cboxRaf.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_13.addWidget(self.cboxRaf)


        self.verticalLayout.addLayout(self.horizontalLayout_13)


        self.verticalLayout_8.addLayout(self.verticalLayout)


        self.horizontalLayout_11.addWidget(self.frmGiris)

        self.frmbutonbar = QVBoxLayout()
        self.frmbutonbar.setSpacing(1)
        self.frmbutonbar.setObjectName(u"frmbutonbar")
        self.frmbutonbar.setSizeConstraint(QLayout.SetFixedSize)
        self.btKaydet = QPushButton(self.widget)
        self.btKaydet.setObjectName(u"btKaydet")
        self.btKaydet.setMinimumSize(QSize(92, 0))
        self.btKaydet.setMaximumSize(QSize(92, 26))
        self.btKaydet.setStyleSheet(u"")

        self.frmbutonbar.addWidget(self.btKaydet)

        self.btGuncelle = QPushButton(self.widget)
        self.btGuncelle.setObjectName(u"btGuncelle")
        self.btGuncelle.setMinimumSize(QSize(92, 0))
        self.btGuncelle.setMaximumSize(QSize(92, 26))

        self.frmbutonbar.addWidget(self.btGuncelle)

        self.btAra = QPushButton(self.widget)
        self.btAra.setObjectName(u"btAra")
        self.btAra.setEnabled(True)
        self.btAra.setMinimumSize(QSize(92, 0))
        self.btAra.setMaximumSize(QSize(92, 26))

        self.frmbutonbar.addWidget(self.btAra)

        self.btISBN = QPushButton(self.widget)
        self.btISBN.setObjectName(u"btISBN")
        self.btISBN.setMinimumSize(QSize(92, 0))
        self.btISBN.setMaximumSize(QSize(92, 26))

        self.frmbutonbar.addWidget(self.btISBN)

        self.btBarcode = QPushButton(self.widget)
        self.btBarcode.setObjectName(u"btBarcode")
        self.btBarcode.setMinimumSize(QSize(92, 0))
        self.btBarcode.setMaximumSize(QSize(92, 26))
        self.btBarcode.setTabletTracking(True)
        self.btBarcode.setStyleSheet(u"")
        icon = QIcon()
        iconThemeName = u"zoom-in"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../kutuphane10", QSize(), QIcon.Normal, QIcon.Off)

        self.btBarcode.setIcon(icon)

        self.frmbutonbar.addWidget(self.btBarcode)

        self.btSil = QPushButton(self.widget)
        self.btSil.setObjectName(u"btSil")
        self.btSil.setMinimumSize(QSize(92, 0))
        self.btSil.setMaximumSize(QSize(92, 26))

        self.frmbutonbar.addWidget(self.btSil)

        self.btClear = QPushButton(self.widget)
        self.btClear.setObjectName(u"btClear")
        self.btClear.setMinimumSize(QSize(92, 0))
        self.btClear.setMaximumSize(QSize(92, 26))

        self.frmbutonbar.addWidget(self.btClear)

        self.btPaylas = QPushButton(self.widget)
        self.btPaylas.setObjectName(u"btPaylas")
        self.btPaylas.setMaximumSize(QSize(92, 26))

        self.frmbutonbar.addWidget(self.btPaylas)


        self.horizontalLayout_11.addLayout(self.frmbutonbar)

        self.frmNot = QFrame(self.widget)
        self.frmNot.setObjectName(u"frmNot")
        self.frmNot.setMaximumSize(QSize(270, 16777215))
        self.frmNot.setFrameShape(QFrame.StyledPanel)
        self.frmNot.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frmNot)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.teNot = QTextEdit(self.frmNot)
        self.teNot.setObjectName(u"teNot")
        self.teNot.setMinimumSize(QSize(0, 140))
        self.teNot.setMaximumSize(QSize(270, 170))
        self.teNot.setAutoFormatting(QTextEdit.AutoNone)

        self.verticalLayout_3.addWidget(self.teNot)

        self.teEtiket = QTextEdit(self.frmNot)
        self.teEtiket.setObjectName(u"teEtiket")
        self.teEtiket.setMaximumSize(QSize(270, 80))

        self.verticalLayout_3.addWidget(self.teEtiket)

        self.frmPaylas = QFrame(self.frmNot)
        self.frmPaylas.setObjectName(u"frmPaylas")
        self.frmPaylas.setFrameShape(QFrame.StyledPanel)
        self.frmPaylas.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frmPaylas)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(1, 0, 1, 6)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(1, 0, 1, 0)
        self.btEmail = QPushButton(self.frmPaylas)
        self.btEmail.setObjectName(u"btEmail")
        self.btEmail.setMinimumSize(QSize(92, 26))
        self.btEmail.setMaximumSize(QSize(70, 26))
        self.btEmail.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.btEmail)

        self.btWhatsap = QPushButton(self.frmPaylas)
        self.btWhatsap.setObjectName(u"btWhatsap")
        self.btWhatsap.setMinimumSize(QSize(92, 26))
        self.btWhatsap.setMaximumSize(QSize(70, 26))
        self.btWhatsap.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.btWhatsap)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_9)


        self.verticalLayout_3.addWidget(self.frmPaylas)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.horizontalLayout_11.addWidget(self.frmNot)

        self.frmResim = QFrame(self.widget)
        self.frmResim.setObjectName(u"frmResim")
        self.frmResim.setMinimumSize(QSize(155, 210))
        self.frmResim.setMaximumSize(QSize(150, 240))
        self.frmResim.setFrameShape(QFrame.StyledPanel)
        self.frmResim.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frmResim)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(1, 2, 1, 2)
        self.lbImg = QLabel(self.frmResim)
        self.lbImg.setObjectName(u"lbImg")
        self.lbImg.setMinimumSize(QSize(150, 210))
        self.lbImg.setMaximumSize(QSize(151, 210))
        self.lbImg.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.lbImg)

        self.frame = QFrame(self.frmResim)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 30))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 151, 20))
        self.horizontalLayout_17 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.cbekitap = QCheckBox(self.layoutWidget)
        self.cbekitap.setObjectName(u"cbekitap")
        self.cbekitap.setEnabled(True)
        self.cbekitap.setMaximumSize(QSize(16777215, 26))
        self.cbekitap.setChecked(False)

        self.horizontalLayout_17.addWidget(self.cbekitap)

        self.cbTr = QCheckBox(self.layoutWidget)
        self.cbTr.setObjectName(u"cbTr")
        self.cbTr.setMaximumSize(QSize(40, 26))

        self.horizontalLayout_17.addWidget(self.cbTr)

        self.cbOkundu = QCheckBox(self.layoutWidget)
        self.cbOkundu.setObjectName(u"cbOkundu")
        self.cbOkundu.setMinimumSize(QSize(50, 0))
        self.cbOkundu.setMaximumSize(QSize(40, 26))
        self.cbOkundu.setChecked(False)

        self.horizontalLayout_17.addWidget(self.cbOkundu)


        self.verticalLayout_7.addWidget(self.frame)


        self.horizontalLayout_11.addWidget(self.frmResim)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget1 = QWidget(self.tab_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 831, 701))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btTodoEkle = QPushButton(self.layoutWidget1)
        self.btTodoEkle.setObjectName(u"btTodoEkle")

        self.horizontalLayout_16.addWidget(self.btTodoEkle)

        self.btTodoEmailGonder = QPushButton(self.layoutWidget1)
        self.btTodoEmailGonder.setObjectName(u"btTodoEmailGonder")

        self.horizontalLayout_16.addWidget(self.btTodoEmailGonder)

        self.btTodoSil = QPushButton(self.layoutWidget1)
        self.btTodoSil.setObjectName(u"btTodoSil")

        self.horizontalLayout_16.addWidget(self.btTodoSil)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.leTodoSatir = QLineEdit(self.layoutWidget1)
        self.leTodoSatir.setObjectName(u"leTodoSatir")

        self.verticalLayout_4.addWidget(self.leTodoSatir)

        self.lvTodo = QTableWidget(self.layoutWidget1)
        self.lvTodo.setObjectName(u"lvTodo")
        self.lvTodo.setMinimumSize(QSize(700, 0))
        self.lvTodo.setMaximumSize(QSize(830, 16777215))

        self.verticalLayout_4.addWidget(self.lvTodo)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.frRafSetup = QFrame(self.tab_3)
        self.frRafSetup.setObjectName(u"frRafSetup")
        self.frRafSetup.setGeometry(QRect(250, 10, 221, 271))
        self.frRafSetup.setFrameShape(QFrame.StyledPanel)
        self.frRafSetup.setFrameShadow(QFrame.Raised)
        self.layoutWidget_4 = QWidget(self.frRafSetup)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(0, 0, 221, 266))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.leRafekle = QLineEdit(self.layoutWidget_4)
        self.leRafekle.setObjectName(u"leRafekle")

        self.horizontalLayout_12.addWidget(self.leRafekle)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btSecRafSil = QPushButton(self.layoutWidget_4)
        self.btSecRafSil.setObjectName(u"btSecRafSil")

        self.horizontalLayout_15.addWidget(self.btSecRafSil)

        self.btRafEkle = QPushButton(self.layoutWidget_4)
        self.btRafEkle.setObjectName(u"btRafEkle")

        self.horizontalLayout_15.addWidget(self.btRafEkle)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lvRafDuzenle = QListWidget(self.layoutWidget_4)
        self.lvRafDuzenle.setObjectName(u"lvRafDuzenle")

        self.horizontalLayout_14.addWidget(self.lvRafDuzenle)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.verticalLayoutWidget = QWidget(self.tab_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 208, 200))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btRafSetupAc = QPushButton(self.verticalLayoutWidget)
        self.btRafSetupAc.setObjectName(u"btRafSetupAc")

        self.verticalLayout_9.addWidget(self.btRafSetupAc)

        self.btVeritabaniYedekle = QPushButton(self.verticalLayoutWidget)
        self.btVeritabaniYedekle.setObjectName(u"btVeritabaniYedekle")

        self.verticalLayout_9.addWidget(self.btVeritabaniYedekle)

        self.btVeritabaniZiple = QPushButton(self.verticalLayoutWidget)
        self.btVeritabaniZiple.setObjectName(u"btVeritabaniZiple")

        self.verticalLayout_9.addWidget(self.btVeritabaniZiple)

        self.btExcel = QPushButton(self.verticalLayoutWidget)
        self.btExcel.setObjectName(u"btExcel")
        self.btExcel.setMinimumSize(QSize(92, 0))
        self.btExcel.setMaximumSize(QSize(220, 16777215))
        self.btExcel.setTabletTracking(True)
        self.btExcel.setStyleSheet(u"")
        self.btExcel.setIcon(icon)

        self.verticalLayout_9.addWidget(self.btExcel)

        self.btVeritabaniRestore = QPushButton(self.verticalLayoutWidget)
        self.btVeritabaniRestore.setObjectName(u"btVeritabaniRestore")

        self.verticalLayout_9.addWidget(self.btVeritabaniRestore)

        self.btSetupEmailAyar = QPushButton(self.verticalLayoutWidget)
        self.btSetupEmailAyar.setObjectName(u"btSetupEmailAyar")

        self.verticalLayout_9.addWidget(self.btSetupEmailAyar)

        self.frSetupEmailBilgi = QFrame(self.tab_3)
        self.frSetupEmailBilgi.setObjectName(u"frSetupEmailBilgi")
        self.frSetupEmailBilgi.setGeometry(QRect(250, 10, 231, 101))
        self.frSetupEmailBilgi.setFrameShape(QFrame.StyledPanel)
        self.frSetupEmailBilgi.setFrameShadow(QFrame.Raised)
        self.layoutWidget2 = QWidget(self.frSetupEmailBilgi)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 218, 96))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.leSetupEmailAdresi = QLineEdit(self.layoutWidget2)
        self.leSetupEmailAdresi.setObjectName(u"leSetupEmailAdresi")

        self.verticalLayout_12.addWidget(self.leSetupEmailAdresi)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.leSetupEmailPassword = QLineEdit(self.layoutWidget2)
        self.leSetupEmailPassword.setObjectName(u"leSetupEmailPassword")
        self.leSetupEmailPassword.setMaximumSize(QSize(16777215, 26))

        self.horizontalLayout_8.addWidget(self.leSetupEmailPassword)

        self.btEmailEncode = QPushButton(self.layoutWidget2)
        self.btEmailEncode.setObjectName(u"btEmailEncode")
        self.btEmailEncode.setMinimumSize(QSize(92, 0))
        self.btEmailEncode.setMaximumSize(QSize(70, 26))

        self.horizontalLayout_8.addWidget(self.btEmailEncode)


        self.verticalLayout_12.addLayout(self.horizontalLayout_8)

        self.btSetupEmailAyarSil = QPushButton(self.layoutWidget2)
        self.btSetupEmailAyarSil.setObjectName(u"btSetupEmailAyarSil")

        self.verticalLayout_12.addWidget(self.btSetupEmailAyarSil)

        self.layoutWidget3 = QWidget(self.tab_3)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 240, 208, 54))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget3)
        self.label.setObjectName(u"label")

        self.verticalLayout_10.addWidget(self.label)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.cbSiralama = QCheckBox(self.layoutWidget3)
        self.cbSiralama.setObjectName(u"cbSiralama")
        self.cbSiralama.setMaximumSize(QSize(65, 16777215))
        self.cbSiralama.setChecked(True)

        self.horizontalLayout_10.addWidget(self.cbSiralama)

        self.leGetSatir = QLineEdit(self.layoutWidget3)
        self.leGetSatir.setObjectName(u"leGetSatir")
        self.leGetSatir.setMaximumSize(QSize(50, 20))

        self.horizontalLayout_10.addWidget(self.leGetSatir)

        self.btSon = QPushButton(self.layoutWidget3)
        self.btSon.setObjectName(u"btSon")
        self.btSon.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_10.addWidget(self.btSon)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.widget1 = QWidget(self.tab_3)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 310, 211, 30))
        self.horizontalLayout_18 = QHBoxLayout(self.widget1)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.btOnCamSec = QPushButton(self.widget1)
        self.btOnCamSec.setObjectName(u"btOnCamSec")

        self.horizontalLayout_18.addWidget(self.btOnCamSec)

        self.btArkaCamSec = QPushButton(self.widget1)
        self.btArkaCamSec.setObjectName(u"btArkaCamSec")

        self.horizontalLayout_18.addWidget(self.btArkaCamSec)

        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_18.addWidget(self.label_2)

        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"K\u00fct\u00fcphane", None))
        self.leKitapAdi.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kitap Ad\u0131", None))
        self.leYazar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Yazar Ad\u0131", None))
        self.leISBN.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ISBN", None))
        self.leYayinEvi.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Yay\u0131n Evi", None))
        self.leBasimYili.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bas\u0131m Y\u0131l\u0131", None))
        self.leSayfa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sayfa", None))
        self.lbRowCount.setText(QCoreApplication.translate("MainWindow", u"Toplam Kitap Say\u0131s\u0131", None))
        self.lbRowCount_2.setText(QCoreApplication.translate("MainWindow", u"Tablo sat\u0131r say\u0131s\u0131", None))
        self.btKaydet.setText(QCoreApplication.translate("MainWindow", u"Kaydet", None))
        self.btGuncelle.setText(QCoreApplication.translate("MainWindow", u"G\u00fcncelle", None))
        self.btAra.setText(QCoreApplication.translate("MainWindow", u"Ara", None))
        self.btISBN.setText(QCoreApplication.translate("MainWindow", u"ISBN", None))
        self.btBarcode.setText(QCoreApplication.translate("MainWindow", u"Barcode", None))
        self.btSil.setText(QCoreApplication.translate("MainWindow", u"Sil", None))
        self.btClear.setText(QCoreApplication.translate("MainWindow", u"Temizle", None))
        self.btPaylas.setText(QCoreApplication.translate("MainWindow", u"Payla\u015f  >", None))
        self.teNot.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.teNot.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Not", None))
        self.teEtiket.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.teEtiket.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Etiketler : ", None))
#if QT_CONFIG(tooltip)
        self.btEmail.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Mail adresi istenecek </p><p>sonra da kitap ad\u0131, yazar ve ISBN</p><p>g\u00f6nderilecek</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btEmail.setText(QCoreApplication.translate("MainWindow", u"eMail", None))
#if QT_CONFIG(tooltip)
        self.btWhatsap.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Telefon numaras\u0131 istenecek </p><p>53xxxxxxxx ba\u015f\u0131nda s\u0131f\u0131r olmadan girin</p><p>sonra da kitap ad\u0131, yazar ve ISBN</p><p>g\u00f6nderilecek</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btWhatsap.setText(QCoreApplication.translate("MainWindow", u"Whatsap", None))
        self.lbImg.setText("")
        self.cbekitap.setText(QCoreApplication.translate("MainWindow", u"E-Kitap", None))
        self.cbTr.setText(QCoreApplication.translate("MainWindow", u"tr", None))
        self.cbOkundu.setText(QCoreApplication.translate("MainWindow", u"Oku", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Giri\u015f", None))
        self.btTodoEkle.setText(QCoreApplication.translate("MainWindow", u"Sat\u0131r Ekle", None))
        self.btTodoEmailGonder.setText(QCoreApplication.translate("MainWindow", u"Se\u00e7ilen sat\u0131r\u0131 eMail at", None))
        self.btTodoSil.setText(QCoreApplication.translate("MainWindow", u"Se\u00e7ilen Sat\u0131r\u0131 Sil", None))
        self.leTodoSatir.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Al\u0131nmas\u0131 planlanan Kitaplar, ilgilenilecek ve ara\u015ft\u0131r\u0131lacak yeni konular ", None))
#if QT_CONFIG(tooltip)
        self.lvTodo.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Sat\u0131r\u0131 se\u00e7ip sil butonu ile silebilirsiniz </p><p>sat\u0131rdaki h\u00fccreleri i\u00e7ine girip de\u011fi\u015ftirebilirsiniz </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Planlama", None))
        self.leRafekle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Raf Ekle", None))
        self.btSecRafSil.setText(QCoreApplication.translate("MainWindow", u"Se\u00e7ili Sat\u0131r\u0131 Sil", None))
        self.btRafEkle.setText(QCoreApplication.translate("MainWindow", u"Raf Ekle", None))
        self.btRafSetupAc.setText(QCoreApplication.translate("MainWindow", u"Raf Sistemi D\u00fczenle   >", None))
        self.btVeritabaniYedekle.setText(QCoreApplication.translate("MainWindow", u"Database Backup", None))
        self.btVeritabaniZiple.setText(QCoreApplication.translate("MainWindow", u"Database Ziple", None))
        self.btExcel.setText(QCoreApplication.translate("MainWindow", u"Database to XLS", None))
        self.btVeritabaniRestore.setText(QCoreApplication.translate("MainWindow", u"Database Restore", None))
        self.btSetupEmailAyar.setText(QCoreApplication.translate("MainWindow", u"Email Ayarlar\u0131     >", None))
        self.leSetupEmailAdresi.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email adresini girin", None))
        self.leSetupEmailPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password\u00fc girin", None))
#if QT_CONFIG(tooltip)
        self.btEmailEncode.setToolTip(QCoreApplication.translate("MainWindow", u"Paword\u00fc kaydet dedi\u011finiz anda girdi\u011finiz password encode edilip \u00f6yle kaydedilecek", None))
#endif // QT_CONFIG(tooltip)
        self.btEmailEncode.setText(QCoreApplication.translate("MainWindow", u"Kaydet", None))
        self.btSetupEmailAyarSil.setText(QCoreApplication.translate("MainWindow", u"Email ayarlar\u0131n\u0131 sil", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID ye g\u00f6re s\u0131ralama", None))
        self.cbSiralama.setText(QCoreApplication.translate("MainWindow", u"ba\u015f/son", None))
        self.leGetSatir.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.btSon.setText(QCoreApplication.translate("MainWindow", u"sat\u0131r ", None))
        self.btOnCamSec.setText(QCoreApplication.translate("MainWindow", u"\u00d6n Cam", None))
        self.btArkaCamSec.setText(QCoreApplication.translate("MainWindow", u"Arka Cam ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Setup", None))
    # retranslateUi

