import pytesseract as ps
from gtts import gTTS
from PIL import Image
import os

ps.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Buka gambar
image = Image.open('img/puisi.jpeg')

# Konversi gambar ke teks dengan pytesseract
text = ps.image_to_string(image)
print(ps.image_to_string(image))

language = 'id'
# Buat objek gTTS
tts = gTTS(text, lang=language, slow=False)

# Simpan suara ke file
tts.save('suara.mp3')

# Putar suara dengan menggunakan aplikasi default
os.system("suara.mp3")
