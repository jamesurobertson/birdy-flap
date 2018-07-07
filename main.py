import sys, pygame
pygame.init()

def handle_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
            speed[1] = SPEED_BOUNCE

# Constants
FPS = 60
WINDOW_SIZE = WIDTH, HEIGHT = 480, 480
SPEED_BOUNCE = -15
SPEED_MAX = 25
GRAVITY = 0.75
clock = pygame.time.Clock()

# Variables
speed = [0, 0]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Draw "bird" and set initial position
james = pygame.image.load("james.png")
jamesrect = james.get_rect()
jamesrect.left = (WIDTH / 3) - (jamesrect.width / 2)
jamesrect.bottom = (HEIGHT / 2)

# background scrolling
bkgd = pygame.image.load("background.png").convert()
x = 0

# main loop
while True:
    handle_event()

    # Flipping the sign of speed makes it change direction.
    # This combined with line 28 gives a bouncing effect.
    if jamesrect.bottom > HEIGHT:
        speed[1] = -speed[1]

    # Accelerate up to speed_max
    if speed[1] < SPEED_MAX:
        speed[1] += GRAVITY

    jamesrect = jamesrect.move(speed)

    # scrolling image
    rel_x = x % bkgd.get_rect().width
	
    screen.blit(bkgd, (rel_x - bkgd.get_rect().width, 0))
    if rel_x < WIDTH:
        screen.blit(bkgd, (rel_x, 0))
    x += -2

    screen.blit(james, jamesrect)
    pygame.display.flip()
    clock.tick(FPS)
