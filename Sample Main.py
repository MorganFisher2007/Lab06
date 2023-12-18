# Import necessary classes and modules
from Real_Window import Window
from Button import Button
from Fish import Fish
from Shark import Shark
from graphics import *

# Initialize a counter for game iterations
counts = 0

def main():
    while True:
        # Counter for stalemate turns
        shark_stomachache_level = 0
        
        # Check if it's the first iteration or not
        if counts >= 1:
            window.redraw(700, 700)
        else:
            window = Window(700, 700)
            game_quit = False

        # Get fish coordinates from user input
        window.fish_input()
        fish1coord = window.get_fish1_coord()
        fish2coord = window.get_fish2_coord()
        fish3coord = window.get_fish3_coord()

        # Check if fish input is valid, if not, clean up coordinates
        if window.check_fish_input(fish1coord, fish2coord, fish3coord) == False and game_quit == False:    
            window.clean_fish_coords()
        
            # Initialize game variables
            stalemate = False
            turns = 0
    
            # Define images for each fish facing different directions
            fish1_images = ["Fish1-facing-west-angry.png", "Fish1-facing-west-calm.png",
                            "Fish1-facing-south-angry.png", "Fish1-facing-south-calm.png",
                            "Fish1-facing-north-angry.png", "Fish1-facing-north-calm.png",
                            "Fish1-facing-east-angry.png", "Fish1-facing-east-calm.png"]
    
            fish2_images = ["Fish2-facing-west-angry.png", "Fish2-facing-west-calm.png",
                            "Fish2-facing-south-angry.png", "Fish2-facing-south-calm.png",
                            "Fish2-facing-north-angry.png", "Fish2-facing-north-calm.png",
                            "Fish2-facing-east-angry.png", "Fish2-facing-east-calm.png"]
    
            fish3_images = ["Fish3-facing-west-angry.png", "Fish3-facing-west-calm.png",
                            "Fish3-facing-south-angry.png", "Fish3-facing-south-calm.png",
                            "Fish3-facing-north-angry.png", "Fish3-facing-north-calm.png",
                            "Fish3-facing-east-angry.png", "Fish3-facing-east-calm.png"]
    
            # Create fish objects and set their initial positions
            Fish1 = Fish(window.fish1_coord_x, window.fish1_coord_y, fish1_images)
            Fish2 = Fish(window.fish2_coord_x, window.fish2_coord_y, fish2_images)
            Fish3 = Fish(window.fish3_coord_x, window.fish3_coord_y, fish3_images)
    
            # Make fish flee if shark is close
            if abs(7 - window.fish1_coord_x) <= 3 and abs(2 - window.fish1_coord_y) <= 3:
                Fish1.flee = True
            Fish1.update_image()
            Fish1_image = Image(Point(Fish1.get_x_pos(), Fish1.get_y_pos()), Fish1.image)
            Fish1_image.draw(window.win)
    
            if abs(7 - window.fish2_coord_x) <= 3 and abs(2 - window.fish2_coord_y) <= 3:
                Fish2.flee = True
            Fish2.update_image()
            Fish2_image = Image(Point(Fish2.get_x_pos(), Fish2.get_y_pos()), Fish2.image)
            Fish2_image.draw(window.win)
    
            if abs(7 - window.fish3_coord_x) <= 3 and abs(2 - window.fish3_coord_y) <= 3:
                Fish3.flee = True
            Fish3.update_image()
            Fish3_image = Image(Point(Fish3.get_x_pos(), Fish3.get_y_pos()), Fish3.image)
            Fish3_image.draw(window.win)
    
            shark = Shark(7, 2)
            shark_image = Image(Point(shark.get_x_pos(), shark.get_y_pos()), shark.image)
            shark_image.draw(window.win)
    
            # Main game loop
            while True:
                value = window.get_click()
    
                if value == "fishmove": # value returned from WWGUI
                    # Move each fish and update their positions and images
                    if not Fish1.dead: # If fish is not dead, update new position
                        Fish1.move(Fish2.get_x_pos(), Fish2.get_y_pos(), Fish3.get_x_pos(), Fish3.get_y_pos(), shark.get_x_pos(), shark.get_y_pos())
                        Fish1_image.undraw() # Redraw image to new fish position
                        Fish1.update_image()
                        Fish1_image = Image(Point(Fish1.get_x_pos(), Fish1.get_y_pos()), Fish1.image)
                        Fish1_image.draw(window.win)
    
                    if not Fish2.dead:
                        Fish2.move(Fish1.get_x_pos(), Fish1.get_y_pos(), Fish3.get_x_pos(), Fish3.get_y_pos(), shark.get_x_pos(), shark.get_y_pos())
                        Fish2_image.undraw()
                        Fish2.update_image()
                        Fish2_image = Image(Point(Fish2.get_x_pos(), Fish2.get_y_pos()), Fish2.image)
                        Fish2_image.draw(window.win)
    
                    if not Fish3.dead:
                        Fish3.move(Fish1.get_x_pos(), Fish1.get_y_pos(), Fish2.get_x_pos(), Fish2.get_y_pos(), shark.get_x_pos(), shark.get_y_pos())
                        Fish3_image.undraw()
                        Fish3.update_image()
                        Fish3_image = Image(Point(Fish3.get_x_pos(), Fish3.get_y_pos()), Fish3.image)
                        Fish3_image.draw(window.win)
                    
                    window.switch_move_label()  # Change label to Move Shark
    
                elif value == "sharkmove": # If WWGUI returns sharkmove value
                    # Update shark coordinates
                    alive_fish_coords = [] # List for alive fish
                    for fish in [Fish1, Fish2, Fish3]: # Iterate over list
                        if fish.dead == False: # If fish not dead, append to list
                            alive_fish_coords.append(fish.get_x_pos())
                            alive_fish_coords.append(fish.get_y_pos())
    
                    closefishx, closefishy = shark.closestfish(*alive_fish_coords) # Chase closest alive fish
                    shark.move(closefishx, closefishy) # Move shark coords
                    shark_image.undraw() # Update shark coord images
                    shark_image = Image(Point(shark.get_x_pos(), shark.get_y_pos()), shark.image)
                    shark_image.draw(window.win)

                    # Every time shark eats, start counting turns
                    if not shark.sharkeat(Fish1.get_x_pos(), Fish1.get_y_pos()) or shark.sharkeat(Fish2.get_x_pos(), Fish2.get_y_pos()) or shark.sharkeat(Fish3.get_x_pos(), Fish3.get_y_pos()):
                        shark_stomachache_level += 1
    
                    if shark_stomachache_level > 20:  # At 10 turns without eaten fish, declare stalemate
                        stalemate = True
                
                    window.switch_move_label()

                elif value == "quit": # Quit button clicked
                    window.win.close() # End it all
                    quit()
    
                # Check if shark has eaten any fish
                sharkpos = Point(shark.get_x_pos(), shark.get_y_pos())
                Fish1pos = Point(Fish1.get_x_pos(), Fish1.get_y_pos())
                Fish2pos = Point(Fish2.get_x_pos(), Fish2.get_y_pos())
                Fish3pos = Point(Fish3.get_x_pos(), Fish3.get_y_pos())
    
                if Fish1.test_dead() == False and shark.get_x_pos() == Fish1.get_x_pos() and shark.get_y_pos() == Fish1.get_y_pos(): # Conditions for fish to be dead are met
                    Fish1.die() # Fish officially dies
                    Fish1_image.undraw() # No more image
                    window.death_message("Fish 1")  # Display that fish is dead
                elif Fish2.test_dead() == False and shark.get_x_pos() == Fish2.get_x_pos() and shark.get_y_pos() == Fish2.get_y_pos():
                    Fish2.die()
                    Fish2_image.undraw()
                    window.death_message("Fish 2")
                elif Fish3.test_dead() == False and shark.get_x_pos() == Fish3.get_x_pos() and shark.get_y_pos() == Fish3.get_y_pos():
                    Fish3.die()
                    Fish3_image.undraw()
                    window.death_message("Fish 3")
    
                # Check if game end conditions are met, reset the game
                if stalemate or (Fish1.test_dead() and Fish2.test_dead() and Fish3.test_dead()) == True:
                    if stalemate:
                        # Display stalemate message and prompt for a new game
                        window.game_over("Stalemate -- Shark perished from malnutrition. Click play to start a new game.")
                        stalemate = False
                    else:
                        # Display Shark victory message and prompt for a new game
                        window.game_over("Shark wins. Go Shark! Click play to start a new game.")
    
                    turns = 0  # Reset stalemate turn counter
    
                    # Inner loop for handling user's decision to play again or quit
                    while True:
                        window.again_button()
                        pt = window.win.getMouse()  # Pause to let the user know the window is about to close
                        if window.play_again_button.clicked(pt): # If play again button clicked
                            window.restart_move() # Reset move button to Start
                            window.win.close() # Close window
                            window.undraw() # Undraw everything on WWGUI
                            shark_image.undraw() # Undraw everything on main
                            Fish1_image.undraw()
                            Fish2_image.undraw()
                            Fish3_image.undraw()
                            break # Break loop to iterate back to original while loop -- restarts everything
                        elif window.quit_button.clicked(pt): # Quit button quits game
                            window.win.close()
                            quit()
                            break
                    break

# Call the main function to start the game
main()
