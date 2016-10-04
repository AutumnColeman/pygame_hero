import pygame
import time
import random

# KEY_UP = 273
# KEY_DOWN = 274
# KEY_LEFT = 276
# KEY_RIGHT = 275

class Monster(object):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed_x = 5
        self.speed_y = 0
        self.image = pygame.image.load('images/monster.png')
        self.time_till_dir_change = None

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x > width:
            self.x = 0
        if self.y > height:
            self.y = 0
        if self.x < 0:
            self.x = width
        if self.y < 0:
            self.y = height

        self.maybe_change_direction()

    def maybe_change_direction(self):
        if self.time_till_dir_change is None:
            now = time.time()
            self.time_till_dir_change = now + 1
            return

        now = time.time()

        if now >= self.time_till_dir_change:
            self.time_till_dir_change = now + 1
            # perform direction change
            print 'perform direction change'
            num = random.randint(0, 3)
            if num == 0:
                self.speed_x = 0
                self.speed_y = -5
            elif num == 1:
                self.speed_x = 5
                self.speed_y = 0
            elif num == 2:
                self.speed_x = 0
                self.speed_y = 5
            else:
                self.speed_x = -5
                self.speed_y = 0

class Hero(object):
    def __init__(self):
        self.x = 250
        self.y = 215
        self.speed_x = 2
        self.speed_y = 2
        self.image = pygame.image.load('images/hero.png')
        self.time_till_dir_change = None

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y
        # keeps hero within tree boundaries
        if self.x > 450:
            self.x = 450
        if self.x < 30:
            self.x = 30
        if self.y > 415:
            self.y = 415
        if self.y < 30:
            self.y = 30

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            print "key %r" % event.key # checks to see if key is hit
            if event.key == pygame.K_UP:
                self.speed_y -= 4
            elif event.key == pygame.K_DOWN:
                self.speed_y = 4
            elif event.key == pygame.K_LEFT:
                self.speed_x -= 4
            elif event.key == pygame.K_RIGHT:
                self.speed_x = 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.speed_y -= 0
            elif event.key == pygame.K_DOWN:
                self.speed_y = 0
            elif event.key == pygame.K_LEFT:
                self.speed_x -= 0
            elif event.key == pygame.K_RIGHT:
                self.speed_x = 0


def main():
    # declare the size of the canvas
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    # initialize the pygame framework
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    background_image = pygame.image.load('images/background.png')
    hero_image = pygame.image.load('images/hero.png')
    hero = Hero()
    # hero_x = 250
    # hero_y = 200
    # hero_speed_x = 3
    # hero_speed_y = 0
    monster = Monster()



    # game loop
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            # moves the hero with arrow keys
            # if event.type == pygame.KEYDOWN:
            #     print "key %r" % event.key # checks to see if key is hit
            #     if event.key == pygame.K_UP:
            #         hero_speed_y -= 4
            #     elif event.key == pygame.K_DOWN:
            #         hero_speed_y = 4
            #     elif event.key == pygame.K_LEFT:
            #         hero_speed_x -= 4
            #     elif event.key == pygame.K_RIGHT:
            #         hero_speed_x = 4
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_UP:
            #         hero_speed_y -= 0
            #     elif event.key == pygame.K_DOWN:
            #         hero_speed_y = 0
            #     elif event.key == pygame.K_LEFT:
            #         hero_speed_x -= 0
            #     elif event.key == pygame.K_RIGHT:
            #         hero_speed_x = 0
            hero.move(event)

            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        monster.update(width, height)
        hero.update(width, height)
        # hero_x += hero_speed_x
        # hero_y += hero_speed_y
        # # keeps hero within tree boundaries
        # if hero_x > 450:
        #     hero_x = 450
        # if hero_x < 30:
        #     hero_x = 30
        # if hero_y > 415:
        #     hero_y = 415
        # if hero_y < 30:
        #     hero_y = 30

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        screen.blit(background_image, (0, 0))

        screen.blit(hero_image, (hero.x, hero.y))
        screen.blit(monster.image, (monster.x, monster.y))

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
