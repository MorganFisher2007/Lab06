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
        self.win.setCoords(0.5, 12.5, 10.5, 0.5)  # Set coords to 10x10 grid
        # Offset coordinates to allow coordinates to be within boxes
        self.win.setBackground("dodger blue")
        # Draw a rectangle at the bottom as a background
        self.background = Rectangle(Point(0.5, 12.5), Point(10.5, 10.5))
        background_color = "wheat"
        self.background.setFill(background_color)
        self.background.setOutline(background_color)
        self.background.draw(self.win)
        # Draw grid
        for row in range(10):  # Nine rows
            for column in range(10):  # Nine columns
                # Draw rectangles + offset to set pts within boxes
                Rectangle(Point(row + 0.5, column + 0.5), Point(row + 1.5, column + 1.5)).draw(self.win)

    def redraw(self, width, height):
        "Essentially draws a new window -- second initialization"
        self.win = GraphWin("Water World", width, height)
        self.win.setCoords(0.5, 12.5, 10.5, 0.5)  # Set coords to 10x10 grid + space
        # Offset coordinates to allow coordinates to be within boxes
        self.win.setBackground("dodger blue")
        # Draw a rectangle at the bottom as a background
        self.background = Rectangle(Point(0.5, 12.5), Point(10.5, 10.5))
        background_color = "wheat"
        self.background.setFill(background_color)
        self.background.setOutline(background_color)
        self.background.draw(self.win)
        # Draw grid
        for row in range(10):  # Nine rows
            for column in range(10):  # Nine columns
                # Draw rectangles + offset to set pts within boxes
                Rectangle(Point(row + 0.5, column + 0.5), Point(row + 1.5, column + 1.5)).draw(self.win)
        
    def fish_input(self):
        "Gather fish inputs on GUI"
        self.fish_instruction = Text(Point(5.25, 12.3), "Enter comma separated coordinates 'x,y', click to enter each, and press start")
        self.fish_instruction.draw(self.win)

        # Fish1
        self.label_fish1 = Text(Point(1.5, 12), "Fish1 Coords:")
        self.label_fish1.draw(self.win)
        self.entry_fish1 = Entry(Point(1.5, 11.5), 10)
        self.entry_fish1.draw(self.win)
        self.win.getMouse() # Ask for click before locking in entry
        self.text_fish1_coord = self.entry_fish1.getText()

        # Fish2
        self.label_fish2 = Text(Point(3, 12), "Fish2 Coords:")
        self.label_fish2.draw(self.win)
        self.entry_fish2 = Entry(Point(3, 11.5), 10)
        self.entry_fish2.draw(self.win)
        self.win.getMouse()
        self.text_fish2_coord = self.entry_fish2.getText()

        # Fish 3
        self.label_fish3 = Text(Point(4.5, 12), "Fish3 Coords:")
        self.label_fish3.draw(self.win)
        self.entry_fish3 = Entry(Point(4.5, 11.5), 10)
        self.entry_fish3.draw(self.win)
        self.win.getMouse()
        self.text_fish3_coord = self.entry_fish3.getText()

        # Draw start/move and quit button
        self.move_button = Button(Point(7, 11.7), 1.5, 0.5, "Start")
        self.quit_button = Button(Point(9, 11.7), 1.5, 0.5, "Quit")
        self.move_button.activate()
        self.quit_button.activate()
        self.move_button.draw(self.win)
        self.quit_button.draw(self.win)

    def undraw(self):
        "Undraws all GUI objects"
        self.background.undraw()
        self.fish_instruction.undraw()
        self.label_fish1.undraw()
        self.entry_fish1.undraw()
        self.label_fish2.undraw()
        self.entry_fish2.undraw()
        self.label_fish3.undraw()
        self.entry_fish3.undraw()
        self.move_button.undraw()
        self.quit_button.undraw()
        self.play_again_button.undraw()
        
    def clean_fish_coords(self):
        "Splits fish coord inputs into x and y ints"
        # Set fish coord values
        fish1_coord = self.text_fish1_coord.split(",")
        fish2_coord = self.text_fish2_coord.split(",")
        fish3_coord = self.text_fish3_coord.split(",")

        # Convert fish1_coord to integers
        self.fish1_coord_x = int(fish1_coord[0])
        self.fish1_coord_y = int(fish1_coord[1])

        # Convert fish2_coord to integers
        self.fish2_coord_x = int(fish2_coord[0])
        self.fish2_coord_y = int(fish2_coord[1])

        # Convert fish3_coord to integers
        self.fish3_coord_x = int(fish3_coord[0])
        self.fish3_coord_y = int(fish3_coord[1])

    def get_fish1_coord(self):
        "Returns entire fish1 coord for reference in main"
        return self.entry_fish1.getText()

    def get_fish2_coord(self):
        "Returns entire fish2 coord for reference in main"
        return self.entry_fish2.getText()

    def get_fish3_coord(self):
        "Returns entire fish3 coord for reference in main"
        return self.entry_fish3.getText()

    def switch_move_label(self):
        "Change move button label between move shark and fish"
        if self.move_button.getLabel() == "Start":
            self.move_button.setLabel("Move Fish")
        elif self.move_button.getLabel() == "Move Shark":
            self.move_button.setLabel("Move Fish")
        elif self.move_button.getLabel() == "Move Fish":
            self.move_button.setLabel("Move Shark")

    def check_fish_input(self, fish1, fish2, fish3):
        "Handles input validation for fish coord inputs"
        # Check if fish entry is valid
        # Returns reason for invalid
        text_inputs = [fish1, fish2, fish3]
        scanned_inputs = []  # List for processed inputs
        invalid_inputs = []  # List for invalid inputs
        error = False # Set default error
        for inpt in text_inputs:  # For each input, check if valid
            if inpt in scanned_inputs:  # Check for duplicate inputs
                # Raise error
                error = True
                # Append to invalid inputs
                invalid_inputs.append(inpt + " (cannot input duplicate coords)")
            elif len(inpt) != 3:  # Check length is 3 for coord
                if len(inpt) == 4:
                    if inpt[1] != "," and inpt[2] != ",": # Check for commas, else raise error
                        error = True
                        invalid_inputs.append(inpt + " (commas)")
                    elif inpt[2:4] != "10": # Check y range is restricted to 10 (0,10) vs (0,11)
                        error = True
                        invalid_inputs.append(inpt + " (incorrect range)")
                        # Append to invalid inputs
                    elif inpt[0:2] != "10": # Check x range is restricted to 10 (10,0) vs (11,0)
                        invalid_inputs.append(inpt + " (incorrect range)")
                    elif inpt[0:2] == "0," or inpt[2:4] == ",0": # Check for zeroes (not in range)
                        error = True
                        invalid_inputs.append(inpt + " (no zeroes)")
                elif len(inpt) > 3 or len(inpt) < 3: # Check length is greater or less than 3 -- not (m,n)
                    if len(inpt) != 4 or len(inpt) != 5: # Check length is not 4 or 5 (10,10) or (10,0)
                        error = True
                        invalid_inputs.append(inpt + " (incorrect length)")
            elif len(inpt) == 3: # Check length is three
                if inpt[0:2] == "0," or inpt[1:3] == ",0": # Check for zeroes
                        error = True
                        invalid_inputs.append(inpt + " (no zeroes)")
                elif inpt == "7,2": # Check input doesn't not matching shark
                    error = True
                    invalid_inputs.append(inpt + " (fish coords match shark)")
                elif inpt[1] != ",": # Check it's m,n and not mnm
                    error = True
                    invalid_inputs.append(inpt + " (commas)")
                
            elif not inpt[0].isdigit() or not inpt[2].isdigit():
                # Check if x and y are numbers
                error = True
                invalid_inputs.append(inpt + " (is not a number)")
            scanned_inputs.append(inpt)

        if error:  # If invalid, change instruction text
            self.fish_instruction.setText("Invalid Input: " + str(invalid_inputs) + " Click anywhere to restart game")
            self.win.getMouse() # Pause for click
            self.win.close() # Close window, main restarts
            return True
        else:
            return False

    def get_click(self):
        "Check for a click on move/quit button"
        while True: # Central click loop
            click = self.win.getMouse()
            if self.move_button.clicked(click): # If play button clicked
                if self.move_button.getLabel() == "Move Shark": # Check if shark move 
                    return "sharkmove"  # Return string "Shark Move" for use in main
                elif self.move_button.getLabel() == "Move Fish": # Check if fish move
                    return "fishmove"  # Return string "Fish Move" for future toggle use
                else:  # All tests passed
                    self.fish_instruction.setText("Click move to move the shark or fish, or quit to quit the game")
                    # Change move button label
                    self.move_button.setLabel("Move Fish")
                    # Return start
                    return "start"

            # If quit button clicked then quit
            if self.quit_button.clicked(click):
                self.win.close()
                return "close"

    def restart_move(self):
        "Reset move button to Start for repitition of game loop"
        self.move_button.undraw()
        self.move_button.setLabel("Start")
        self.move_button.draw(self.win)
        self.move_button.activate()

    def game_over(self, winner):
        "Sets instruction text for endgame and restarts move button"
        self.fish_instruction.setText(winner)
        self.move_button.setLabel("Start")
        # Clear text boxes
        self.entry_fish1.setText("")
        self.entry_fish2.setText("")
        self.entry_fish3.setText("")

    def again_button(self):
        "Draws play again button in center screen for user to restart game"
        self.play_again_button = Button(Point(5.5, 7), 1.5, 0.5, "Play")
        self.play_again_button.activate()
        self.play_again_button.draw(self.win)

    def death_message(self, name):
        "Change text to a death message so user knows what fish died"
        self.fish_instruction.setText(name + " just died")
