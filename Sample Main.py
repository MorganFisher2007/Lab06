from Real_Window import Window
from Button import Button
from Fish import Fish
from Shark import Shark
from graphics import *


def main():

    window = Window(700, 700)

    
    fish1coord = window.get_fish1_coord()
    fish2coord = window.get_fish2_coord()
    fish3coord = window.get_fish3_coord()

    if window.check_fish_input(fish1coord, fish2coord, fish3coord) == False:   
    
        stalemate = False  # initialize stalemate variable
        turns = 0  # initialize turncounter
    
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
    
        Fish1 = Fish(window.fish1_coord_x, window.fish1_coord_y, fish1_images)
        Fish2 = Fish(window.fish2_coord_x, window.fish2_coord_y, fish2_images)
        Fish3 = Fish(window.fish3_coord_x, window.fish3_coord_y, fish3_images)
    
        Fish1.update_image()
        Fish1_image = Image(Point(window.fish1_coord_x, window.fish1_coord_y), Fish1.image)
        Fish1_image.draw(window.win)
    
        Fish2.update_image()
        Fish2_image = Image(Point(window.fish2_coord_x, window.fish2_coord_y), Fish2.image)
        Fish2_image.draw(window.win)
    
        Fish3.update_image()
        Fish3_image = Image(Point(window.fish3_coord_x, window.fish3_coord_y), Fish3.image)
        Fish3_image.draw(window.win)
    
        shark = Shark(7, 2)
        shark_image = Image(Point(shark.xpos, shark.ypos), shark.image)
        shark_image.draw(window.win)
    
        # if all fish aren't alive, or stalemate, loop stops
        while True:
            value = window.get_click()
    
            if value == "start":
                window.toggle_move_label()
    
            if value == "fishmove":
                # move each fish (movement function takes care of determining direction
                # d is returned point of where Fish1 will move to
                if not Fish1.dead:
                    Fish1_initial_coord_x = window.fish1_coord_x
                    Fish1_initial_coord_y = window.fish1_coord_y
                    Fish1.move(window.fish2_coord_x, window.fish2_coord_y, window.fish3_coord_x, window.fish3_coord_y, shark.get_x_pos(), shark.get_y_pos())
                    Fish1_image.undraw()
                    Fish1_image.move((Fish1.get_x_pos() - Fish1_initial_coord_x), (Fish1.get_y_pos() - Fish1_initial_coord_y))
                    Fish1_image.draw(window.win)
    
                if not Fish2.dead:
                    Fish2_initial_coord_x = window.fish2_coord_x
                    Fish2_initial_coord_y = window.fish2_coord_y
                    Fish2.move(window.fish1_coord_x, window.fish1_coord_y, window.fish3_coord_x, window.fish3_coord_y, window.fish2_coord_x, window.fish2_coord_x)
                    Fish2_image.undraw()
                    Fish2_image.move((window.fish2_coord_x - Fish2_initial_coord_x), (window.fish2_coord_y - Fish2_initial_coord_y))
                    Fish2_image.draw(window.win)
    
                if not Fish3.dead:
                    Fish3_initial_coord_x = window.fish3_coord_x
                    Fish3_initial_coord_y = window.fish3_coord_y
                    Fish3.move(window.fish1_coord_x, window.fish1_coord_y, window.fish2_coord_x, window.fish2_coord_y, window.fish3_coord_x, window.fish3_coord_x)
                    Fish3_image.undraw()
                    Fish3_image.move((window.fish3_coord_x - Fish3_initial_coord_x), (window.fish3_coord_y - Fish3_initial_coord_y))
                    Fish3_image.draw(window.win)
                window.win.getMouse()
                
                window.toggle_move_label()  # change label to 'MOVE SHARK'
    
            if value == "sharkmove":
                # Update shark coords
                shark_initial_coord_x = shark.xpos
                shark_initial_coord_y = shark.ypos
                closefishx, closefishy = shark.closestfish(window.fish3_coord_x, window.fish3_coord_y, window.fish2_coord_x, window.fish2_coord_y, window.fish1_coord_x, window.fish1_coord_y) 
                shark.move(closefishx, closefishy)
                shark_image.undraw()
                shark_image.move((shark.xpos - shark_initial_coord_x), (shark.ypos - shark_initial_coord_y))
                shark_image.draw(window.win)
                # everytime shark moves, count it as a turn
                turns += 1
    
                if turns > 20:  # at 20 turns
                    stalemate = True
    
                window.win.getMouse()
            
                window.toggle_move_label()
    
            sharkpos = Point(shark.get_x_pos(), shark.get_y_pos())
            Fish1pos = Point(Fish1.get_x_pos(), Fish1.get_y_pos())
            Fish2pos = Point(Fish2.get_x_pos(), Fish2.get_y_pos())
            Fish3pos = Point(Fish3.get_x_pos(), Fish3.get_y_pos())
    
            if Fish1.test_dead() == False and shark.get_x_pos() == Fish1.get_x_pos() and shark.get_y_pos() == Fish1.get_y_pos():
                Fish1.die()
                window.death_message("Fish 1")  # also display that fish is dead
            elif Fish2.test_dead() == False and shark.get_x_pos() == Fish2.get_x_pos() and shark.get_y_pos() == Fish2.get_y_pos():
                Fish2.die()
                window.death_message("Fish 2")
            elif Fish3.test_dead() == False and shark.get_x_pos() == Fish3.get_x_pos() and shark.get_y_pos() == Fish3.get_y_pos():
                Fish3.die()
                window.death_message("Fish 3")
    
            # game meets end conditions, reset
            if stalemate or (Fish1.test_dead() and Fish2.test_dead() and Fish3.test_dead()) == True:
                if stalemate:
                    window.game_over("Stalemate.")
                    stalemate = False
                else:
                    window.game_over("Shark wins.")
    
                turns = 0  # reset stalemate turn counter
    
                if not Fish1.test_dead():
                    Fish1.revive()
    
                if not Fish2.test_dead():
                    Fish2.revive()
    
                if not Fish3.test_dead():
                    Fish3.revive() # Need to code fish revive class method
    
                window.play_again_label()
    
                window.toggle_move_label()
    
                # Run main once more
                if window.play == True:
                    continue

main()
