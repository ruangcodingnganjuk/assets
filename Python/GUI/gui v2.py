import tkinter as tk
from tkinter import filedialog
import openpyxl

# Buat window utama
window = tk.Tk()
window.title("GUI dengan Tkinter")

# Buat label dan entry untuk mengisi file
label_file = tk.Label(text="Masukkan file Excel:")
label_file.grid(column=0, row=0)
entry_file = tk.Entry()
entry_file.grid(column=1, row=0)

# Buat tombol "Open" untuk membuka file dari komputer
def open_file():
  file = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
  entry_file.delete(0, tk.END)
  entry_file.insert(0, file)
  # Baca daftar sheet dari file Excel
  wb = openpyxl.load_workbook(file)
  sheets = wb.sheetnames
  # Kosongkan daftar sheet jika sebelumnya sudah ada isian
  sheet_var.set('')
  sheet_menu['menu'].delete(0, 'end')
  # Tambahkan daftar sheet ke dalam menu
  for sheet in sheets:
    sheet_menu['menu'].add_command(label=sheet, command=tk._setit(sheet_var, sheet))

button_open = tk.Button(text="Open", command=open_file)
button_open.grid(column=2, row=0)

# Buat label dan menu untuk memilih sheet
label_sheet = tk.Label(text="Pilih sheet:")
label_sheet.grid(column=0, row=1)
sheet_var = tk.StringVar(window)
sheet_menu = tk.OptionMenu(window, sheet_var, '')
sheet_menu.grid(column=1, row=1)

# Buat label dan entry untuk mengisi link
label_link = tk.Label(text="Masukkan link:")
label_link.grid(column=0, row=2)
entry_link = tk.Entry()
entry_link.grid(column=1, row=2)

# Buat tombol generate
def generate():
  file = entry_file.get()
  sheet = sheet_var.get()
  print("File:", file)
  print("Sheet:", sheet)

button_generate = tk.Button(text="Generate", command=generate)
button_generate.grid(column=1, row=3)

# Buat tombol clear untuk mengosongkan isian
def clear():
  entry_file.delete(0, tk.END)
  sheet_var.set('')
  sheet_menu['menu'].delete(0, 'end')

button_clear = tk.Button(text="Clear", command=clear)
button_clear.grid(column=1, row=4)

# Atur lebar kolom agar lebih rapi
window.columnconfigure(1, weight=1)

# Jalankan GUI
window.mainloop()
