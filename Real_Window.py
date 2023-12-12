# Jack Flynn
# Window Class
from graphics import *
from Button import *
import random

class Window:
    "Handles the drawing and redrawing of the grid"
    def __init__(self, width, height):
        "Initial setup of inputs and grid"
        self.win = GraphWin("Water World", width, height)
        self.win.setCoords(0.5, 12.5, 10.5, 0.5)  # Set coords to 10x10 grid + space
        # Offset coordinates to allow coordinates to be within boxes
        self.win.setBackground("blue")
        # Draw a rectangle at the bottom as a background
        back = Rectangle(Point(0.5, 12.5), Point(10.5, 10.5))
        background_color = "lightskyblue"
        back.setFill(background_color)
        back.setOutline(background_color)
        back.draw(self.win)
        # Draw grid
        for row in range(10):  # Nine rows
            for column in range(10):  # Nine columns
                # Draw rectangles + offset to set pts within boxes
                Rectangle(Point(row + 0.5, column + 0.5), Point(row + 1.5, column + 1.5)).draw(self.win)

        # Draw fish inputs
        self.fish_instruction = Text(Point(5.25, 12.3), "Enter comma separated coordinates 'x,y', click to enter each, and press start")
        self.fish_instruction.draw(self.win)
        self.label_fish1 = Text(Point(1.5, 12), "Fish1 Coords:")
        self.label_fish1.draw(self.win)
        self.entry_fish1 = Entry(Point(1.5, 11.5), 10)
        self.entry_fish1.draw(self.win)
        self.win.getMouse()
        text_fish1_coord = self.entry_fish1.getText()

        self.label_fish2 = Text(Point(3, 12), "Fish2 Coords:")
        self.label_fish2.draw(self.win)
        self.entry_fish2 = Entry(Point(3, 11.5), 10)
        self.entry_fish2.draw(self.win)
        self.win.getMouse()
        text_fish2_coord = self.entry_fish2.getText()

        self.label_fish3 = Text(Point(4.5, 12), "Fish3 Coords:")
        self.label_fish3.draw(self.win)
        self.entry_fish3 = Entry(Point(4.5, 11.5), 10)
        self.entry_fish3.draw(self.win)
        self.win.getMouse()
        text_fish3_coord = self.entry_fish3.getText()
        
        # Set fish coord values
        fish1_coord = text_fish1_coord.split(",")
        fish2_coord = text_fish2_coord.split(",")
        fish3_coord = text_fish3_coord.split(",")

        # Convert fish1_coord to integers
        self.fish1_coord_x = int(fish1_coord[0])
        self.fish1_coord_y = int(fish1_coord[1])

        # Convert fish2_coord to integers
        self.fish2_coord_x = int(fish2_coord[0])
        self.fish2_coord_y = int(fish2_coord[1])

        # Convert fish3_coord to integers
        self.fish3_coord_x = int(fish3_coord[0])
        self.fish3_coord_y = int(fish3_coord[1])

        # Draw start/move and quit button
        self.move_button = Button(Point(7, 11.7), 1.5, 0.5, "Start")
        self.quit_button = Button(Point(9, 11.7), 1.5, 0.5, "Quit")
        self.move_button.activate()
        self.quit_button.activate()
        self.move_button.draw(self.win)
        self.quit_button.draw(self.win)
                
    def get_win(self):
        "Returns window for reference in main function"
        return self.win

    def move(self, obj, initial_pt, final_pt):
        "Move fish/shark object"
        # Move in relation to target point
        obj.move(final_pt.getX() - initial_pt.getX(), final_pt.getY() - initial_pt.getY())
        obj.set_pos(final_pt)
        return obj

    def get_click(self):
        """Check for a click on single button
            If start button pressed, returns list of inputs
            If move button pressed, returns string for analysis"""
        while True:
            click = self.win.getMouse()
            if self.move_button.clicked(click):
                if self.move_button.getLabel() == "Move Shark":
                    return "sharkmove"  # Return string "Shark Move" for future toggle use
                elif self.move_button.getLabel() == "Move Fish":
                    return "fishmove"  # Return string "Fish Move" for future toggle use

                # Check if fish entry is valid
                # Code for if it is the first move (start move)
                elif self.move_button.getLabel() == "Start":  # if first move
                    while True:
                        # Return fish coords or prompt invalid coords
                        invalid_flag = False
                        # Input validation
                        text_inputs = [self.entry_fish1.getText(), self.entry_fish2.getText(), self.entry_fish3.getText()]
                        scanned_inputs = [] # List for processed inputs
                        invalid_inputs = [] # List for invalid inputs
                        for inpt in text_inputs:  # For each input, check if valid
                            if inpt in scanned_inputs: # Boolean algebra to check all input
                                invalid_flag = True
                                # Append to invalid inputs
                                invalid_inputs.append(inpt + " (exists)")
                                scanned_inputs.append(inpt)  # Append to processed inputs
                                continue
                            elif len(inpt) != 3:  # Check length is 3 for coord
                                invalid_flag = True
                                # Append to invalid inputs
                                invalid_inputs.append(inpt + " (bad format)")
                                scanned_inputs.append(inpt)  # App to scanned
                            elif not (inpt[0].isdigit() and inpt[2].isdigit()):
                                # Check if x and y are numbers
                                invalid_flag = True
                                invalid_inputs.append(inpt + " (not number)")
                                scanned_inputs.append(inpt)  # App to scanned
                            else:  # Valid input
                                scanned_inputs.append(inpt)

                        if invalid_flag == True:  # If invalid, change instruction text
                            self.fish_instruction.setText("BAD INPUT: " + str(invalid_inputs))
                        else:  # All tests passed
                            self.fish_instruction.setText("Click move to move the shark or fish, or quit to quit the game")
                            # Change move button label
                            self.move_button.setLabel("Move Fish")
                            # Return start
                            return "start"

            # If quit button clicked then quit
            if self.quit_button.clicked(click):
                self.win.close()
                quit()

    def game_over(self, winner):
        "Prompt to play again"
        self.fish_instruction.setText(winner + " Enter comma separated coordinates 'x,y' and press start to try again.")
        self.move_button.setLabel("Start")
        # Clear text boxes
        self.entry_fish1.setText("")
        self.entry_fish2.setText("")
        self.entry_fish3.setText("")

    def toggle_move_label(self):
        "Change move button label between move shark and fish"
        if self.move_button.getLabel() == "Start":
            self.move_button.setLabel("Move Fish")
        elif self.move_button.getLabel() == "Move Shark":
            self.move_button.setLabel("Move Fish")
        elif self.move_button.getLabel() == "Move Fish":
            self.move_button.setLabel("Move Shark")

    def play_again_label(self):
        "Add a play again button"
        self.play_again_button = Button(Point(4.5, 5.5), 2, 1, "Play Again")
        self.play_again_button.activate()
        self.play_again_button.draw(self.win)
        self.win.getMouse()
        if self.play_again_button.clicked:
            self.play = True

    def death_message(self, name):
        "Change text to a death message"
        self.fish_instruction.setText(name + " just died")

    def drawfish(self, x, y, imageFile):
        "Draws fish"
        self.image = Image(Point(x, y), imageFile)
        self.image.draw(self.win)

    def drawfish2(self, x, y, imageFile):
        "Draws fish 2"
        self.image = Image(Point(x, y), imageFile)
        self.image.draw(self.win)

    def drawfish3(self, x, y, imageFile):
        "Draws fish 3"
        self.image = Image(Point(x, y), imageFile)
        self.image.draw(self.win)

    def undrawfish(self, imageObject):
        imageObject.undraw()

    def get_image(self):
        return self.image

    def drawshark(self, x, y):
        self.shark = Image(Point(x, y), "image file name")

    def undrawshark(self):
        self.shark.undraw()
