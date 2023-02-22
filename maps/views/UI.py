# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'newdiproject.ui'
##
# Created by: Qt User Interface Compiler version 6.4.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import folium
import io
import os
import csv
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt,QStringListModel
from PySide6.QtWidgets import QLineEdit,QCompleter,QComboBox,QGridLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QPushButton, QSizePolicy, QTextEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QMouseEvent,QStandardItemModel,QStandardItem,QTextCursor, QTextDocument, QTextCharFormat
from service.API_maps import find_address
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from component.map import create_map


class Ui_Form(object):

    searches = []
    con = QSqlDatabase.addDatabase("QSQLITE")
    
    
    def setupUi(self, Form):
        self.data=[]
        self.load_csv()
        
        #!Creacion de Base de Datos y Tabla
        self.con.setDatabaseName(os.path.join(os.path.dirname(__file__), "mapsDB.sqlite"))
        self.con.open()
        QSqlQuery("create table if not exists history (name varchar(248))", self.con)
        
        
        #!Interfaz
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1029, 738)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 9, 431, 181))
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
        self.model=QStringListModel()
        self.model.setStringList(self.data)
        self.lineEdit_3 = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy = QSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setLayoutDirection(Qt.LeftToRight)
        #Configurar el autocompletado
        completer = QCompleter(self.model, self.lineEdit_3)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        completer.activated.connect(self.insert_completion)
        self.lineEdit_3.setCompleter(completer)
        self.gridLayout_4.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)

        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)

        self.textEdit = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_4.addWidget(self.textEdit, 2, 1, 1, 1)

        self.textEdit_2 = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_4.addWidget(self.textEdit_2, 3, 1, 1, 1)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        
        
        self.comboboxname = QComboBox(self.horizontalLayoutWidget)
        self.comboboxname.addItems(["Badalona", "Barcelona" ,"L'Hospitalet de Llobregat","Sabadell", "Castelldefels"])
        self.comboboxname.setObjectName(u"comboboxname")
        sizePolicy.setHeightForWidth(
            self.comboboxname.sizePolicy().hasHeightForWidth())
        self.comboboxname.setSizePolicy(sizePolicy)
        self.comboboxname.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_4.addWidget(self.comboboxname, 0, 1, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        # Accion de Localizar
        self.pushButton_3.clicked.connect(self.buscar_direcion)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        # Accion de Formatear Formulario
        self.pushButton_4.clicked.connect(self.format_form)


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
        sizePolicy1.setHeightForWidth(
            self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_5.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.listView = QListWidget(self.layoutWidget)
        self.listView.setObjectName(u"listWidget")
        
        # Limpiar Tabla al Inicio
        self.llenar_tabla()

        self.gridLayout_5.addWidget(self.listView, 0, 0, 1, 2)


        # Buscar en base al historial
        self.pushButton_2.clicked.connect(self.look_based_on_historial)

        # Eliminar historial
        self.pushButton_5.clicked.connect(self.borrar_historial)
        

        layout = QVBoxLayout()
        self.setLayout(layout)

        m = folium.Map(
            zoom_start=1,
        )

        # Guardamos los datos del mapa en un objeto
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        self.verticalLayout_3.addWidget(webView, 0)
        
        self.retranslateUi(Form)
        #Conectamos los botones con las funciones
        QMetaObject.connectSlotsByName(Form)
        
    

    def buscar_direcion(self):
        city = self.comboboxname.currentText()
        street = self.lineEdit_3.text()
        number = self.textEdit.toPlainText()
        floor = self.textEdit_2.toPlainText()
        addres = f"{city} {street} {number} {floor}".lower()

        layout = QVBoxLayout()
        self.setLayout(layout)

        m = create_map(find_address(addres))
        # Guardamos los datos del mapa en un objeto
        
        data = io.BytesIO()
        m.save(data, close_file=False)

        ubicate = QWebEngineView()
        ubicate.setHtml(data.getvalue().decode())
        self.verticalLayout_3.replaceWidget(
            self.verticalLayout_3.itemAt(1).widget(), ubicate)

        # Add to the searches list
        QSqlQuery(f"INSERT INTO history VALUES ('{addres}')")
        self.llenar_tabla()


    def llenar_tabla(self):
        
        self.listView.clear()
        query = QSqlQuery("SELECT * FROM history", self.con)
        while query.next():
            self.listView.addItem(query.value(0))

    def look_based_on_historial(self):
        item = self.listView.currentItem().text()

        m = create_map(find_address(item))
        # Guardamos los datos del mapa en un objeto
        data = io.BytesIO()
        m.save(data, close_file=False)

        ubicate = QWebEngineView()
        ubicate.setHtml(data.getvalue().decode())
        self.verticalLayout_3.replaceWidget(
            self.verticalLayout_3.itemAt(1).widget(), ubicate)
        # Añadimos el item a la lista de busquedas
        self.searches = list(filter(lambda x: x != item, self.searches))
        self.searches.insert(0, item)

        self.llenar_tabla()

    def borrar_historial(self):
        self.listView.clear()
        QSqlQuery("DELETE FROM history", self.con)

    def format_form(self):
        self.comboboxname.setCurrentIndex(0)
        self.lineEdit_3.setText("")
        self.textEdit.setText("")
        self.textEdit_2.setText("")

    def load_csv(self):
        pathdata=os.path.join(os.path.dirname(__file__),'data.csv')
        with open(pathdata,encoding='utf-8')as archivo:
            #intentaremos evitar el error unicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 0: character maps to <undefined>
            datos=csv.DictReader(archivo,delimiter=';')
            for row in datos:
            #guardamos los valores de TIPUSVIA,NEXEVIA y NOMVIA en una lista
                self.data.append( row['TIPUSVIA']+' '+row['NEXEVIA']+' '+row['NOMVIA'])
    
    def insert_completion(self, completion):
        # Obtener el cursor actual y el documento de texto
        cursor = self.lineEdit_3.cursorPosition()
        document=self.lineEdit_3.text()
        # Obtener la posición del cursor y retroceder para encontrar el inicio de la palabra actual
        cursor.movePosition(QTextCursor.StartOfWord, QTextCursor.MoveAnchor)
        start_pos = cursor.position()
        # Reemplazar la palabra actual con la selección del autocompletado
        cursor.setPosition(start_pos, QTextCursor.KeepAnchor)
        cursor.insertText(completion)
        # Resaltar la palabra completada
        cursor.movePosition(QTextCursor.EndOfWord, QTextCursor.KeepAnchor)
        char_format = QTextCharFormat()
        char_format.setBackground(Qt.yellow)
        cursor.setCharFormat(char_format)
        
                
        
   


    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate(
            "Form", u"RUTAS PARA TRABAJO Y RUTAS ANTERIORES", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Piso", None))
        self.label_3.setText(
            QCoreApplication.translate("Form", u"Calle", None))
        self.label_4.setText(
            QCoreApplication.translate("Form", u"Numero", None))
        self.label_6.setText(
            QCoreApplication.translate("Form", u"Ciudad", None))
        '''self.comboboxname.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None))'''
        self.pushButton_3.setText(
            QCoreApplication.translate("Form", u"Localizar", None))
        self.pushButton_4.setText(
            QCoreApplication.translate("Form", u"Formatear", None))
        self.pushButton_2.setText(QCoreApplication.translate(
            "Form", u"Buscar", None))
        self.pushButton_5.setText(
            QCoreApplication.translate("Form", u"Eliminar todo", None))
    # retranslateUi
