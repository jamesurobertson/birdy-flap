import sys, pygame, random
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
bkgdx = 0

# draw pipes and set initial positions
def load_pipe(img):
    pipeUpper = pygame.image.load(img)
    pipeLower = pygame.image.load(img)
    pipeUpperRect = pipeUpper.get_rect()
    pipeLowerRect = pipeLower.get_rect()
    pipeUpperRect.left = WIDTH + (WIDTH / 3)
    pipeLowerRect.left = WIDTH + (WIDTH / 3)
    pipeUpperRect.bottom = random.randrange(30 , 322)
    # space between pipes
    pipeLowerRect.top = pipeUpperRect.bottom + (jamesrect.height * 2.5)
    return pipeUpper, pipeUpperRect, pipeLower, pipeLowerRect

# pipe scrolling
pipeUpper, pipeUpperRect, pipeLower, pipeLowerRect = load_pipe("pipe.bmp")
pipeUpper2, pipeUpperRect2, pipeLower2, pipeLowerRect2 = load_pipe("pipe.bmp")


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

    # scrolling backgroundimage
    rel_x = bkgdx % bkgd.get_rect().width
	
    screen.blit(bkgd, (rel_x - bkgd.get_rect().width, 0))
    if rel_x < WIDTH:
        screen.blit(bkgd, (rel_x, 0))
    bkgdx += -2
    # replacing the pipes
    if pipeUpperRect.left < -pipeUpperRect.width:
        pipeUpperRect.left = WIDTH + (WIDTH / 3)
        pipeLowerRect.left = WIDTH + (WIDTH / 3)
        pipeUpperRect.bottom = random.randrange(30 , 322)
        pipeLowerRect.top = pipeUpperRect.bottom + (jamesrect.height * 2.5)
    if pipeUpperRect2.left < -pipeUpperRect.width:
        pipeUpperRect2.left = WIDTH + (WIDTH / 3)
        pipeLowerRect2.left = WIDTH + (WIDTH / 3)
        pipeUpperRect2.bottom = random.randrange(30 , 322)
        pipeLowerRect2.top = pipeUpperRect2.bottom + (jamesrect.height * 2.5)
    
    pipeUpperRect.left += -5
    pipeLowerRect.left += -5 

    screen.blit(james, jamesrect)
    screen.blit(pipeUpper, pipeUpperRect)
    screen.blit(pipeLower, pipeLowerRect)
    screen.blit(pipeUpper2, pipeUpperRect2)
    screen.blit(pipeLower2, pipeLowerRect2)

    pygame.display.flip()
    clock.tick(FPS)
