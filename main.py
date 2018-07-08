import sys, pygame, random
pygame.init()

# Constants
BACKGROUND = "background.png"
BIRD = "james.png"
PIPE = "pipe.bmp"
FPS = 60
WINDOW_SIZE = WIDTH, HEIGHT = 480, 480
SPEED_BOUNCE = -10
SPEED_MAX = 25
GRAVITY = 0.65
MYFONT = pygame.font.match_font('arial')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()

# Variables
speed = [0, 0]
started = False
score = 0;
screen = pygame.display.set_mode(WINDOW_SIZE)

# background
bkgd = pygame.image.load(BACKGROUND).convert()
bkgdx = 0

def handle_event():
    global started
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
            speed[1] = SPEED_BOUNCE
            started = True

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(MYFONT, size)
    textSurface = font.render(text, True, BLACK)
    textRect = textSurface.get_rect()
    textRect.midtop = (x, y)
    surf.blit(textSurface, textRect)
     


# Draw "bird" and set initial position
def load_bird(img):
    bird = pygame.image.load(img)
    rect = bird.get_rect()
    rect.left = (WIDTH / 3) - (rect.width / 2)
    rect.bottom = (HEIGHT / 2) + (rect.height / 2)
    return bird, rect

# draw pipes and set initial positions
def load_pipe(img):
    pipeUpper = pygame.image.load(img)
    pipeLower = pygame.image.load(img)
    pipeUpperRect = pipeUpper.get_rect()
    pipeLowerRect = pipeLower.get_rect()
    pipeUpperRect.left = WIDTH + (WIDTH / 3)
    pipeLowerRect.left = WIDTH + (WIDTH / 3)
    pipeUpperRect.bottom = random.randrange(30 , 300)
    # space between pipes
    pipeLowerRect.top = pipeUpperRect.bottom + (jamesrect.height * 2)
    return pipeUpper, pipeUpperRect, pipeLower, pipeLowerRect

def load_pipe2(img):
    pipeUpper2 = pygame.image.load(img)
    pipeLower2 = pygame.image.load(img)
    pipeUpperRect2 = pipeUpper.get_rect()
    pipeLowerRect2 = pipeLower.get_rect()
    pipeUpperRect2.left = pipeUpperRect.left + (WIDTH * .73)
    pipeLowerRect2.left = pipeLowerRect.left + (WIDTH * .73)

    pipeUpperRect2.bottom = random.randrange(30 , 300)
    # space between pipes
    pipeLowerRect2.top = pipeUpperRect2.bottom + (jamesrect.height * 2)
    return pipeUpper2, pipeUpperRect2, pipeLower2, pipeLowerRect2

# load objects
james, jamesrect = load_bird(BIRD)
pipeUpper, pipeUpperRect, pipeLower, pipeLowerRect = load_pipe(PIPE)
pipeUpper2, pipeUpperRect2, pipeLower2, pipeLowerRect2 = load_pipe2(PIPE)


# main loop
while True:
    handle_event()

    # scrolling backgroundimage
    rel_x = bkgdx % bkgd.get_rect().width
    if rel_x < WIDTH:
        screen.blit(bkgd, (rel_x, 0))

    bkgdx += -2

    if started:    
        # replacing the pipes
        if pipeUpperRect.left < -pipeUpperRect.width:
            pipeUpper, pipeUpperRect, pipeLower, pipeLowerRect = load_pipe(PIPE)
        if pipeUpperRect2.left < -pipeUpperRect2.width:
            pipeUpper2, pipeUpperRect2, pipeLower2, pipeLowerRect2 = load_pipe2(PIPE)

        # scrolling pipes
        pipeUpperRect.left += -5
        pipeLowerRect.left += -5
        pipeUpperRect2.left += -5
        pipeLowerRect2.left += -5


        # Flipping the sign of speed makes it change direction.
        if jamesrect.bottom > HEIGHT:
            speed[1] = 0
            started = False
            pipeUpper, pipeUpperRect, pipeLower, pipeLowerRect = load_pipe(PIPE)
            pipeUpper2, pipeUpperRect2, pipeLower2, pipeLowerRect2 = load_pipe2(PIPE)
            james, jamesrect = load_bird(BIRD)
            score = 0


        # Accelerate up to speed_max
        if speed[1] < SPEED_MAX:
            speed[1] += GRAVITY

        jamesrect = jamesrect.move(speed) 

    #scoring 
    if pipeUpperRect.right == 132:
        score += 1
    if pipeUpperRect2.right == 132:
        score += 1

    # collision testing

    if jamesrect.colliderect(pipeUpperRect) or jamesrect.colliderect(pipeLowerRect):
        print("Collide")
        speed[1] = 0
        started = False
        pipeUpper, pipeUpperRect, pipeLower, pipeLowerRect = load_pipe(PIPE)
        pipeUpper2, pipeUpperRect2, pipeLower2, pipeLowerRect2 = load_pipe2(PIPE)
        james, jamesrect = load_bird(BIRD)
        score = 0
	
    screen.blit(bkgd, (rel_x - bkgd.get_rect().width, 0))
    screen.blit(pipeUpper, pipeUpperRect)
    screen.blit(pipeLower, pipeLowerRect)
    screen.blit(pipeUpper2, pipeUpperRect2)
    screen.blit(pipeLower2, pipeLowerRect2)
    draw_text(screen, str(score), 36, WIDTH/2, 10)

    screen.blit(james, jamesrect)
        
    pygame.display.flip()
    clock.tick(FPS)
