from graphics import *
import random
import time
import pygame
import math

pygame.init()
window = pygame.display.set_mode((1000, 750))
rect1 = pygame.Rect(random.randint(0, 925), random.randint(0, 675), 25, 25)
rect2 = pygame.Rect(0, 0, 91, 91)
corcle = pygame.draw.circle(window, (0, 0, 0), (100, 100), 8)
circXpos = 100
circYpos = 100
circXvel = 0
circYvel = 0
circXaccel = 0
circYaccel = .002
tick = 0
speed = 0
dy = 0
dx = 0
bounceCoefficient = .7

touched = False
floor = False
contacting = False

movement_speedy = 0
movement_speedx = 0
previous_mouse_position = (0,0)
previous_sample_time    = pygame.time.get_ticks()
ticks = 0

run = True
p1y = 0
p1x = 0
while run:
    # SETUP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            dx, dy = event.rel
            speed = (dx ** 2 + dy ** 2) ** (1/2)


    # MOUSE STUFF :
    current_mouse_pos = pygame.mouse.get_pos()
    if ( previous_mouse_position != current_mouse_pos and current_mouse_pos != None):
        # mouse has moved
        p1x = previous_mouse_position[0]
        p2x = current_mouse_pos[0]
        p1y = previous_mouse_position[1]
        p2y = current_mouse_pos[1]
        pixels_movementx = p2x - p1x
        pixels_movementy = p2y - p1y
        time_now        = pygame.time.get_ticks()
        movement_time   = ( time_now - previous_sample_time ) + 1 / 1000  # milliseconds -> seconds
        movement_speedy = pixels_movementy / movement_time
        movement_speedx = pixels_movementx / movement_time
        previous_mouse_position = current_mouse_pos
        previous_sample_time    = time_now
    elif ( previous_mouse_position == None ):
        # No previous recorded position
        previous_mouse_position = current_mouse_pos
        previous_sample_time    = pygame.time.get_ticks()
    else :
        # previous position = current
        if (abs(movement_speedy) < .0005) :
            movement_speedy = 0
        else :
            movement_speedy -= movement_speedy/50
        if (abs(movement_speedx) < .0005) :
            movement_speedx = 0
        else :
            movement_speedx -= movement_speedx/50

    # TICK CONTROL FOR MOUSE STUFF
    ticks += 1
    if (ticks == 500) :
        # print("movement_speed")
        # print(movement_speedy*500)
        # print("current_mouse_pos")
        # print(current_mouse_pos)
        # print("previous_mouse_position")
        # print(previous_mouse_position)
        ticks = 0

    # Floor
    if (floor) :
        if (circYpos >= 550) :
            circYpos = 550
            circYvel = 0
    if (pygame.mouse.get_pressed()[0]) :
        if (floor) :
            floor = False
        else :
            floor = True


    # ACTUAL MOVEMENT
    circXpos += circXvel
    circYpos += circYvel
    circXvel += circXaccel
    circYvel += circYaccel
    if (circYpos > 1000) :
        circYpos = 0
    if (circYpos < 0) :
        circYpos = 1000
    if (circXpos < 0) :
        circXpos = 999
    if (circXpos > 1000) :
        circXpos = 1

    # COLLISIONS!
    if (abs(circYpos - p1y) > abs(circXpos - p1x)) :
        if (corcle.colliderect(rect2) and circYpos < p1y) :
            circYvel = -abs(circYvel)*bounceCoefficient + movement_speedy/5*bounceCoefficient/.2
            circYpos -= 2
            if (movement_speedy < 0) :
                circYvel += movement_speedy/5*bounceCoefficient/.2
        if (corcle.colliderect(rect2) and circYpos > p1y) :
            circYvel = abs(circYvel)*bounceCoefficient + movement_speedy/5*bounceCoefficient/.2
            circYpos += 3
            if (movement_speedy > 0) :
                circYvel += movement_speedy/5*bounceCoefficient/.2
    else :
        if (corcle.colliderect(rect2) and circXpos > p1x) :
            if (not contacting) :
                print("worked")
                print(circXvel)
                circXvel = abs(circXvel)*bounceCoefficient + movement_speedx/5*bounceCoefficient/.2
                print(circXvel)
                circXpos += 3
            else :
                circXvel += movement_speedx/5
            contacting = True
        elif (corcle.colliderect(rect2) and circXpos < p1x) :
            if (not contacting) :
                circXvel = -abs(circXvel)*bounceCoefficient + movement_speedx/5*bounceCoefficient/.2
                circXpos -= 3
            else :
                circXvel += movement_speedx/5
            contacting = True
        else :
            contacting = False

    # SPEED CONTROL FOR IF IT GOES TOO FAST
    if (circYvel > 20 or circYvel < -20) :
        circYvel = 0
        circYpos = 375

    # RED RECTANGLE LEFTOVER STUFF LOL
    rect2.center = pygame.mouse.get_pos()
    collide = rect1.colliderect(rect2)
    color = (255, 0, 0) if collide else (255, 255, 255)

    window.fill((255, 255, 255))
    pygame.draw.rect(window, color, rect1)
    pygame.draw.rect(window, (0, 255, 0), rect2, 6, 1)
    corcle = pygame.draw.circle(window, (0, 0, 0), (circXpos, circYpos), 8)

    pygame.display.flip()

pygame.quit()
exit()




    # two diamonds that don't change rotation but can be pushed around
        # Use momentum and variating mass to make it realistic
    # balls dropped from cursor
    # Check if they are touching,
    # if they are, see what side it is
        # Check if it's above or below the center, and left or right of center
    # Set the new direction to
        # if current direction is greater than normal vector to bounce, than new dir = old dir + 2*dist between normal vector and old dir
        # else new dir = old dir - 2*dist between normal vector and old dir
    # win.getMouse() # Pause to view result
