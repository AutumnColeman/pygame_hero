# Catch the Monster Game
#
# You will make a game in which the hero wins by catching the monster, while having to avoid the goblins. You will make use of object-oriented programming to make your life easier, but how and when will you use it? You will encounter a series of OOP Choice Points - where you can make the decision about whether to convert some code to OOP or not. Use your own judgement, there are no wrong choices.
import pygame, random, time



# class Monster(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.speed_x = 5
#         self.speed_y = 5
#
#
#     # def update()
#     def render(self):
#         screen.blit(monster, (150, 150))


def main():
    # declare the size of the canvas
    width = 510
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
    #background image
    background_image = pygame.image.load('images/background.png').convert_alpha()
    #sprite characters
    hero = pygame.image.load('images/hero.png').convert_alpha()
    monster = pygame.image.load('images/monster.png').convert_alpha()
    monster_x = 50
    monster_y = 50
    goblin = pygame.image.load('images/goblin.png').convert_alpha()
    # game loop
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        ######################################
        #moves the monster right and off screen
        # while time < 120:
        monster_x += random.randint()
        monster_y += random.randint()
        if monster_x > width:
            monster_x = 0

        # fill background color
        screen.fill(blue_color)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        #renders background image
        screen.blit(background_image, (0, 0))

        #renders sprites
        screen.blit(hero, (250, 200))
        screen.blit(monster, (monster_x, monster_y)),
        screen.blit(goblin, (350, 350))

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
