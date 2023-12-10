# Button
from graphics import *

class Button:
    "Button class creates button"
    def __init__(self,center,width,height,label):
        self.buttonCenter = center
        self.buttonWidth = width
        self.buttonHeight = height
        self.buttonLabel = label

        self.p1y = center.getY() + .5 * height
        self.p1x = center.getX() + .5 * width
        self.p2y = center.getY() - .5 * height
        self.p2x = center.getX() - .5 * width

        self.outline = Rectangle(Point(self.p1x,self.p1y),Point(self.p2x,self.p2y))

        self.label = Text(center,label)

        self.deactivate()

    def draw(self,win):
        "Draws Button on graphics window"
        self.outline.draw(win)
        self.label.draw(win)

    def undraw(self):
        "Removes Button from graphics window"
        self.deactivate()
        self.outline.undraw()
        self.label.undraw()

    def activate(self):
        "Primes Button to recieve clicks"
        self.active = True
        self.wasClicked = False
        self.label.setFill("black")
        self.label.setStyle("normal")
        self.outline.setFill("LightBlue")
        self.outline.setWidth(2)

    def deactivate(self):
        "Prevents Button from reacting to clicks"
        self.active = False
        self.label.setFill("grey")
        self.label.setStyle("italic")
        self.outline.setFill("grey89")
        self.outline.setWidth(1)

    def setLabel(self,label):
        "Labels Button"
        self.label.setText(label)

    def getLabel(self):
        "Accessor for Button Label"
        return self.label.getText()

    def clicked(self, point):
        "Test if Button was clicked"
        if self.wasClicked == False:
            if self.p2x <= point.getX() <= self.p1x:
                if self.p2y <= point.getY() <= self.p1y:
                    if self.active == True:
                        self.wasClicked = False
                        return True
    def reset(self):
        "resets button values"
        self.wasClicked = False
