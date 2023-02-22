# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QListView, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1029, 738)
        Form.setMinimumSize(QSize(1029, 738))
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 9, 431, 444))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)

        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)

        self.textEdit_3 = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        self.textEdit_3.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_4.addWidget(self.textEdit_3, 1, 1, 1, 1)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_4.addWidget(self.textEdit_2, 3, 1, 1, 1)

        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.textEdit = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_4.addWidget(self.textEdit, 2, 1, 1, 1)

        self.comboBox = QComboBox(self.horizontalLayoutWidget)
        self.comboBox.addItems(["Badalona", "Barcelona" ,"L'Hospitalet de Llobregat","Sabadell", "Castelldefels"])
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_4.addWidget(self.comboBox, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 200, 431, 531))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.verticalLayoutWidget_2)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_3.addWidget(self.widget)

        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(450, 10, 571, 721))
        self.gridLayout_5 = QGridLayout(self.layoutWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_5.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.listView = QListView(self.layoutWidget)
        self.listView.setObjectName(u"listView")

        self.gridLayout_5.addWidget(self.listView, 0, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"RUTAS PARA TRABAJO Y RUTAS ANTERIORES", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Piso", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Calle", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Numero", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Ciudad", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Enviar", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Eliminar seleccion", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Eliminar todo", None))
    # retranslateUi

