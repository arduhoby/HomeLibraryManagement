# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'anasayfaJWnuVX.ui'
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
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(829, 727)
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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.ust = QHBoxLayout()
        self.ust.setObjectName(u"ust")
        self.frmGiris = QFrame(self.centralwidget)
        self.frmGiris.setObjectName(u"frmGiris")
        self.frmGiris.setFrameShape(QFrame.StyledPanel)
        self.frmGiris.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frmGiris)
        self.verticalLayout_8.setSpacing(12)
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

        self.horizontalLayout.addWidget(self.leKitapAdi)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leYazar = QLineEdit(self.frmGiris)
        self.leYazar.setObjectName(u"leYazar")
        self.leYazar.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_2.addWidget(self.leYazar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.leISBN = QLineEdit(self.frmGiris)
        self.leISBN.setObjectName(u"leISBN")
        self.leISBN.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_4.addWidget(self.leISBN)

        self.btISBN = QPushButton(self.frmGiris)
        self.btISBN.setObjectName(u"btISBN")
        self.btISBN.setMinimumSize(QSize(92, 0))
        self.btISBN.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_4.addWidget(self.btISBN)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.leYayinEvi = QLineEdit(self.frmGiris)
        self.leYayinEvi.setObjectName(u"leYayinEvi")
        self.leYayinEvi.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_6.addWidget(self.leYayinEvi)

        self.btBarcode = QPushButton(self.frmGiris)
        self.btBarcode.setObjectName(u"btBarcode")
        self.btBarcode.setMinimumSize(QSize(92, 0))
        self.btBarcode.setMaximumSize(QSize(70, 16777215))
        self.btBarcode.setTabletTracking(True)
        self.btBarcode.setStyleSheet(u"")
        icon = QIcon()
        iconThemeName = u"zoom-in"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../kutuphane10", QSize(), QIcon.Normal, QIcon.Off)

        self.btBarcode.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.btBarcode)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.leBasimYili = QLineEdit(self.frmGiris)
        self.leBasimYili.setObjectName(u"leBasimYili")
        self.leBasimYili.setMinimumSize(QSize(0, 26))
        self.leBasimYili.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_7.addWidget(self.leBasimYili)

        self.cboxRaf = QComboBox(self.frmGiris)
        self.cboxRaf.setObjectName(u"cboxRaf")

        self.horizontalLayout_7.addWidget(self.cboxRaf)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, -1, 2, -1)
        self.leSayfa = QLineEdit(self.frmGiris)
        self.leSayfa.setObjectName(u"leSayfa")
        self.leSayfa.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_3.addWidget(self.leSayfa)

        self.cbTr = QCheckBox(self.frmGiris)
        self.cbTr.setObjectName(u"cbTr")

        self.horizontalLayout_3.addWidget(self.cbTr)

        self.cbOkundu = QCheckBox(self.frmGiris)
        self.cbOkundu.setObjectName(u"cbOkundu")
        self.cbOkundu.setChecked(False)

        self.horizontalLayout_3.addWidget(self.cbOkundu)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_8.addLayout(self.verticalLayout)


        self.ust.addWidget(self.frmGiris)

        self.butonbar = QVBoxLayout()
        self.butonbar.setSpacing(12)
        self.butonbar.setObjectName(u"butonbar")
        self.btKaydet = QPushButton(self.centralwidget)
        self.btKaydet.setObjectName(u"btKaydet")
        self.btKaydet.setMinimumSize(QSize(92, 0))
        self.btKaydet.setMaximumSize(QSize(60, 16777215))
        self.btKaydet.setStyleSheet(u"")

        self.butonbar.addWidget(self.btKaydet)

        self.btGuncelle = QPushButton(self.centralwidget)
        self.btGuncelle.setObjectName(u"btGuncelle")
        self.btGuncelle.setMinimumSize(QSize(92, 0))
        self.btGuncelle.setMaximumSize(QSize(70, 16777215))

        self.butonbar.addWidget(self.btGuncelle)

        self.btAra = QPushButton(self.centralwidget)
        self.btAra.setObjectName(u"btAra")
        self.btAra.setEnabled(True)
        self.btAra.setMinimumSize(QSize(92, 0))
        self.btAra.setMaximumSize(QSize(70, 16777215))

        self.butonbar.addWidget(self.btAra)

        self.btSil = QPushButton(self.centralwidget)
        self.btSil.setObjectName(u"btSil")
        self.btSil.setMinimumSize(QSize(92, 0))
        self.btSil.setMaximumSize(QSize(70, 16777215))

        self.butonbar.addWidget(self.btSil)

        self.btClear = QPushButton(self.centralwidget)
        self.btClear.setObjectName(u"btClear")
        self.btClear.setMinimumSize(QSize(92, 0))
        self.btClear.setMaximumSize(QSize(70, 16777215))

        self.butonbar.addWidget(self.btClear)

        self.btPaylas = QPushButton(self.centralwidget)
        self.btPaylas.setObjectName(u"btPaylas")

        self.butonbar.addWidget(self.btPaylas)


        self.ust.addLayout(self.butonbar)

        self.notvepaylas = QVBoxLayout()
        self.notvepaylas.setSpacing(2)
        self.notvepaylas.setObjectName(u"notvepaylas")
        self.notvepaylas.setContentsMargins(-1, -1, -1, 5)
        self.frmNot = QFrame(self.centralwidget)
        self.frmNot.setObjectName(u"frmNot")
        self.frmNot.setMaximumSize(QSize(16777215, 16777215))
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
        self.teNot.setAutoFormatting(QTextEdit.AutoNone)

        self.verticalLayout_3.addWidget(self.teNot)

        self.teEtiket = QTextEdit(self.frmNot)
        self.teEtiket.setObjectName(u"teEtiket")
        self.teEtiket.setMaximumSize(QSize(16777215, 75))

        self.verticalLayout_3.addWidget(self.teEtiket)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.notvepaylas.addWidget(self.frmNot)

        self.frmPaylas = QFrame(self.centralwidget)
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
        self.btEmail.setMinimumSize(QSize(92, 0))
        self.btEmail.setMaximumSize(QSize(70, 16777215))
        self.btEmail.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.btEmail)

        self.btWhatsap = QPushButton(self.frmPaylas)
        self.btWhatsap.setObjectName(u"btWhatsap")
        self.btWhatsap.setMinimumSize(QSize(92, 0))
        self.btWhatsap.setMaximumSize(QSize(70, 16777215))
        self.btWhatsap.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.btWhatsap)

        self.btExcel = QPushButton(self.frmPaylas)
        self.btExcel.setObjectName(u"btExcel")
        self.btExcel.setMinimumSize(QSize(92, 0))
        self.btExcel.setMaximumSize(QSize(70, 16777215))
        self.btExcel.setTabletTracking(True)
        self.btExcel.setStyleSheet(u"")
        self.btExcel.setIcon(icon)

        self.horizontalLayout_9.addWidget(self.btExcel)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_9)


        self.notvepaylas.addWidget(self.frmPaylas)


        self.ust.addLayout(self.notvepaylas)

        self.frmResim = QFrame(self.centralwidget)
        self.frmResim.setObjectName(u"frmResim")
        self.frmResim.setMinimumSize(QSize(155, 210))
        self.frmResim.setFrameShape(QFrame.StyledPanel)
        self.frmResim.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frmResim)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(1, 2, 1, 25)
        self.lbImg = QLabel(self.frmResim)
        self.lbImg.setObjectName(u"lbImg")
        self.lbImg.setMinimumSize(QSize(151, 226))
        self.lbImg.setMaximumSize(QSize(151, 226))
        self.lbImg.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.lbImg)


        self.ust.addWidget(self.frmResim)


        self.gridLayout.addLayout(self.ust, 1, 1, 1, 2)

        self.frmTable = QFrame(self.centralwidget)
        self.frmTable.setObjectName(u"frmTable")
        self.frmTable.setMinimumSize(QSize(800, 400))
        self.frmTable.setFrameShape(QFrame.StyledPanel)
        self.frmTable.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frmTable)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 5, 6, 4)
        self.tblKitap = QTableWidget(self.frmTable)
        self.tblKitap.setObjectName(u"tblKitap")
        self.tblKitap.horizontalHeader().setCascadingSectionResizes(False)
        self.tblKitap.horizontalHeader().setMinimumSectionSize(40)
        self.tblKitap.verticalHeader().setMinimumSectionSize(30)

        self.verticalLayout_6.addWidget(self.tblKitap)


        self.gridLayout.addWidget(self.frmTable, 2, 1, 1, 2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbRowCount = QLabel(self.centralwidget)
        self.lbRowCount.setObjectName(u"lbRowCount")

        self.horizontalLayout_8.addWidget(self.lbRowCount)

        self.lbRowCount_2 = QLabel(self.centralwidget)
        self.lbRowCount_2.setObjectName(u"lbRowCount_2")

        self.horizontalLayout_8.addWidget(self.lbRowCount_2)

        self.cbekitap = QCheckBox(self.centralwidget)
        self.cbekitap.setObjectName(u"cbekitap")
        self.cbekitap.setEnabled(True)
        self.cbekitap.setChecked(False)

        self.horizontalLayout_8.addWidget(self.cbekitap)


        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.cbSiralama = QCheckBox(self.centralwidget)
        self.cbSiralama.setObjectName(u"cbSiralama")
        self.cbSiralama.setMaximumSize(QSize(65, 16777215))
        self.cbSiralama.setChecked(True)

        self.horizontalLayout_10.addWidget(self.cbSiralama)

        self.leGetSatir = QLineEdit(self.centralwidget)
        self.leGetSatir.setObjectName(u"leGetSatir")
        self.leGetSatir.setMaximumSize(QSize(50, 20))

        self.horizontalLayout_10.addWidget(self.leGetSatir)

        self.btSon = QPushButton(self.centralwidget)
        self.btSon.setObjectName(u"btSon")
        self.btSon.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_10.addWidget(self.btSon)


        self.gridLayout.addLayout(self.horizontalLayout_10, 3, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"K\u00fct\u00fcphane", None))
        self.leKitapAdi.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kitap Ad\u0131", None))
        self.leYazar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Yazar Ad\u0131", None))
        self.leISBN.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ISBN", None))
        self.btISBN.setText(QCoreApplication.translate("MainWindow", u"ISBN", None))
        self.leYayinEvi.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Yay\u0131n Evi", None))
        self.btBarcode.setText(QCoreApplication.translate("MainWindow", u"Barcode", None))
        self.leBasimYili.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bas\u0131m Y\u0131l\u0131", None))
        self.leSayfa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sayfa", None))
        self.cbTr.setText(QCoreApplication.translate("MainWindow", u"tr", None))
        self.cbOkundu.setText(QCoreApplication.translate("MainWindow", u"Okundu", None))
        self.btKaydet.setText(QCoreApplication.translate("MainWindow", u"Kaydet", None))
        self.btGuncelle.setText(QCoreApplication.translate("MainWindow", u"G\u00fcncelle", None))
        self.btAra.setText(QCoreApplication.translate("MainWindow", u"Ara", None))
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
        self.btExcel.setText(QCoreApplication.translate("MainWindow", u"XLS", None))
        self.lbImg.setText("")
        self.lbRowCount.setText(QCoreApplication.translate("MainWindow", u"Toplam Kitap Say\u0131s\u0131", None))
        self.lbRowCount_2.setText(QCoreApplication.translate("MainWindow", u"Tablo sat\u0131r say\u0131s\u0131", None))
        self.cbekitap.setText(QCoreApplication.translate("MainWindow", u"E-Kitap", None))
        self.cbSiralama.setText(QCoreApplication.translate("MainWindow", u"ba\u015f/son", None))
        self.leGetSatir.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.btSon.setText(QCoreApplication.translate("MainWindow", u"sat\u0131r ", None))
    # retranslateUi

