import pygame

# Instalasi
pygame.init()

# setting layar
height = 600
width = 600

screen = pygame.display.set_mode([height, width])

# ubah tittle screen
pygame.display.set_caption('Ruang Coding Nganjuk')

# ubah warna screen
screen.fill((255, 255, 255)) #putih

# ganti logo screen
icon = pygame.image.load("ai.png")
pygame.display.set_icon(icon)

# import gambar ke screen
image = pygame.image.load("rbt.png")
screen.blit(image,(20,50))

running = True
while running:
    #loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

    pygame.display.update()

pygame.quit()