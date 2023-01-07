import pygame

# Instalasi
pygame.init()

# setting layar
height = 600
width = 600

screen = pygame.display.set_mode([height, width])

# ubah warna screen
screen.fill((255, 0, 0))

# membuat lingkaran
pygame.draw.circle(screen, (0,0,255), (300,300), 75)
# #  membuat garis
pygame.draw.line(screen, (0,0,255),(100,100), (300,300), 75)

running = True
while running:
    #loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

    pygame.display.update()

pygame.quit()