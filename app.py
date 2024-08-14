import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget


# Subclass QMainWindow to customize your application's main window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fishing Simulator")
        self.setFixedSize(QSize(800, 600))

        button = QPushButton("Press Me!")


        main_layout = QVBoxLayout()
        main_layout.addWidget(button)

        # pole selection
        pole_select_widget = QWidget()
        pole_select_layout = QVBoxLayout()

        self.setLayout(main_layout)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()