# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(856, 1016)
        self.but_start = QPushButton(Form)
        self.but_start.setObjectName(u"but_start")
        self.but_start.setGeometry(QRect(600, 960, 240, 41))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(730, 50, 110, 61))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pbut_listAndMainBean_add = QPushButton(self.layoutWidget)
        self.pbut_listAndMainBean_add.setObjectName(u"pbut_listAndMainBean_add")

        self.horizontalLayout_2.addWidget(self.pbut_listAndMainBean_add)

        self.pbut_listAndMainBean_remove = QPushButton(self.layoutWidget)
        self.pbut_listAndMainBean_remove.setObjectName(u"pbut_listAndMainBean_remove")

        self.horizontalLayout_2.addWidget(self.pbut_listAndMainBean_remove)

        self.layoutWidget_4 = QWidget(Form)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(60, 290, 150, 180))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.cb_picture = QCheckBox(self.layoutWidget_4)
        self.cb_picture.setObjectName(u"cb_picture")

        self.verticalLayout.addWidget(self.cb_picture)

        self.cb_examine = QCheckBox(self.layoutWidget_4)
        self.cb_examine.setObjectName(u"cb_examine")

        self.verticalLayout.addWidget(self.cb_examine)

        self.cb_annotation = QCheckBox(self.layoutWidget_4)
        self.cb_annotation.setObjectName(u"cb_annotation")

        self.verticalLayout.addWidget(self.cb_annotation)

        self.tw_listAndMainBean = QTableWidget(Form)
        if (self.tw_listAndMainBean.columnCount() < 5):
            self.tw_listAndMainBean.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_listAndMainBean.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_listAndMainBean.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_listAndMainBean.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_listAndMainBean.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_listAndMainBean.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tw_listAndMainBean.setObjectName(u"tw_listAndMainBean")
        self.tw_listAndMainBean.setGeometry(QRect(260, 100, 580, 381))
        self.tw_listLineName = QTableWidget(Form)
        if (self.tw_listLineName.columnCount() < 2):
            self.tw_listLineName.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_listLineName.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_listLineName.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        if (self.tw_listLineName.rowCount() < 2):
            self.tw_listLineName.setRowCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_listLineName.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_listLineName.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tw_listLineName.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tw_listLineName.setItem(1, 1, __qtablewidgetitem10)
        self.tw_listLineName.setObjectName(u"tw_listLineName")
        self.tw_listLineName.setGeometry(QRect(10, 100, 241, 181))
        self.tw_listLineName.setSortingEnabled(True)
        self.layoutWidget_3 = QWidget(Form)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(140, 50, 110, 61))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pbut_listLineName_add = QPushButton(self.layoutWidget_3)
        self.pbut_listLineName_add.setObjectName(u"pbut_listLineName_add")
        self.pbut_listLineName_add.setEnabled(True)
        self.pbut_listLineName_add.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.pbut_listLineName_add)

        self.pbut_listLineName_remove = QPushButton(self.layoutWidget_3)
        self.pbut_listLineName_remove.setObjectName(u"pbut_listLineName_remove")
        self.pbut_listLineName_remove.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.pbut_listLineName_remove)

        self.tw_entryBean = QTableWidget(Form)
        if (self.tw_entryBean.columnCount() < 4):
            self.tw_entryBean.setColumnCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tw_entryBean.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tw_entryBean.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tw_entryBean.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tw_entryBean.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        self.tw_entryBean.setObjectName(u"tw_entryBean")
        self.tw_entryBean.setGeometry(QRect(260, 520, 580, 380))
        self.layoutWidget_2 = QWidget(Form)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(720, 470, 120, 61))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.but_entryBean_add = QPushButton(self.layoutWidget_2)
        self.but_entryBean_add.setObjectName(u"but_entryBean_add")

        self.horizontalLayout_4.addWidget(self.but_entryBean_add)

        self.but_entryBean_remove = QPushButton(self.layoutWidget_2)
        self.but_entryBean_remove.setObjectName(u"but_entryBean_remove")

        self.horizontalLayout_4.addWidget(self.but_entryBean_remove)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 70, 120, 20))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 490, 120, 20))
        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 300, 23))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.edit_className = QLineEdit(self.layoutWidget1)
        self.edit_className.setObjectName(u"edit_className")

        self.horizontalLayout.addWidget(self.edit_className)

        self.layoutWidget2 = QWidget(Form)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(259, 920, 581, 25))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.edit_outPath = QLineEdit(self.layoutWidget2)
        self.edit_outPath.setObjectName(u"edit_outPath")
        self.edit_outPath.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.edit_outPath)

        self.but_selectOutPath = QPushButton(self.layoutWidget2)
        self.but_selectOutPath.setObjectName(u"but_selectOutPath")

        self.horizontalLayout_3.addWidget(self.but_selectOutPath)

        self.plainT_output = QPlainTextEdit(Form)
        self.plainT_output.setObjectName(u"plainT_output")
        self.plainT_output.setGeometry(QRect(10, 520, 240, 480))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 490, 80, 20))
        self.but_resetAll = QPushButton(Form)
        self.but_resetAll.setObjectName(u"but_resetAll")
        self.but_resetAll.setGeometry(QRect(489, 960, 101, 41))
        self.layoutWidget_5 = QWidget(Form)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(330, 20, 300, 23))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.edit_className_2 = QLineEdit(self.layoutWidget_5)
        self.edit_className_2.setObjectName(u"edit_className_2")

        self.horizontalLayout_6.addWidget(self.edit_className_2)

        QWidget.setTabOrder(self.edit_className, self.edit_className_2)
        QWidget.setTabOrder(self.edit_className_2, self.pbut_listAndMainBean_add)
        QWidget.setTabOrder(self.pbut_listAndMainBean_add, self.pbut_listAndMainBean_remove)
        QWidget.setTabOrder(self.pbut_listAndMainBean_remove, self.tw_listAndMainBean)
        QWidget.setTabOrder(self.tw_listAndMainBean, self.but_entryBean_add)
        QWidget.setTabOrder(self.but_entryBean_add, self.but_entryBean_remove)
        QWidget.setTabOrder(self.but_entryBean_remove, self.tw_entryBean)
        QWidget.setTabOrder(self.tw_entryBean, self.cb_picture)
        QWidget.setTabOrder(self.cb_picture, self.cb_examine)
        QWidget.setTabOrder(self.cb_examine, self.cb_annotation)
        QWidget.setTabOrder(self.cb_annotation, self.but_selectOutPath)
        QWidget.setTabOrder(self.but_selectOutPath, self.edit_outPath)
        QWidget.setTabOrder(self.edit_outPath, self.but_start)
        QWidget.setTabOrder(self.but_start, self.but_resetAll)
        QWidget.setTabOrder(self.but_resetAll, self.pbut_listLineName_add)
        QWidget.setTabOrder(self.pbut_listLineName_add, self.pbut_listLineName_remove)
        QWidget.setTabOrder(self.pbut_listLineName_remove, self.tw_listLineName)
        QWidget.setTabOrder(self.tw_listLineName, self.plainT_output)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u751f\u6210\u5de5\u5177", None))
        self.but_start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u751f\u6210", None))
        self.pbut_listAndMainBean_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.pbut_listAndMainBean_remove.setText(QCoreApplication.translate("Form", u"-", None))
        self.cb_picture.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u9644\u4ef6", None))
        self.cb_examine.setText(QCoreApplication.translate("Form", u"\u5ba1\u6838", None))
        self.cb_annotation.setText(QCoreApplication.translate("Form", u"\u6ce8\u91ca", None))
        ___qtablewidgetitem = self.tw_listAndMainBean.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.tw_listAndMainBean.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u53d8\u91cf\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tw_listAndMainBean.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u7c7b\u578b", None));
        ___qtablewidgetitem3 = self.tw_listAndMainBean.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u5217\u8868\u4f4d\u7f6e\u5e8f\u53f7", None));
        ___qtablewidgetitem4 = self.tw_listAndMainBean.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u8be6\u60c5\u4f4d\u7f6e\u5e8f\u53f7", None));
        ___qtablewidgetitem5 = self.tw_listLineName.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u5217\u663e\u793a\u540d\u79f0", None));
        ___qtablewidgetitem6 = self.tw_listLineName.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"\u5217Fragment\u4e2d\u7f00", None));

        __sortingEnabled = self.tw_listLineName.isSortingEnabled()
        self.tw_listLineName.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tw_listLineName.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u5f85\u63d0\u4ea4", None));
        ___qtablewidgetitem8 = self.tw_listLineName.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Approval", None));
        ___qtablewidgetitem9 = self.tw_listLineName.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"\u5df2\u5904\u7406", None));
        ___qtablewidgetitem10 = self.tw_listLineName.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Processed", None));
        self.tw_listLineName.setSortingEnabled(__sortingEnabled)

        self.pbut_listLineName_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.pbut_listLineName_remove.setText(QCoreApplication.translate("Form", u"-", None))
        ___qtablewidgetitem11 = self.tw_entryBean.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u540d\u79f0", None));
        ___qtablewidgetitem12 = self.tw_entryBean.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"\u53d8\u91cf\u540d\u79f0", None));
        ___qtablewidgetitem13 = self.tw_entryBean.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u7c7b\u578b", None));
        ___qtablewidgetitem14 = self.tw_entryBean.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u4f4d\u7f6e\u5e8f\u53f7", None));
        self.but_entryBean_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.but_entryBean_remove.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8be6\u60c5\u6570\u636e", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5206\u5f55\u6570\u636e", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7c7b\u540d\u524d\u7f00\uff1a", None))
        self.edit_className.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u7c7b\u540d\u524d\u7f00\uff0c\u4f8b\uff1aMettePurRequestBill", None))
        self.but_selectOutPath.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u8f93\u51fa\u8def\u5f84", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u65e5\u5fd7\u8f93\u51fa", None))
        self.but_resetAll.setText(QCoreApplication.translate("Form", u"\u6e05\u7406", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5355\u636e\u540d\u79f0\uff1a", None))
        self.edit_className_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5355\u636e\u540d\u79f0\uff0c\u4f8b\uff1a\u62db\u5f85\u8d39\u7533\u8bf7\u5355", None))
    # retranslateUi

