import requests
from bs4 import BeautifulSoup

# Memuat soal dari link yang diberikan
url = "https://wirahadie.com/materi-bahasa-indonesia-kelas-10/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# Mencari semua tag <p> yang berisi soal
soal_tags = soup.find_all("p")

# Inisialisasi list untuk menyimpan soal dan jawaban
soal_list = []
jawaban_list = []

# Iterasi setiap tag <p> untuk mengambil soal dan jawaban
for soal_tag in soal_tags:
    # Mencari tag <strong> untuk mengambil soal
    soal_strong_tag = soal_tag.find("strong")
    if soal_strong_tag is not None:
        soal = soal_strong_tag.text
        # Mencari tag <br/> untuk memisahkan soal dan jawaban
        jawaban_br_tag = soal_tag.find("br")
        # Jika tag <br/> ditemukan, maka ambil bagian setelah tag <br/> sebagai jawaban
        if jawaban_br_tag is not None:
            jawaban = soal_tag.text.split("<br/>")[1]
            # Menambahkan soal dan jawaban ke list
            soal_list.append(soal)
            jawaban_list.append(jawaban)

# Inisialisasi variabel untuk menyimpan jumlah soal yang benar
jumlah_benar = 0

# Iterasi setiap soal untuk memunculkan soal dan meminta jawaban dari pengguna
for i in range(len(soal_list)):
    # Menampilkan soal
    print("Soal", i + 1)
    print(soal_list[i])
    # Meminta jawaban dari pengguna
    jawaban = input("Jawaban: ")
    # Menambahkan jumlah soal yang benar jika jawaban benar
    if jawaban.lower() == jawaban_list[i].lower():
        jumlah_benar += 1

# Menampilkan jumlah soal yang benar
print("Jumlah soal yang benar:", jumlah_benar)
