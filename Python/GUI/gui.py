import tkinter as tk
import psutil

def update_info():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    gpu_info = get_gpu_info()
    temperature = get_temperature()
    cpu_label.config(text="CPU: {}%".format(cpu_percent))
    memory_label.config(text="Memory: {}%".format(memory_percent))
    gpu_label.config(text="GPU: {}".format(gpu_info))
    temperature_label.config(text="Temperature: {}°C".format(temperature))
    root.after(1000, update_info)

root = tk.Tk()
root.title("Monitoring Info")

cpu_label = tk.Label(root, text="CPU:")
cpu_label.pack()

memory_label = tk.Label(root, text="Memory:")
memory_label.pack()

gpu_label = tk.Label(root, text="GPU:")
gpu_label.pack()

temperature_label = tk.Label(root, text="Temperature:")
temperature_label.pack()

update_info()
root.mainloop()
