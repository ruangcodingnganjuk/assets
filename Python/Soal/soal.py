import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout
from bs4 import BeautifulSoup

class UjianSimulasi(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        def initUI(self):
            # Muat soal dan jawaban dari link materi
            self.soal, self.jawaban = self.muat_soal()

            # Buat label dan line edit untuk nama peserta
            nama_label = QLabel('Nama:', self)
            self.nama_edit = QLineEdit(self)

            # Buat label untuk menampilkan soal
            self.soal_label = QLabel(self)
            self.soal_label.setWordWrap(True)

            # Buat radio button untuk opsi jawaban
            self.opsi_a = QRadioButton("A", self)
            self.opsi_b = QRadioButton("B", self)
            self.opsi_c = QRadioButton("C", self)
            self.opsi_d = QRadioButton("D", self)

            # Buat tombol Selanjutnya, Kembali, dan Selesai
            self.next_button = QPushButton('Selanjutnya', self)
            self.prev_button = QPushButton('Kembali', self)
            self.selesai_button = QPushButton('Selesai', self)

            # Buat layout vertikal untuk menampung semua widget
            vbox = QVBoxLayout()
            vbox.addWidget(nama_label)
            vbox.addWidget(self.nama_edit)
            vbox.addWidget(self.soal_label)
            vbox.addWidget(self.opsi_a)
            vbox.addWidget(self.opsi_b)
            vbox.addWidget(self.opsi_c)
            vbox.addWidget(self.opsi_d)

            # Buat layout horizontal untuk menampung tombol Selanjutnya, Kembali, dan Selesai
            hbox = QHBoxLayout()
            hbox.addWidget(self.prev_button)
            hbox.addWidget(self.next_button)
            hbox.addWidget(self.selesai_button)

            # Tambahkan layout horizontal ke dalam layout vertikal
            vbox.addLayout(hbox)

            # Buat label untuk menampilkan nilai akhir
            self.nilai_label = QLabel(self)

            # Tambahkan label nilai akhir ke dalam layout vertikal
            vbox.addWidget(self.nilai_label)

            # Atur layout untuk widget ini
            self.setLayout(vbox)

            # Tentukan ukuran dan posisi widget
            self.setGeometry(300, 300, 300, 150)
            self.setWindowTitle('Ujian Simulasi')

            # Tampilkan soal pertama
            self.tampilkan_soal(0)

            # Atur event handler untuk tombol Selanjutnya
            self.next_button.clicked.connect(self.selanjutnya)

            # Atur event handler untuk tombol Kembali
            self.prev_button.clicked.connect(self.kembali)

            # Atur event handler untuk tombol Selesai
            self.selesai_button.clicked.connect(self.selesai)

            # Sembunyikan tombol Kembali saat ini
            self.prev_button.hide()

            # Sembunyikan label nilai akhir saat ini
            self.nilai_label.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UjianSimulasi()
    ex.show()
    sys.exit(app.exec_())

# def muat_soal(self):
#     # Muat halaman web menggunakan requests dan BeautifulSoup
#     page = requests.get("https://wirahadie.com/materi-bahasa-indonesia-kelas-10/")
#     soup = BeautifulSoup(page.content, "html.parser")

#     # Cari semua tag div dengan class "entry-content"
#     divs = soup.find_all("div", class_="entry-content")

#     # Inisialisasi list soal dan jawaban
#     soal = []
#     jawaban = []

#     # Iterasi setiap tag div
#     for div in divs:
#         # Cari semua tag p di dalam div
#         ps = div.find_all("p")

#             # Iterasi setiap tag p
#         for p in ps:
#                 # Jika tag p mengandung soal
#             if p.strong is not None:
#                     # Tambahkan soal ke list soal
#                 soal.append(p.get_text())
#                 # Jika tag p mengandung jawaban
#             elif "Jawaban:" in p.get_text():
#                     # Tambahkan jawaban ke list jawaban
#                 jawaban.append(p.get_text()[-1])

#     # Kembalikan list soal dan jawaban
#     return soal, jawaban

# def tampilkan_soal(self, indeks):
#         # Tampilkan soal ke indeks yang ditentukan
#         self.soal_label.setText(self.soal[indeks])

#         # Bersihkan semua radio button
#         self.opsi_a.setChecked(False)
#         self.opsi_b.setChecked(False)
#         self.opsi_c.setChecked(False)
#         self.opsi_d.setChecked(False)  

# def selanjutnya(self):
#     # Dapatkan indeks soal saat ini
#     indeks = self.soal.index(self.soal_label.text())

#     # Jika ini bukan soal terakhir
#     if indeks < len(self.soal) - 1:
#         # Tampilkan soal berikutnya
#         self.tampilkan_soal(indeks + 1)

#         # Tampilkan tombol Kembali
#         self.prev_button.show()
#     # Jika ini adalah soal terakhir
#     else:
#         # Sembunyikan tombol Selanjutnya
#         self.next_button.hide()

# def kembali(self):
#     # Dapatkan indeks soal saat ini
#     indeks = self.soal.index(self.soal_label.text())

#     # Jika ini bukan soal pertama
#     if indeks > 0:
#         # Tampilkan soal sebelumnya
#         self.tampilkan_soal(indeks - 1)

#         # Sembunyikan tombol Kembali jika ini adalah soal pertama
#     if indeks == 1:
#         self.prev_button.hide()
#     # Tampilkan tombol Selanjutnya
#         self.next_button.show()

# def selesai(self):
#     # Dapatkan jawaban yang dipilih
#     jawaban = ""
#     if self.opsi_a.isChecked():
#         jawaban = "A"
#     elif self.opsi_b.isChecked():
#         jawaban = "B"
#     elif self.opsi_c.isChecked():
#         jawaban = "C"
#     elif self.opsi_d.isChecked():
#         jawaban = "D"

#         # Jika jawaban belum dipilih
#         if jawaban == "":
#                 # Tampilkan pesan error
#             self.nilai_label.setText("Pilih jawaban terlebih dahulu!")
#             self.nilai_label.setStyleSheet("color: red")
#             self.nilai_label.show()
#             # Jika jawaban sudah dipilih
#         else:
#                 # Sembunyikan tombol Selesai
#             self.selesai_button.hide()

#             # Hitung nilai akhir
#             nilai = 0
#             for i, soal in enumerate(self.soal):
#                 if self.jawaban[i] == jawaban[i]:
#                     nilai += 1

#         # Tampilkan nilai akhir
#             self.nilai_label.setText(f"Nilai akhir: {nilai}")
#             self.nilai_label.setStyleSheet("color: black")
#             self.nilai_label.show()

# def main():
#     app = QApplication([sys.argv])
#     ex = UjianSimulasi()
#     ex.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#         main()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = UjianSimulasi()
#     ex.show()
#     sys.exit(app.exec_())
            