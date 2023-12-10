from Real_Window import Window
from graphics import *
from Sharkk import Shark
from Fish import Fish

def shark_draw(win, point, direction):
    if direction == "left":
        shark_image_left = Image(point, "Shark-facing-west-clear.png")
        shark_image_left.draw(win)
    if direction == "up":
        shark.image_up = Image(point, "Shark-facing-north-clear.png")
    if direction == "right":
        shark.image_right = Image(point, "Shark-facing-east-clear.png")
    if direction == "down":
        shark.image_down = Image(point, "Shark-facing-south-clear.png")

def fish_draw(win, point, number, direction, disposition):
    if number == 1:
        if direction == "left":
            if disposition == "angry":
                fish_image_left = Image(point, "Fish1-facing-west-angry.png")
                fish_image_left.draw(win)
            if disposition == "calm":
                fish_image_left = Image(point, "Fish1-facing-west-calm.png")
                fish_image_left.draw(win)
        if direction == "up":
            if disposition == "angry":
                fish_image_up = Image(point, "Fish1-facing-north-angry.png")
                fish_image_up.draw(win)
            if disposition == "calm":
                fish_image_up = Image(point, "Fish1-facing-north-calm.png")
                fish_image_up.draw(win)
        if direction == "right":
            if disposition == "angry":
                fish_image_right = Image(point, "Fish1-facing-east-angry.png")
                fish_image_right.draw(win)
            if disposition == "calm":
                fish_image_right = Image(point, "Fish1-facing-east-calm.png")
                fish_image_right.draw(win)
        if direction == "down":
            if disposition == "angry":
                fish_image_down = Image(point, "Fish1-facing-south-angry.png")
                fish_image_down.draw(win)
            if disposition == "calm":
                fish_image_down = Image(point, "Fish1-facing-west-calm.png")
                fish_image_down.draw(win)

    if number == 2:
        if direction == "left":
            if disposition == "angry":
                fish_image_left = Image(point, "Fish2-facing-west-angry.png")
                fish_image_left.draw(win)
            if disposition == "calm":
                fish_image_left = Image(point, "Fish2-facing-west-calm.png")
                fish_image_left.draw(win)
        if direction == "up":
            if disposition == "angry":
                fish_image_up = Image(point, "Fish2-facing-north-angry.png")
                fish_image_up.draw(win)
            if disposition == "calm":
                fish_image_up = Image(point, "Fish2-facing-north-calm.png")
                fish_image_up.draw(win)
        if direction == "right":
            if disposition == "angry":
                fish_image_right = Image(point, "Fish2-facing-east-angry.png")
                fish_image_right.draw(win)
            if disposition == "calm":
                fish_image_right = Image(point, "Fish2-facing-east-calm.png")
                fish_image_right.draw(win)
        if direction == "down":
            if disposition == "angry":
                fish_image_down = Image(point, "Fish2-facing-south-angry.png")
                fish_image_down.draw(win)
            if disposition == "calm":
                fish_image_down = Image(point, "Fish2-facing-west-calm.png")
                fish_image_down.draw(win)

    if number == 3:
        if direction == "left":
            if disposition == "angry":
                fish_image_left = Image(point, "Fish3-facing-west-angry.png")
                fish_image_left.draw(win)
            if disposition == "calm":
                fish_image_left = Image(point, "Fish3-facing-west-calm.png")
                fish_image_left.draw(win)
        if direction == "up":
            if disposition == "angry":
                fish_image_up = Image(point, "Fish3-facing-north-angry.png")
                fish_image_up.draw(win)
            if disposition == "calm":
                fish_image_up = Image(point, "Fish3-facing-north-calm.png")
                fish_image_up.draw(win)
        if direction == "right":
            if disposition == "angry":
                fish_image_right = Image(point, "Fish3-facing-east-angry.png")
                fish_image_right.draw(win)
            if disposition == "calm":
                fish_image_right = Image(point, "Fish3-facing-east-calm.png")
                fish_image_right.draw(win)
        if direction == "down":
            if disposition == "angry":
                fish_image_down = Image(point, "Fish3-facing-south-angry.png")
                fish_image_down.draw(win)
            if disposition == "calm":
                fish_image_down = Image(point, "Fish3-facing-west-calm.png")
                fish_image_down.draw(win)

# Set Window Class
window = Window(800, 800)
window.get_click()

# Set Shark Class
game_shark = Shark(7, 2)

# Set Fish1 Class
fish1 = Fish(window.fish1_coord_x, window.fish1_coord_y)
fish_draw(window.win, Point(window.fish1_coord_x, window.fish1_coord_y), 1, "west", "angry")
fish2 = Fish(window.fish2_coord_x, window.fish2_coord_y)
fish_draw(window.win, Point(window.fish2_coord_x, window.fish2_coord_y), 2, "west", "angry")
fish3 = Fish(window.fish3_coord_x, window.fish3_coord_y)
fish_draw(window.win, Point(window.fish3_coord_x, window.fish3_coord_y), 3, "west", "angry")


# Draw window
