from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt,QStringListModel
from PySide6.QtWidgets import QMainWindow,QApplication,QCompleter,QComboBox,QGridLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QPushButton, QSizePolicy, QTextEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QMouseEvent,QStandardItemModel,QStandardItem,QTextCursor, QTextDocument, QTextCharFormat


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Lista de palabras para autocompletar
        self.words = ['auto', 'bicicleta', 'camión', 'moto', 'triciclo', 'van']

        # Crear modelo para el autocompletado
        self.model = QStringListModel()
        self.model.setStringList(self.words)

        # Crear QTextEdit para la entrada de texto
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(50, 50, 200, 200)

        # Configurar el autocompletado
        completer = QCompleter(self.model, self.text_edit)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        completer.activated.connect(self.insert_completion)
        self.text_edit.setCompleter(completer)

        # Agregar QTextEdit a la ventana principal
        self.setCentralWidget(self.text_edit)

    def insert_completion(self, completion):
        # Obtener el cursor actual y el documento de texto
        cursor = self.text_edit.textCursor()
        document = self.text_edit.document()

        # Obtener la posición del cursor y retroceder para encontrar el inicio de la palabra actual
        pos = cursor.position()
        cursor.movePosition(QTextCursor.StartOfWord, QTextCursor.MoveAnchor)
        start_pos = cursor.position()

        # Reemplazar la palabra actual con la selección del autocompletado
        cursor.setPosition(start_pos, QTextCursor.KeepAnchor)
        cursor.insertText(completion)

        # Resaltar la palabra completada
        cursor.setPosition(pos)
        cursor.movePosition(QTextCursor.EndOfWord, QTextCursor.KeepAnchor)
        char_format = QTextCharFormat()
        char_format.setBackground(Qt.yellow)
        cursor.setCharFormat(char_format)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
