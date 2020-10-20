import pygame
import random
import neat
import math
#Initializing the pygame
pygame.init()

#create screen
screen=pygame.display.set_mode((640,960))

score=0
px = 320
py = 944
status="T"

red=(255,0,0)
green=(0,255,0)
WHITE=(255,255,255)

status="T"

step_x=0
step_y=-16
pos=[(320,944)]
snek_len=1
#FOOD
def ran():
    lx=[i[0] for i in pos]
    ly=[j[1] for j in pos]
    while True:
        x=random.randrange(0,640,16)
        y=random.randrange(0,960,16)
        if x not in lx and y not in ly:
            return x,y 
        else:
            continue
F_x,F_y = ran()


def draw():
    for i in range(0,snek_len):
        pygame.draw.rect(screen, red, (pos[i][0],pos[i][1], 16, 16))

def ad(q,w):
    pos.append((q,w))

def pos_update(x,y):
    for i in range(snek_len-1,0,-1):
        pos[i]=pos[i-1]
    pos[0]=(x,y)
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

config_path="./config.txt"

running=True
while running:
    clock = pygame.time.Clock()
    pygame.display.flip()

    # Ensure program maintains a rate of  frames per second
    clock.tick(10)
    screen.fill((0,0,0))
    #screen.blit(back,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if status is "L" or status is "R":
                    continue
                elif status is "T" or status is "B":
                    step_y=0
                    step_x=-16
                    status="L"
            if event.key == pygame.K_RIGHT:
                if status is "L" or status is "R":
                    continue
                elif status is "T" or status is "B":
                    step_y=0
                    step_x=16
                    status="R"
            if event.key == pygame.K_UP:
                if status is "T" or status is "B":
                    continue
                elif status is "R" or status is "L":
                    step_y=-16
                    step_x=0
                    status="T"
            if event.key == pygame.K_DOWN:
                if status is "T" or status is "B":
                    continue
                elif status is "L" or status is "R":
                    step_y=16
                    step_x=0
                    status="B"
    last_x=px
    last_y=py


    px=px+step_x
    py=py+step_y
    if (px == F_x and py == F_y):
        snek_len=snek_len+1
        score=score+1
        print(score)
        ad(last_x,last_y)
        F_x,F_y = ran()
        pygame.draw.rect(screen,green,(F_x,F_y,16,16))
    else:
        pygame.draw.rect(screen,green,(F_x,F_y,16,16))
    if ((px>=0 and px<=626 and py>=0 and py<=944) and ((px,py) not in pos )):
        pos_update(px,py)
        draw()
        #pygame.draw.rect(screen, red, (px, py, 16, 16))
    else:
        print("END")
        break
    draw_text(screen, str(score), 18, 320,10)
    pygame.display.update()
        
"""
def run():
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                            neat.DefaultSpeciesSet, neat.DefaultStagnation,
                            config_file)
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    winner= p.run(f,50)"""