import pygame

# Instalasi
pygame.init()

# setting layar
height = 600
width = 600

screen = pygame.display.set_mode([height, width])

# ubah tittle screen
pygame.display.set_caption('GAMEBOT by Wildan Taufiq')

# ubah warna screen
screen.fill((255, 255, 255))

# ganti logo screen
icon = pygame.image.load("ai.png")
pygame.display.set_icon(icon)

# import gambar ke screen
def train(x,y):
    image = pygame.image.load("train.png")
    screen.blit(image,(x,y))

x = 0
y = 0

x_point = 0
y_point = 0

running = True
while running:
    #loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

        # Apabila kita menekan tombol
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x_point -= 0.5
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x_point += 0.5
            if event.key == pygame.K_UP or event.key == ord('w'):
                y_point -= 0.5
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                y_point += 0.5

        # Apabila Kita melepas tombol
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x_point = 0
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x_point = 0
            if event.key == pygame.K_UP or event.key == ord('w'):
                y_point = 0
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                y_point = 0

    screen.fill((255, 255, 255))

    x += x_point 
    y += y_point

    # Menampilkan gambar ke dalam screen
    train(x,y)

    pygame.display.update()

pygame.quit()