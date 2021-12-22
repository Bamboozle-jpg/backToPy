from graphics import *
import random
import time
import pygame
from pygame.locals import *
import math

gameRun = True

pygame.init()
w, h = 1240, 900
screen = pygame.display.set_mode((w, h))

# Background image
background = pygame.image.load('parchment.png')
background.convert()
backgroundRect = background.get_rect()
backgroundRect.center = w/2, h/2

# Table hee hoo
table = pygame.image.load('table.jpg')
table = pygame.transform.rotozoom(table, 0, 2.5)
table.convert()
tableRect = table.get_rect()
tableRect.center = w/2, h-70

# Flask image
flask = pygame.image.load('flask.png')
flask = pygame.transform.rotozoom(flask, 0, .5)
flask = pygame.transform.flip(flask, True, False)
flask.convert()
flaskRect = flask.get_rect()
flaskRect.center = w/2 + 400, h/2
moving = False

# Game run loop
while (gameRun) :

    # Something to do with quitting the game.... I think
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # Moving the flask
        elif event.type == MOUSEBUTTONDOWN:
            if flaskRect.collidepoint(event.pos):
                moving = True

        # Don't move if not clicking
        elif event.type == MOUSEBUTTONUP:
            moving = False

        # Do move flask if move mouse while clicking on it
        elif event.type == MOUSEMOTION and moving:
            flaskRect.move_ip(event.rel)

    screen.fill((255, 255, 255))
    screen.blit(background, backgroundRect)
    screen.blit(flask, flaskRect)
    screen.blit(table, tableRect)

    pygame.draw.rect(screen, (255, 255, 255), backgroundRect, 1)
    pygame.draw.rect(screen, 0, flaskRect, -1)
    pygame.draw.rect(screen, 0, tableRect, 5)
    pygame.display.update()

pygame.quit()
