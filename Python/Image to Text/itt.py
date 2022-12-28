try:
    from PIL import Image
except ImportError:
    import image
import pytesseract as ps

ps.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#mengubah gambar menjadi teks
print(ps.image_to_string(Image.open('img/puisi.jpeg')))