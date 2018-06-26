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

# pacman not moving or touching walls initially
move_left = False
move_right = False
move_up = False
move_down = False
touch_left = False
touch_right = False
touch_top = False
touch_bottom = False

# the game loop
while 1:
    # check all the current events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
                # moving left ensures not touching right wall
                touch_right = False
                # set all other directions to be false
                move_right = False
                move_up = False
                move_down = False
            if event.key == pygame.K_RIGHT:
                move_right = True
                touch_left = False
                # set all other directions to be false
                move_left = False
                move_down = False
                move_up = False
            if event.key == pygame.K_UP:
                move_up = True
                touch_bottom = False
                # set all other directions to be false
                move_right = False
                move_left = False
                move_down = False
            if event.key == pygame.K_DOWN:
                move_down = True
                touch_top = False
                # set all other directions to be false
                move_up = False
                move_left = False
                move_right = False
    if move_left and not touch_left:
        pacmanrect = pacmanrect.move([-8,0])
    if move_right and not touch_right:
        pacmanrect = pacmanrect.move([8,0])
    if move_up and not touch_top:
        pacmanrect = pacmanrect.move([0, -8])
    if move_down and not touch_bottom:
        pacmanrect = pacmanrect.move([0, 8])
    if pacmanrect.left < 0:
        move_left = False
        touch_left = True
    if pacmanrect.right > width:
        move_right = False
        touch_right = True
    if pacmanrect.top < 0:
        move_top = False
        touch_top = True
    if pacmanrect.bottom > height:
        move_bottom = False
        touch_bottom = True

    screen.fill(black)
    screen.blit(pacman, pacmanrect)
    pygame.display.flip()
    pygame.display.update()