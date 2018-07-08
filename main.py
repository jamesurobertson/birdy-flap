import sys, pygame, random
pygame.init()

def handle_event():
    global started
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
            speed[1] = SPEED_BOUNCE
            started = True

# Draw "bird" and set initial position
def load_bird(img):
    bird = pygame.image.load(img)
    rect = bird.get_rect()
    rect.left = (WIDTH / 3) - (rect.width / 2)
    rect.bottom = (HEIGHT / 2) + (rect.height / 2)
    return bird, rect

# Constants
BACKGROUND = "background.png"
BIRD = "james.png"
FPS = 60
WINDOW_SIZE = WIDTH, HEIGHT = 480, 480
SPEED_BOUNCE = -10
SPEED_MAX = 25
GRAVITY = 0.65
clock = pygame.time.Clock()

# Variables
speed = [0, 0]
started = False
screen = pygame.display.set_mode(WINDOW_SIZE)

# background scrolling
bkgd = pygame.image.load(BACKGROUND).convert()
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

james, jamesrect = load_bird(BIRD)

# main loop
while True:
    handle_event()

    # Flipping the sign of speed makes it change direction.
    # This combined with line 28 gives a bouncing effect.
    if jamesrect.bottom > HEIGHT:
        speed[1] = 0

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

    if started:
        # Flipping the sign of speed makes it change direction.
        # This combined with line 28 gives a bouncing effect.
        if jamesrect.bottom > HEIGHT:
            speed[1] = 0
            started = False
            jamesrect.left = (WIDTH / 3) - (jamesrect.width / 2)
            jamesrect.bottom = (HEIGHT / 2) + (jamesrect.height / 2)

        # Accelerate up to speed_max
        if speed[1] < SPEED_MAX:
            speed[1] += GRAVITY

        jamesrect = jamesrect.move(speed)
        
    screen.blit(james, jamesrect)
    screen.blit(pipeUpper, pipeUpperRect)
    screen.blit(pipeLower, pipeLowerRect)
    screen.blit(pipeUpper2, pipeUpperRect2)
    screen.blit(pipeLower2, pipeLowerRect2)

    pygame.display.flip()
    clock.tick(FPS)
