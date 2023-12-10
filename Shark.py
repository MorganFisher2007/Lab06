from random import *
from math import *

class Shark:

    def __init__(self, xpos, ypos):

        self.xpos = xpos
        self.ypos = ypos
        self.closefishx = -1
        self.closefishy = -1
        self.image = "shark-facing-north-clear.png"
    
    def get_x_pos(self):
        return self.xpos

    def get_y_pos(self):
        return self.ypos

    def setsharkpos(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

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

        
    def closestfish(self, fish1x, fish1y, fish2x, fish2y, fish3x, fish3y):

        helperformula1 = (fish1x - self.xpos)**2 + (fish1y - self.ypos)**2
        helperformula2 = (fish2x - self.xpos)**2 + (fish2y - self.ypos)**2
        helperformula3 = (fish3x - self.xpos)**2 + (fish3y - self.ypos)**2
        
        distfish1 = sqrt(float(helperformula1))
        distfish2 = sqrt(float(helperformula2))
        distfish3 = sqrt(float(helperformula3))

        xcoordslist = [distfish1, distfish2]
        ycoordslist = []

        if distfish1 < distfish2 and distfish1 < distfish3:
            self.closestfishx = fish1x
            self.closestfishy = fish1y
        
        elif distfish2 < distfish1 and distfish2 < distfish3:
            self.closestfishx = fish2x
            self.closestfishy = fish2y
            
        elif distfish3 < distfish1 and distfish3 < distfish2:
            self.closestfishx = fish3x
            self.closestfishy = fish3y

        #elif distfish1 == distfish2 and distfish1 < distfish3:
         #   xcoordslist.append(fish1x)
          #  xcoordslist.append(fish2x)
           # ycoordslist.append(fish1y)
            #ycoordslist.append(fish2y)
                               
            #closestfishx = choice(xcoordslist)
            #closestfishy = choice(ycoordslist)

        return (self.closestfishx, self.closestfishy)
        

    def sharkeat(self, fishx, fishy):

        if self.xpos == fishx and self.ypos == fishy:
            return (True)
        else:
            return (False)