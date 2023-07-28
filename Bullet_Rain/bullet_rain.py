import pygame
from pygame.locals import *
import random
import os



pygame.init()


screen = pygame.display.set_mode((1728, 972))
pygame.display.set_caption("BulletRain")
font = pygame.font.Font(None, 100)
clock = pygame.time.Clock()


def random_speed_giver():
    random_speed = random.randint(5, 25)
    return random_speed

def to_x_giver():
    random_x = random.randint(1, 1688)
    return random_x

def random_y_giver():
    random_y = random.randint(1, 670)
    return random_y

def assects_pather(filename):
    asfp = os.path.dirname(os.path.realpath(__file__))
    return (os.path.join(asfp, filename))


main = "title_screen"
play_button = pygame.Rect(730, 347.2, 268, 97.2)
to1y, to1x = -100, 300
to2y, to2x = -100, 1200
tb = pygame.image.load(assects_pather("assects/tb.png"))
tb = pygame.transform.scale(tb, (100,150))
loy, lox = 0, -100
lb = pygame.image.load(assects_pather("assects/lb.png"))
lb = pygame.transform.scale(lb, (150,100))
roy, rox = 500, 1728
rb = pygame.image.load(assects_pather("assects/rb.png"))
rb = pygame.transform.scale(rb, (150,100))
score = 0
h_score = 0
life1c = "Red"
life2c = "Red"
life3c = "Red"
collision = 0

blue_player_x, blue_player_y = 864, 630
br1c = pygame.Rect(blue_player_x - 60, blue_player_y - 60, 120, 120)
ball = pygame.image.load(assects_pather("assects/ball.png"))
ball = pygame.transform.scale(ball, (160, 160))


keys = {}
running = True
while running:
    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == VIDEORESIZE:
                pygame.display.set_mode((1728, 972))

            elif event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()

                if play_button.collidepoint(pos) and event.button == 1 and main == "title_screen":
                    score = 0
                    collision = 0
                    life1c = "Red"
                    life2c = "Red"
                    life3c = "Red"
                    main = "game"

            if event.type == pygame.KEYDOWN:
                keys[event.key] = True
            if event.type == pygame.KEYUP:
                keys[event.key] = False

            

            


    if main == "title_screen":
        screen.fill((135, 206, 235))
        pygame.draw.rect(screen, (101, 67, 33), (0, 920, 1728, 52), 100)
        pygame.draw.rect(screen, (139, 69, 19), (0, 850, 1728, 70), 100)
        pygame.draw.rect(screen, (205, 133, 63), (0, 730, 1728, 120), 100)
        pygame.draw.rect(screen, (124, 252, 0), (0, 710, 1728, 20), 100)

        pygame.draw.rect(screen, "Red", (668.7, 225, 390.6, 97.2), 100)
        pygame.draw.rect(screen, "Black", (668.7, 225, 390.6, 97.2), 10)
        screen.blit(font.render("Bullet Rain", True, (245, 245, 245)), (682.5, 240))

        pygame.draw.rect(screen, "Red", play_button, 100)
        pygame.draw.rect(screen, "Black", play_button, 10)
        screen.blit(font.render("PLAY", True, (245, 245, 245)), (775, 365))

        screen.blit(font.render("High Score:", True, "Black"), (30, 30))
        screen.blit(font.render(str(h_score), True, "Black"), (420, 30))
        screen.blit(font.render("Latest Score:", True, "Black"), (30, 110))
        screen.blit(font.render(str(score), True, "Black"), (475, 110))



    elif main == "game":

        screen.fill((135, 206, 235))

        br1 = pygame.Rect(0, 0, 1728, 10)
        br2 = pygame.Rect(0, 0, 10, 710)
        br3 = pygame.Rect(1718, 0, 10, 710)
        to1 = pygame.Rect(to1x, to1y, 30, 100)
        to2 = pygame.Rect(to2x, to2y, 30, 100)
        lo = pygame.Rect(lox, loy, 100, 30)
        ro = pygame.Rect(rox, roy, 100, 30)


        pygame.draw.rect(screen, "Red", br1, 100)
        pygame.draw.rect(screen, "Red", br2, 100)
        pygame.draw.rect(screen, "Red", br3, 100)


        screen.blit(tb, ( to1x- 35, to1y- 22))
        screen.blit(tb, ( to2x- 35, to2y- 25))
        screen.blit(lb, ( lox- 22, loy- 35))
        screen.blit(rb, ( rox- 22, roy- 35))



        pygame.draw.rect(screen, (101, 67, 33), (0, 920, 1728, 52), 100)
        pygame.draw.rect(screen, (139, 69, 19), (0, 850, 1728, 70), 100)
        pygame.draw.rect(screen, (205, 133, 63), (0, 730, 1728, 120), 100)
        pygame.draw.rect(screen, (124, 252, 0), (0, 710, 1728, 20), 100)

        screen.blit(font.render("Lives:", True, "Black"), (1200, 790))
        pygame.draw.circle(screen, life1c, (1460, 810), 40)
        pygame.draw.circle(screen, life2c, (1560, 810), 40)
        pygame.draw.circle(screen, life3c, (1660, 810), 40)

        screen.blit(font.render("Score:", True, "Black"), (30, 790))
        screen.blit(font.render(str(score), True, "Black"), (250, 790))


        screen.blit(ball, (blue_player_x - 80, blue_player_y - 80))
        br1c = pygame.Rect(blue_player_x - 60, blue_player_y - 60, 120, 120)


        if keys.get(pygame.K_d):
            blue_player_x += 10
        if keys.get(pygame.K_a):
            blue_player_x -= 10
        if keys.get(pygame.K_s) and blue_player_y < 650:
            blue_player_y += 15
        if keys.get(pygame.K_w):
            blue_player_y -= 10

        if not keys.get(pygame.K_w):
            blue_player_y += 15
        if keys.get(pygame.K_LSHIFT) and keys.get(pygame.K_a):
            blue_player_x -= 15
        if keys.get(pygame.K_LCTRL) and keys.get(pygame.K_a):
            blue_player_x += 5
        if keys.get(pygame.K_LSHIFT) and keys.get(pygame.K_d):
            blue_player_x += 15
        if keys.get(pygame.K_LCTRL) and keys.get(pygame.K_d):
            blue_player_x -= 5
        if blue_player_y > 630:
            blue_player_y = 630


        if to1y == -100:
            to1s = random_speed_giver()
            to1x = to_x_giver()
        to1y += to1s
        if to1y > 710:
            to1y = -100
            score += 1

        if to2y == -100:
            to2s = random_speed_giver()
            to2x = to_x_giver()
        to2y += to2s
        if to2y > 710:
            to2y = -100
            score += 1

        if lox == -100:
            los = random_speed_giver()
            loy = random_y_giver()
        lox += los
        if lox > 1728:
            lox = -100
            score += 1

        if rox == 1728:
            ros = random_speed_giver()
            roy = random_y_giver()
        rox -= ros
        if rox < -100:
            rox = 1728 
            score += 1


        if br1c.colliderect(br1) or br1c.colliderect(br2) or br1c.colliderect(br3) or br1c.colliderect(to1) or br1c.colliderect(to2) or br1c.colliderect(lo) or br1c.colliderect(ro):
            collision += 1
            if collision == 1:
                life3c = (50, 50, 50)
            elif collision == 2:
                life3c = (50, 50, 50)
                life2c = (50, 50, 50)
            elif collision == 2:
                life3c = (50, 50, 50)
                life2c = (50, 50, 50)
                life1c = (50, 50, 50)
            blue_player_x, blue_player_y = 864, 650
            to1y = -100
            to2y = -100
            lox = -100
            rox = 1728
            if score > h_score:
                h_score = score
            if collision == 3:
                main = "title_screen"


    pygame.display.flip()
    clock.tick(60)

pygame.quit()