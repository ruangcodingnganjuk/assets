#import Library google TTS python
from gtts import gTTS
import os

# Masukkan Teks yang ingin dirubah ke suara
mytext = 'halo semua'

# pilih bahasa
language = 'id'

#proses pengubahan suara
myobj = gTTS(text=mytext, lang=language, slow=False)

#Save Suara.mp3
myobj.save("welcome.mp3")

# Memutar Suara
os.system("start welcome.mp3")
