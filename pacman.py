# import the libraries
import sys, pygame

# initialize pygame
pygame.init()

# set size of the window
size = width, height = 1024, 720

# initially pacman does not move
speed = [0,0]

# windows color
black = 0, 0, 0

screen = pygame.display.set_mode(size)

# pacman image object
pacman = pygame.image.load('pacman.gif')
# rectangle around pacman
pacmanrect = pacman.get_rect()

# pacman not moving initially
moving = False

# the game loop
while 1:
    # check all the current events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving = True
                speed = [-8, 0]
            if event.key == pygame.K_RIGHT:
                moving = True
                speed = [8, 0]
            if event.key == pygame.K_UP:
                moving = True
                speed = [0, -8]
            if event.key == pygame.K_DOWN:
                moving = True
                speed = [0, 8]
    if moving:
        pacmanrect = pacmanrect.move(speed)
    if pacmanrect.left < 0 or pacmanrect.right > width:
        moving = False
    if pacmanrect.top < 0 or pacmanrect.bottom > height:
        moving = False

    screen.fill(black)
    screen.blit(pacman, pacmanrect)
    pygame.display.flip()
    pygame.display.update()