import sys, pygame, random
from classes import Pipes
pygame.init()

# Constants
BACKGROUND = "background.png"
BIRD = "james.png"
PIPE = "pipe.bmp"
PIPE_SPEED = 2
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

# load objects
james, jamesrect = load_bird(BIRD)
pipes = Pipes(3, jamesrect, screen)
pipes.place()

# main loop
while True:
    handle_event()

    # scrolling backgroundimage
    rel_x = bkgdx % bkgd.get_rect().width
    if rel_x < WIDTH:
        screen.blit(bkgd, (rel_x, 0))

    bkgdx -= 2

    if started:    
        # Flipping the sign of speed makes it change direction.
        if jamesrect.bottom > HEIGHT:
            speed[1] = 0
            started = False
            pipes.place()
            james, jamesrect = load_bird(BIRD)
            score = 0

        # Accelerate up to speed_max
        if speed[1] < SPEED_MAX:
            speed[1] += GRAVITY

        jamesrect = jamesrect.move(speed)
        pipes.move(PIPE_SPEED)

    # scoring 
    # if pipes.upperRect.right == 132:
    #     score += 1

    # collision testing
    # if jamesrect.colliderect(pipes.upperRect) or jamesrect.colliderect(pipes.lowerRect):
    #     speed[1] = 0
    #     started = False
    #     pipes.place()
    #     james, jamesrect = load_bird(BIRD)
    #     score = 0
	
    screen.blit(bkgd, (rel_x - bkgd.get_rect().width, 0))
    pipes.blit(screen)
    draw_text(screen, str(score), 36, WIDTH/2, 10)
    screen.blit(james, jamesrect)
        
    pygame.display.flip()
    clock.tick(FPS)
