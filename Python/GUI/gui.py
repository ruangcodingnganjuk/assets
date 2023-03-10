import tkinter as tk
from tkinter import filedialog

# Buat window utama
window = tk.Tk()
window.title("GUI dengan Tkinter")

# Buat label dan entry untuk mengisi file
label_file = tk.Label(text="Masukkan file:")
label_file.grid(column=0, row=0)
entry_file = tk.Entry()
entry_file.grid(column=1, row=0)

# Buat tombol "Open" untuk membuka file dari komputer
def open_file():
  file = filedialog.askopenfilename()
  entry_file.delete(0, tk.END)
  entry_file.insert(0, file)

button_open = tk.Button(text="Open", command=open_file)
button_open.grid(column=2, row=0)

# Buat label dan entry untuk mengisi link
label_link = tk.Label(text="Masukkan link:")
label_link.grid(column=0, row=1)
entry_link = tk.Entry()
entry_link.grid(column=1, row=1)

# Buat tombol generate
def generate():
  file = entry_file.get()
  link = entry_link.get()
  print("File:", file)
  print("Link:", link)

button_generate = tk.Button(text="Generate", command=generate)
button_generate.grid(column=1, row=2)

# Buat tombol clear untuk mengosongkan isian
def clear():
  entry_file.delete(0, tk.END)
  entry_link.delete(0, tk.END)

button_clear = tk.Button(text="Clear", command=clear)
button_clear.grid(column=2, row=1)

# Atur lebar kolom agar lebih rapi
window.columnconfigure(1, weight=1)

# Jalankan GUI
window.mainloop()
