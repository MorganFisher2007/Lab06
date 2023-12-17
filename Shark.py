from random import *
from math import *

class Shark:

    def __init__(self, xpos, ypos):

        self.xpos = xpos
        self.ypos = ypos
        self.closefishx = -1
        self.closefishy = -1
        self.image = "shark-facing-north-clear.png"
        self.recent_fish = []
        

    def setsharkpos(self, xpos, ypos):

        self.xpos = xpos
        self.ypos = ypos

    def get_x_pos(self):
        return self.xpos
                
    def get_y_pos(self):
        return self.ypos

    def move(self, closefishx, closefishy):
        if closefishx - self.xpos == 1 and closefishy - self.ypos == 1:
            self.xpos += 1
            self.ypos += 1
        elif closefishx - self.xpos == -1 and closefishy - self.ypos == -1:
            self.xpos -= 1
            self.ypos -= 1
        elif closefishx - self.xpos == 1 and closefishy - self.ypos == -1:
            self.xpos += 1
            self.ypos -= 1
        elif closefishx - self.xpos == -1 and closefishy - self.ypos == 1:
            self.xpos -= 1
            self.ypos += 1
        elif closefishx == self.xpos and closefishy - self.ypos == 1:
            self.ypos += 1
        elif closefishx == self.xpos and closefishy - self.ypos == -1:
            self.ypos -= 1
        elif closefishy == self.ypos and closefishx - self.xpos == 1:
            self.xpos += 1
        elif closefishy == self.ypos and closefishx - self.xpos == -1:
            self.xpos -= 1

        elif closefishx - self.xpos > 2 and closefishy - self.ypos == 1:
            self.xpos += 2
            if self.ypos < 9:
                self.ypos += 2
        elif closefishx - self.xpos > 2 and closefishy - self.ypos == -1:
            self.xpos += 2
            if self.ypos > 2:
                self.ypos -= 2
        elif closefishx - self.xpos < -2 and closefishy - self.ypos == 1:
            self.xpos -= 2
            if self.ypos < 9:
                self.ypos += 2
        elif closefishx - self.xpos < -2 and closefishy - self.ypos == -1:
            self.xpos -= 2
            if self.ypos > 2:
                self.ypos -= 2
            
        elif closefishx - self.xpos == 1 and closefishy - self.ypos > 2:
            if self.xpos < 9:
                self.xpos += 2
            self.ypos += 2
        elif closefishx - self.xpos == -1 and closefishy - self.ypos > 2:
            if self.xpos > 2:
                self.xpos -= 2
            self.ypos += 2
        elif closefishx - self.xpos == 1 and closefishy - self.ypos < -2:
            if self.xpos < 9:
                self.xpos += 2
            self.ypos -= 2
        elif closefishx - self.xpos == -1 and closefishy - self.ypos < -2:
            if self.xpos > 2:
                self.xpos -= 2
            self.ypos -= 2
            

        elif closefishx - self.xpos >= 2 and closefishy - self.ypos >= 2:
            self.xpos += 2
            self.ypos += 2
        elif closefishx - self.xpos <= -2 and closefishy - self.ypos <= -2:
            self.xpos -= 2
            self.ypos -= 2
        elif closefishx - self.xpos >= 2 and closefishy - self.ypos <= -2:
            self.xpos += 2
            self.ypos -= 2
        elif closefishx - self.xpos <= -2 and closefishy - self.ypos >= 2:
            self.xpos -= 2
            self.ypos += 2
        elif closefishx == self.xpos and closefishy - self.ypos >= 2:
            self.ypos += 2
        elif closefishx == self.xpos and closefishy - self.ypos <= -2:
            self.ypos -= 2
        elif closefishy == self.ypos and closefishx - self.xpos >= 2:
            self.xpos += 2
        elif closefishy == self.ypos and closefishx - self.xpos <= -2:
            self.xpos -= 2

        elif closefishx - self.xpos == 2 and closefishy - self.ypos == 1:
            self.xpos += 2
            self.ypos += 1
        elif closefishx - self.xpos == 2 and closefishy - self.ypos == -1:
            self.xpos += 2
            self.ypos -= 1
        elif closefishx - self.xpos == -2 and closefishy - self.ypos == 1:
            self.xpos -= 2
            self.ypos += 1
        elif closefishx - self.xpos == -2 and closefishy - self.ypos == -1:
            self.xpos -= 2
            self.ypos -= 1
        
        elif closefishy - self.ypos == 2 and closefishx - self.xpos == 1:
            self.ypos += 2
            self.xpos += 1
        elif closefishy - self.ypos == 2 and closefishx - self.xpos == -1:
            self.ypos += 2
            self.xpos -= 1
        elif closefishy - self.ypos == -2 and closefishx - self.xpos == 1:
            self.ypos -= 2
            self.xpos += 1
        elif closefishy - self.ypos == -2 and closefishx - self.xpos == -1:
            self.ypos -= 2
            self.xpos -= 1

        return (self.xpos, self.ypos)

        
    def closestfish(self, fish1x, fish1y, fish2x=99, fish2y=99, fish3x=99, fish3y=99):
        
        distfish1 = sqrt(float(((fish1x - self.xpos)**2) + ((fish1y - self.ypos)**2)))
        distfish2 = sqrt(float(((fish2x - self.xpos)**2) + ((fish2y - self.ypos)**2)))
        distfish3 = sqrt(float(((fish3x - self.xpos)**2) + ((fish3y - self.ypos)**2)))

        randomfish = []

        if distfish1 < distfish2 and distfish1 < distfish3:
            closestfish = (fish1x, fish1y)
        
        elif distfish2 < distfish1 and distfish2 < distfish3:
            closestfish = (fish2x, fish2y)
            
        elif distfish3 < distfish1 and distfish3 < distfish2:
            closestfish = (fish3x, fish3y)

        elif distfish1 == distfish2 and distfish1 < distfish3:

            closestfish1 = (fish1x, fish1y)
            closestfish2 = (fish2x, fish2y)

            randomfish.append(closestfish1)
            randomfish.append(closestfish2)
                               
            closestfish = choice(randomfish)

        elif distfish1 == distfish3 and distfish1 < distfish2:

            closestfish1 = (fish1x, fish1y)
            closestfish2 = (fish3x, fish3y)

            randomfish.append(closestfish1)
            randomfish.append(closestfish2)
                               
            closestfish = choice(randomfish)

        elif distfish2 == distfish3 and distfish2 < distfish1:

            closestfish1 = (fish2x, fish2y)
            closestfish2 = (fish3x, fish3y)

            randomfish.append(closestfish1)
            randomfish.append(closestfish2)
                               
            closestfish = choice(randomfish)

        elif distfish1 == distfish2 == distfish3:

            closestfish1 = (fish1x, fish1y)
            closestfish2 = (fish2x, fish2y)
            closestfish3 = (fish3x, fish3y)

            randomfish.append(closestfish1)
            randomfish.append(closestfish2)
            randomfish.append(closestfish3)
                               
            closestfish = choice(randomfish)

        self.closefish = closestfish
        return (closestfish)
        

    def sharkeat(self, fishx, fishy):

        if self.xpos == fishx and self.ypos == fishy:
            return (True)
        else:
            return (False)
