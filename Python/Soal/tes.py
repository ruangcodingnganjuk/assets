import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class Sederhana(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Buat tombol dan label
        self.tombol = QPushButton('Klik Saya', self)
        self.label = QLabel('Belum Diklik', self)

        # Atur posisi tombol dan label
        self.tombol.move(50, 50)
        self.label.move(50, 100)

        # Atur ukuran widget
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('GUI Sederhana')

        # Atur event handler untuk tombol
        self.tombol.clicked.connect(self.tombol_diklik)

    def tombol_diklik(self):
        self.label.setText('Sudah Diklik')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Sederhana()
    ex.show()
    sys.exit(app.exec_())
