from PySide6.QtWidgets import QWidget
from views.UI import Ui_Form as UI

class MainUI(QWidget, UI):
    def __init__(self):
        super().__init__()
        #ponemos el tema en dark
        self.setStyleSheet("background-color: #2d2d2d; color: #ffffff;")
        self.setupUi(self)
        
