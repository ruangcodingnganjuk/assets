import matplotlib.pyplot as plt
import numpy as np

# membuat data x dan y
theta = np.linspace(0, 2*np.pi, 100)
x = 20 * np.cos(theta) + 50
y = 20 * np.sin(theta) + 50

# memplot lingkaran untuk bagian tubuh kupu
plt.plot(x, y)

# membuat data x dan y untuk sayap kupu
theta = np.linspace(np.pi/2, 3*np.pi/2, 100)
x = 15 * np.cos(theta) + 50
y = 15 * np.sin(theta) + 50

# memplot lingkaran untuk sayap kupu pertama
plt.plot(x, y)

# membuat data x dan y untuk sayap kupu
theta = np.linspace(np.pi/2, 3*np.pi/2, 100)
x = 15 * np.cos(theta) + 75
y = 15 * np.sin(theta) + 50

# memplot lingkaran untuk sayap kupu kedua
plt.plot(x, y)

# menampilkan grafik
plt.show()
