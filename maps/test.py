import csv
from PySide6.QtCore import Qt
from PySide6.QtWidgets import  QComboBox, QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle("Autorellenado desde CSV")
        self.setGeometry(100, 100, 300, 150)

        # Crear el layout principal
        layout = QVBoxLayout()

        # Crear los widgets
        self.label = QLabel("Autorellenado")
        self.label.setAlignment(Qt.AlignCenter)
        self.text_input = QLineEdit()
        #Creamos un combo box que tendra unos valores predefinidos barcerlona, madrid, valencia
        self.combo = QComboBox()
        self.combo.addItems(["Barcelona", "Madrid", "Valencia"])
        self.button = QPushButton("Cargar datos")
        self.button.clicked.connect(self.load_data)

        # Agregar los widgets al layout
        layout.addWidget(self.label)
        layout.addWidget(self.combo)
        layout.addWidget(self.text_input)
        layout.addWidget(self.button)

        # Crear el widget central y agregarle el layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Crear la lista de datos
        self.data = {}

    def load_data(self):
        # Cargar los datos del archivo CSV
        with open('noms-carrer-v1r0-20210702.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.data[row['texto']] = row['valor']

    def keyPressEvent(self, event):
        # Buscar el valor correspondiente al texto ingresado y mostrarlo en el label
        if event.key() == Qt.Key_Return:
            text = self.text_input.text()
            if text in self.data:
                self.label.setText(self.data[text])
            else:
                self.label.setText("No se encontró el valor")

if __name__ == '__main__':
    # Crear la aplicación y la ventana principal
    app = QApplication([])
    window = MainWindow()
    window.show()

    # Ejecutar la aplicación
    app.exec_()
