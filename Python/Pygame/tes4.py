import pygame
import random

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

# ganti bg
bg = pygame.image.load("bg.jpg")

# import gambar ke screen
def train(x,y):
    image = pygame.image.load("train.png")
    screen.blit(image,(x,y))

x = 0
y = 0

x_point = 0
y_point = 0

# membuat musuh
def enemy(x,y):
    image = pygame.image.load("enemy.png")
    screen.blit(image,(x_enemy,y_enemy))

x_enemy = random.randint(0,600)
y_enemy = random.randint(0,600)

x_point_enemy = 0
y_point_enemy = 0

running = True
while running:
    #loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

        # Apabila kita menekan tombol
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x_point -= 0.6
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                x_point += 0.6
            if event.key == pygame.K_UP or event.key == ord('w'):
                y_point -= 0.6
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                y_point += 0.6

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

        # Batasan
        if x <= 0:
            x = 0
        elif x >= 525:
            x = 525
        if y <= 0:
            y = 0
        elif y >= 550:
            y = 550

    screen.fill((255, 255, 255))

    screen.blit(bg, (0,0))

    x += x_point 
    y += y_point

    # Menampilkan gambar ke dalam screen
    train(x,y)
    # Menampilkan musuh
    enemy(x,y)

    pygame.display.update()

pygame.quit()