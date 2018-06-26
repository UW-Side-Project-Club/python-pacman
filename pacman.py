# import the libraries
import sys, pygame

def get_angle(cur_angle, des_angle):
    ang = des_angle-cur_angle
    if ang < 0:
        ang += 360
    return ang

# initialize pygame
pygame.init()

# set size of the window
size = width, height = 1024, 720

# initially pacman does not move
speed = [0,0]
angle = 0

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
                if pacmanrect.left >= 0:
                    moving = True
                    speed = [-8, 0]
                    pacman = pygame.transform.rotate(pacman, get_angle(angle,180))
                    angle = 180
            if event.key == pygame.K_RIGHT:
                if pacmanrect.right <= width:
                    moving = True
                    speed = [8, 0]
                    pacman = pygame.transform.rotate(pacman, get_angle(angle, 0))
                    angle = 0
            if event.key == pygame.K_UP:
                if pacmanrect.top >= 0:
                    moving = True
                    speed = [0, -8]
                    pacman = pygame.transform.rotate(pacman, get_angle(angle, 90))
                    angle = 90
            if event.key == pygame.K_DOWN:
                if pacmanrect.bottom <= height:
                    moving = True
                    speed = [0, 8]
                    pacman = pygame.transform.rotate(pacman, get_angle(angle, 270))
                    angle = 270
    if moving:
        pacmanrect = pacmanrect.move(speed)
    if pacmanrect.left < 0:  
        pacmanrect.left = 0
        moving = False
    if pacmanrect.right > width:
        pacmanrect.right = width
        moving = False
    if pacmanrect.top < 0:
        pacmanrect.top = 0
        moving = False
    if pacmanrect.bottom > height:
        pacmanrect.bottom = height
        moving = False

    screen.fill(black)
    screen.blit(pacman, pacmanrect)
    pygame.display.flip()
    pygame.display.update()