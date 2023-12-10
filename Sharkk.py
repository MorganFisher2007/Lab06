
from math import *

class Shark:

    def __init__(self, xpos, ypos):

        self.xpos = xpos
        self.ypos = ypos
        self.closefishx = -1
        self.closefishy = -1
        

    def setsharkpos(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def getsharkpos(self):
        return (self.xpos, self.ypos)
        

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

        elif closefishx - self.xpos >= 2 and closefishy - self.ypos == 1:
            self.xpos += 2
            self.ypos += 2
        elif closefishx - self.xpos >= 2 and closefishy - self.ypos == -1:
            self.xpos += 2
            self.ypos -= 2
        elif closefishx - self.xpos <= -2 and closefishy - self.ypos == 1:
            self.xpos -= 2
            self.ypos += 2
        elif closefishx - self.xpos <= -2 and closefishy - self.ypos == -1:
            self.xpos -= 2
            self.ypos -= 2
            
        elif closefishx - self.xpos == 1 and closefishy - self.ypos >= 2:
            self.xpos += 2
            self.ypos += 2
        elif closefishx - self.xpos == -1 and closefishy - self.ypos >= 2:
            self.xpos -= 2
            self.ypos += 2
        elif closefishx - self.xpos == 1 and closefishy - self.ypos <= -2:
            self.xpos += 2
            self.ypos -= 2
        elif closefishx - self.xpos == -1 and closefishy - self.ypos <= -2:
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

        return (self.xpos, self.ypos)

        
        

    def closestfish(self, fishx, fishy):

        helperformula = (fishx - self.xpos)**2 + (fishy - self.ypos)**2
        
        distfish = sqrt(helperformula)

        return (distfish)
        

    def sharkeat(self, fishx, fishy):

        if self.xpos == fishx and self.ypos == fishy:
            return (True)
        else:
            return (False)
