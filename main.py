import pygame



pygame.init()
screen = pygame.display.set_mode((900,600))
background = pygame.image.load("space4.jpg")
icon = pygame.image.load("background.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("space invader")

while True:
    screen.blit(background,(0,50))
    pygame.display.update()