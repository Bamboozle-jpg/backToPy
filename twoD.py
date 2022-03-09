import OpenGL
import pygame
import random

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

global treeNum
treeNum = 40
global treeAngle
treeAngle = 25
global treeDist
treeDist = 40

vertices = (            #TRUNK :
    (.25, 0, .25),      #0
    (.25, 0, -.25),     #1
    (-.25, 0, .25),     #2
    (-.25, 0, -.25),    #3
    (.25, 1.5, .25),      #4
    (.25, 1.5, -.25),     #5
    (-.25, 1.5, .25),     #6
    (-.25, 1.5, -.25),    #7
                        #TOP VERTEX :
    (0, 5, 0),        #8
                        #EDGES OF TREE :
    (1, 1.5, 1),          #9
    (1, 1.5, -1),         #10
    (-1, 1.5, 1),         #11
    (-1, 1.5, -1)         #12
)

surfaces = (
    (0,1,2,3),          #TRUNK BASE
    (4,5,6,7),          #TRUNK TOP
                        #TRUNK UPS :
    (0,1,5,4),
    (0,2,6,4),
    (2,3,7,6),
    (1,3,7,5),
                        #TREE LEAVES :
    (8, 9, 10, 8),
    (8, 9, 11, 8),
    (8, 12, 10, 8),
    (8, 12, 11, 8)
)

# edges = (               #TRUNK BASE :
#     (0, 1),
#     (0, 2),
#     (3, 1),
#     (3, 2),
#                         #TRUNK UPs :
#     (0, 4),
#     (1, 5),
#     (2, 6),
#     (3, 7),
#                         #TRUNK TOP :
#     (4, 5),
#     (4, 6),
#     (7, 5),
#     (7, 6),
#                         #TREE BASE :
#     (9, 10),
#     (9, 11),
#     (12, 10),
#     (12, 11),
#                         #TREE UPs :
#     (8, 9),
#     (8, 10),
#     (8, 11),
#     (8, 12),
# )

groundColors = (
    (.6, .5, .5),
    (.35, .25, .25),
    (.85, .75, .75),
    (.7, .6, .6)
)
colors = ((
    (.4,.3,.3),
    (.3,.2,.2),
    (.4,.3,.3),
    (.2,.1,.1),
    ),(
    (1,0,0), #NOTHING?
    (1,0,0),
    (1,0,0),
    (1,0,0),
    ),(
    (1,0,0), #NOTHING?
    (1,0,0),
    (1,0,0),
    (1,0,0),
    ),(
    (.4,.3,.3), #TRUNK BASE AND SIDE 1
    (.3,.2,.2),
    (.4,.3,.3),
    (.2,.1,.1),
    ),(
    (.4,.3,.3), #TRUNK BASE AND SIDE 1
    (.3,.2,.2),
    (.4,.3,.3),
    (.2,.1,.1),
    ),(
    (.4,.3,.3), #TRUNK SIDE 2
    (.3,.2,.2),
    (.4,.3,.3),
    (.2,.1,.1),
    ),(
    (.4,.3,.3), #TRUNK SIDE 3
    (.3,.2,.2),
    (.4,.3,.3),
    (.2,.1,.1),
    ),(
    (.2,.6,0), #TREE... AND TRUNK BASE?????
    (.3,.6,0),
    (.4,.5,0),
    (.2,.4,.1),
    ),(
    (.2,.6,0), #TREE... AND TRUNK BASE?????
    (.3,.6,0),
    (.4,.5,0),
    (.2,.4,.1),
    ),(
    (.2,.6,0), #TREE... AND TRUNK BASE?????
    (.3,.6,0),
    (.4,.5,0),
    (.2,.4,.1),
    ),(
    (.2,.6,0), #TREE... AND TRUNK BASE?????
    (.3,.6,0),
    (.4,.5,0),
    (.2,.4,.1),
    ),(
    (.2,.6,0), #TREE... AND TRUNK BASE?????
    (.3,.6,0),
    (.4,.5,0),
    (.2,.4,.1),
    )
)

ground_surfaces = (0,1,2,3)

ground_vertices = (
    (-20,-5,-20),
    (20,-5,-20),
    (20,-5,20),
    (-20,-5,20)
)

def Settings():
    #SETUP/SETTINGS
    X = 1600
    Y = 800
    settingsRunning = True
    global treeNum
    treeNum = 40
    global treeAngle
    treeAngle = 25
    global treeDist
    treeDist = 40

    pygame.init()
    bone = (242, 255, 249)
    pink = (255, 186, 226)
    colorNum = pink
    highlightNum = bone

    colorAngle = bone
    highlightAngle = pink

    colorDist = bone
    highlightDist = pink

    display_surface = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('Tree Simulation')
    font = pygame.font.Font('freesansbold.ttf', 64)

    selected = 0
    while settingsRunning :
        treeNumRender = font.render(('Number of Trees : < ' + str(treeNum) + ' >'), True, colorNum, highlightNum)
        treeNumRect = treeNumRender.get_rect()
        treeNumRect.center = (X // 2, (Y // 2) - 100)

        treeAngleRender = font.render(('Angle of Camera (up/down) : < ' + str(treeAngle) + ' >'), True, colorAngle, highlightAngle)
        treeAngleRect = treeAngleRender.get_rect()
        treeAngleRect.center = (X // 2, Y // 2)

        treeDistRender = font.render(('How far Away you are: < ' + str(treeDist) + ' >'), True, colorDist, highlightDist)
        treeDistRect = treeDistRender.get_rect()
        treeDistRect.center = (X // 2, (Y // 2) + 100)


        display_surface.fill(pink)
        display_surface.blit(treeNumRender, treeNumRect)
        display_surface.blit(treeAngleRender, treeAngleRect)
        display_surface.blit(treeDistRender, treeDistRect)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    settingsRunning = 0
                if event.key == pygame.K_UP:
                    selected -= 1
                if event.key == pygame.K_DOWN:
                    selected += 1
                if event.key == pygame.K_RIGHT:
                    if selected == 0:
                        treeNum += 1
                    elif selected == 1:
                        treeAngle += 1
                    elif selected == 2:
                        treeDist += 1
                if event.key == pygame.K_LEFT:
                    if selected == 0:
                        treeNum -= 1
                    elif selected == 1:
                        treeAngle -= 1
                    elif selected == 2:
                        treeDist -= 1
                if event.key == pygame.K_d:
                    if selected == 0:
                        treeNum += 10
                    elif selected == 1:
                        treeAngle += 10
                    elif selected == 2:
                        treeDist += 10
                if event.key == pygame.K_a:
                    if selected == 0:
                        treeNum -= 10
                    elif selected == 1:
                        treeAngle -= 10
                    elif selected == 2:
                        treeDist -= 10
        if selected > 2:
            selected = 0
        if selected < 0:
            selected = 2

        if selected == 0:
            colorNum = pink
            highlightNum = bone

            colorAngle = bone
            highlightAngle = pink

            colorDist = bone
            highlightDist = pink
        if selected == 1:
            colorNum = bone
            highlightNum = pink

            colorAngle = pink
            highlightAngle = bone

            colorDist = bone
            highlightDist = pink
        if selected == 2:
            colorNum = bone
            highlightNum = pink

            colorAngle = bone
            highlightAngle = pink

            colorDist = pink
            highlightDist = bone


        pygame.display.update()





def Ground():

    glBegin(GL_QUADS)

    x = 0
    y = 0
    for vertex in ground_vertices:
        x+=1
        y += 1
        if y > 3:
            y = 0
        glColor3fv(groundColors[y])
        glVertex3fv(vertex)

    glEnd()

def set_vertices(max_distance):
    x_value_change = random.randrange(-18,18)
    y_value_change = -5
    z_value_change = random.randrange(-18,18)

    new_vertices = []

    for vert in vertices:
        new_vert = []

        new_x = vert[0] + x_value_change
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices

def Cube(vertices):
    glBegin(GL_QUADS)
    y = 0
    for surface in surfaces:
        x = 0
        y+=1
        for vertex in surface:
            x+=1
            if x > 3:
                x = 0
            glColor3fv(colors[y][x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    # for edge in edges:
    #     for vertex in edge:
    #         glVertex3fv(vertices[vertex])
    glEnd()


def main():
    Settings()
    mainRunning = True
    pygame.init()
    display = (1600, 800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    #Display Setup

    gluPerspective(45, display[0]/display[1], 0.1, 300.0)
    glTranslatef(0, 2, -treeDist)
    glRotatef(treeAngle, 25, 0, 0)
    #FOV
    #Aspect ration (display width/height)
    #Znear & Zfar (clipping planes)

    x_move = 0
    y_move = 0
    max_distance = 30
    #For making as many as in range
    cube_dict = {}


    i = 0
    j = treeNum
    # for x in range(treeNum):
    #     cube_dict[x] = set_vertices(max_distance)

    accel = 0
    accelDir = False
    while mainRunning:
        if i > 5:
            i = 0
        i += 1

        if i == 5:
            if j > 0:
                cube_dict[j] = set_vertices(max_distance)
                j -= 1
        #ME====================
        if accel >= 1 :
            accelDir = True
        elif accel <= -1 :
            accelDir = False
        if not accelDir :
            accel += .05
        else :
            accel -= .05
        #Me stuff
        # glRotatef(10, 0, 4, 0)
        glTranslatef(0, accel/10, 0)
        #ME========================
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            glRotatef(2, 0, 2, 0)
        if keys[pygame.K_LEFT]:
            glRotatef(-2, 0, 2, 0)
        # if keys[pygame.K_UP]:
        #     #test
        # if keys[pygame.K_DOWN]:
        #     #Test
        for event in pygame.event.get():
            #Quit events
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mainRunning = False
            #Key press events

        # glTranslatef(random.randrange(-10,10),random.randrange(-10,10), -60)
        #Multiplies Matrix by transition matrix
        #AKA Move back 5 units (z)

        #camera setup
        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        #Refresh screen?
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #Make ground
        Ground()

        #move all cubes forward
        glTranslatef(x_move,y_move,0)

        #DRAW ALL
        for each_cube in cube_dict:
            Cube(cube_dict[each_cube])
            # glRotatef(10, 0, 4, 0)

        pygame.display.flip()
        pygame.time.wait(25)

#-------------------------------------------------------------------
        # object_passed = False
while True:
    main()
pygame.quit()
quit()
