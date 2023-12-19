import random

class Fish():
    def __init__(self, x, y, image_list):
        self.x = x
        self.y = y
        self.direction = random.choice(['N', 'S', 'E', 'W']) # random starting direction
        self.flee = False
        self.dead = False
        self.list = image_list

    def undraw(self):
        self.image.undraw()
    
    def set_direction(self, number, win):
        if number == 1:
            self.direction == 'N'
        elif number == 2:
            self.direction == 'S'
        elif number == 3:
            self.direction == 'E'
        elif number == 4:
            self.direction == 'W'

    def test_dead(self):
        if self.dead == True: 
            return True
        else:
            return False

    def revive(self):
        if self.dead == False:
            self.dead == True

    def get_x_pos(self):
        return self.x

    def get_y_pos(self):
        return self.y

    def update_image(self): # assign image from list based on direction & flee mode
        if self.direction == 'N':
            if self.flee == False:
                self.image = self.list[5]
            if self.flee == True:
                self.image = self.list[4]
        elif self.direction == 'S':
            if self.flee == False:
                self.image = self.list[3]
            if self.flee == True:
                self.image = self.list[2]
        elif self.direction == 'E':
            if self.flee == False:
                self.image = self.list[7]
            if self.flee == True:
                self.image = self.list[6]
        elif self.direction == 'W':
            if self.flee == False:
                self.image = self.list[1]
            if self.flee == True:
                self.image = self.list[0]
        
    def die(self):
        self.dead = True
        return True
    
    def move(self, f1x, f1y, f2x, f2y, sx, sy):
        if sx == self.x and sy == self.y:
            self.die()
            return
        
        # x and y components of distance between fish and shark
        dsx = sx-self.x
        dsy = sy-self.y

        if abs(dsx) <= 3 and abs(dsy) <= 3:
            self.flee = True # fish enters flee mode when within 4x4 box centered around shark
        
        if self.flee:
            if abs(dsx) == abs(dsy):
                if random.randint(0, 1) == True: # random choice of direction when distance is equal
                    if dsx > 0:
                        self.direction = 'W'
                    else:
                        self.direction = 'E'
                else:
                    if dsy > 0:
                        self.direction = 'N'
                    else:
                        self.direction = 'S'
            elif abs(dsx) > abs(dsy): # continue case handling to determine direction
                if dsx > 0:
                    self.direction = 'W'
                else:
                    self.direction = 'E'
            else:
                if dsy > 0:
                    self.direction = 'N'
                else:
                    self.direction = 'S'

        # now that direction has been established, fish will attempt to move while also handling flee
        if self.direction == 'N' and self.y == 1:
            if self.flee:
                if [self.x, 10] not in [[f1x, f1y], [f2x, f2y]]: # make sure space not occupied
                    self.y = 10
                    self.flee = False
            else:
                self.direction = 'S' # turns around if facing wall and not in flee mode
            return
        elif self.direction == 'E' and self.x == 10: 
            if self.flee:
                if [1, self.y] not in [[f1x, f1y], [f2x, f2y]]:
                    self.x = 1
                    self.flee = False
            else:
                self.direction = 'W'
            return
        elif self.direction == 'S' and self.y == 10:
            if self.flee:
                if [self.x, 1] not in [[f1x, f1y], [f2x, f2y]]:
                    self.y = 1
                    self.flee = False
            else:
                self.direction = 'N'
            return
        elif self.direction == 'W' and self.x == 1:
            if self.flee:
                if [10, self.y] not in [[f1x, f1y], [f2x, f2y]]:
                    self.x = 10
                    self.flee = False
            else:
                self.direction = 'E'
            return

        # move forward in direction "default move"
        if self.direction == 'N': 
            if [self.x, self.y-1] not in [[f1x, f1y], [f2x, f2y]]:
                self.y -= 1
        elif self.direction == 'E':
            if [self.x+1, self.y] not in [[f1x, f1y], [f2x, f2y]]:
                self.x += 1
        elif self.direction == 'S':
            if [self.x, self.y+1] not in [[f1x, f1y], [f2x, f2y]]:
                self.y += 1
        elif self.direction == 'W':
            if [self.x-1, self.y] not in [[f1x, f1y], [f2x, f2y]]:
                self.x -= 1
