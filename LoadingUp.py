from graphics import *
import random
import time

int

def main():
    n = random.randint(10, 50)
    win = GraphWin("Loading", 1500, 700, autoflush = False)
    sum = .1;
    summ = 0;

    win.setBackground(color_rgb(242, 255, 249))
    while sum < 800:

        aRectangle = Rectangle(Point(0,0), Point(1500,250))
        aRectangle.setFill(color_rgb(242, 255, 249))
        aRectangle.setWidth(0)

        bRectangle = Rectangle(Point(0,450), Point(1500,700))
        bRectangle.setFill(color_rgb(242, 255, 249))
        bRectangle.setWidth(0)
        # velrand = velrand-2
        n = random.randint(1, 5)
        summ += .002
        sum += summ
        c = Circle(Point(750,350), sum)
        # rand = random.randint(1, 2)

        c.setWidth(0)
        c.setFill(color_rgb(255, 186, 226))
        c.draw(win)
        aRectangle.draw(win)
        bRectangle.draw(win)
        time.sleep(.001)
        win.update()
        c.undraw()
        aRectangle.undraw()
        bRectangle.undraw()

    c.draw(win)
    aRectangle.draw(win)
    bRectangle.draw(win)
    message = Text(Point(750,350), "Press enter to continue")
    message.setSize(36)
    message.setStyle("bold")
    message.setTextColor(color_rgb(255, 255, 255))
    textr = 255
    textg = 186
    textb = 226
    # want 255, 186, 226
    #diff of 0, 69, 29
    loadEnd = True
    while loadEnd:
        for i in range(29):
            if (loadEnd == True):
                textg += 2.3793103448275863
                textb += 1
                textgint = int(textg)
                textbint = int(textb)
                if (textgint > 255):
                    textgint = 255;
                if (textbint > 255):
                    textbint = 255
                message.setTextColor(color_rgb(255, textgint, textbint))
                message.draw(win)
                keyString = win.checkKey()
                if (keyString == 'Return'):
                    loadEnd = False
                win.update()
                message.undraw()
                time.sleep(.05)
        time.sleep(.5)
        for i in range(29):
            if (loadEnd == True):
                textg -= 2.3793103448275863
                textb -= 1.0
                textgint = int(textg)
                textbint = int(textb)
                if (textgint > 255):
                    textgint = 255;
                if (textbint > 255):
                    textbint = 255
                message.setTextColor(color_rgb(255, textgint, textbint))
                message.draw(win)
                keyString = win.checkKey()
                if (keyString == 'Return'):
                    loadEnd = False
                win.update()
                time.sleep(.05)
                message.undraw()
    for i in range(6):
        message.setTextColor(color_rgb(255, 186, 226))
        message.undraw()
        message.draw(win)
        win.update()
        time.sleep(.08)
        message.setTextColor(color_rgb(255, 255, 255))
        message.undraw()
        message.draw(win)
        win.update()
        time.sleep(.08)
    for item in win.items[:]:
        item.undraw()
    win.update()
    message.draw(win)
    win.update()

    # win.getMouse() # Pause to view result
    win.close()    # Close window when done
    import physSim


main()
