import pygame
import random

pygame.init()
running = True
screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Vampire Survivor Copy')
bg = pygame.image.load("bg.jpg")

# Player
player_img = pygame.image.load('ship.png')
player_updated = pygame.transform.scale(player_img, (20, 40))

# Enemy
enemy_img = pygame.image.load('ship.png')
enemyX = random.randint(0, 464)
enemyY = random.randint(0, 30)

pygame.display.flip()

# velocity / speed of movement
vel = 2


class Player:
    def __init__(self):
        self.width = 20
        self.height = 40
        self.xpos = 200
        self.ypos = 200

    def create_player(self):
        pygame.draw.rect(self.xpos, self.ypos, self.width, self.height)

    def draw(self):
        screen.blit(player_updated, (self.xpos, self.ypos))


Player = Player()

# game loop
while running:

    pygame.time.delay(10)
    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and Player.xpos > 0:
        # decrement in x co-ordinate
        Player.xpos -= vel

    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and Player.xpos < 500 - Player.width:
        # increment in x co-ordinate
        Player.xpos += vel

    # if left arrow key is pressed
    if keys[pygame.K_UP] and Player.ypos > 0:
        # decrement in y co-ordinate
        Player.ypos -= vel

    # if left arrow key is pressed
    if keys[pygame.K_DOWN] and Player.ypos < 500 - Player.height:
        # increment in y co-ordinate
        Player.ypos += vel

    # completely fill the surface object
    # with black colour
    screen.blit(bg, (0, 0))

    # drawing object on screen which is rectangle here
    Player.draw()

    # it refreshes the window
    pygame.display.update()
