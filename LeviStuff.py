import pygame
import math
import colorsys
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

scrnW = 300
scrnH = 600
x_charsize = 14
y_charsize = 14
x_slots = math.floor(scrnW/x_charsize)
y_slots = math.floor(scrnH/y_charsize)
print(str(x_slots)+", "+str(y_slots))

screen = pygame.display.set_mode((scrnW, scrnH))
display_surface = pygame.display.set_mode((scrnW, scrnH))
pygame.display.set_caption('wowie zoinks gaming')
font = pygame.font.SysFont('Courier', 16)

def text_display(letter, x_slot, y_slot):
    text = font.render(str(letter), True, white)
    display_surface.blit(text, (x_charsize*x_slot, y_charsize*y_slot))

# [a][b][c]
# [1][2][3]
# =
# [[a,b,c],[1,2,3]]

display_letters = [[[' ']*x_slots]*y_slots]
def add_character(x_slot, y_slot, letter):
    display_letters[0][y_slot][x_slot] = letter

add_character(0,0,'B')
add_character(5,0,'A')

run = True
while run:
    screen.fill(black)
    print(display_letters)
    for i in range(0, y_slots):
        for j in range(0, x_slots):
            text_display(display_letters[i][j],j,i)

    pygame.display.update()
    time.sleep(5)
