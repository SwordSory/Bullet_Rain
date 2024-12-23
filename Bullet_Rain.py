import pygame
from pygame.locals import *
import random
import os



pygame.init()

width, height = pygame.display.Info().current_w*0.9, pygame.display.Info().current_h*0.9
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("BulletRain")
font = pygame.font.Font(None, int(height*25/243))
clock = pygame.time.Clock()



def random_speed_giver(r1, r2):
    random_speed = random.randint(r1, r2)
    return random_speed

def to_x_giver():
    random_x = random.randint(int(width*5/864), int(width - width*(5/216)))
    return int(random_x)

def random_y_giver():
    random_y = random.randint(int(height*5/486), int(height - height*(151/486)))
    return int(random_y)

def assects_pather(filename):
    asfp = os.path.dirname(os.path.realpath(__file__))
    return (os.path.join(asfp, filename))


class high_score:
    file_path = assects_pather("assects/high_score.txt")
    def read_high_score():
        if not os.path.exists(high_score.file_path):
            with open(high_score.file_path, "w") as file:
                file.write(str(0))
        with open(high_score.file_path, "r") as file:
            return int(file.read().strip())
            
    def write_high_score(h_score):
        with open(high_score.file_path, "w") as file:
            file.write(str(h_score))



    
main = "title_screen"
play_button = pygame.Rect(width-width*(499/864), height-height*(52/81), width*(67/432), height*(1/10))
to1y, to1x = 0-int(height*25/243), 300
to2y, to2x = 0-int(height*25/243), 1200
tb = pygame.image.load(assects_pather("assects/tb.png"))
tb = pygame.transform.scale(tb, (width*25/432,height*25/162))
loy, lox = 0, 0-int(width*25/432)
lb = pygame.image.load(assects_pather("assects/lb.png"))
lb = pygame.transform.scale(lb, (width*25/288,height*25/243))
roy, rox = 500, width
rb = pygame.image.load(assects_pather("assects/rb.png"))
rb = pygame.transform.scale(rb, (width*25/288,height*25/243))
score = 0
h_score = high_score.read_high_score()
life1c = "Red"
life2c = "Red"
life3c = "Red"
collision = 0

blue_player_x, blue_player_y = width/2, height-height*337/972
br1c = pygame.Rect(blue_player_x - height*5/81, blue_player_y - height*5/81, 2*(height*5/81), 2*(height*5/81))
ball = pygame.image.load(assects_pather("assects/ball.png"))
ball = pygame.transform.scale(ball, (height*40/243, height*40/243))

p_resume = pygame.Rect(width*317/864, height*750/972, width*115/432, height*95/972)
p_home = pygame.Rect(width*317/864, height*855/972, width*115/432, height*95/972)
r1 = 5
r2 = 20

keys = {}
running = True
while running:
    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == VIDEORESIZE:
                pygame.display.set_mode((width, height))

            elif event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()

                if play_button.collidepoint(pos) and event.button == 1 and main == "title_screen":
                    score = 0
                    collision = 0
                    life1c = "Red"
                    life2c = "Red"
                    life3c = "Red"
                    main = "game"

                if p_resume.collidepoint(pos) and event.button == 1 and main == "pause":
                    main = "game"

                if p_home.collidepoint(pos) and event.button == 1 and main == "pause":
                    main = "title_screen"


            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE and main == "game":
                    main = "pause"
                elif event.key == K_ESCAPE and main == "pause":
                    main = "game"                    

                keys[event.key] = True
            if event.type == pygame.KEYUP:
                keys[event.key] = False

            

            


    if main == "title_screen":
        screen.fill((135, 206, 235))
        pygame.draw.rect(screen, (124, 252, 0), (0, height-height*(131/486), width, height*(131/486)))
        pygame.draw.rect(screen, (205, 133, 63), (0, height-height*(121/486), width, height*(121/486)))
        pygame.draw.rect(screen, (139, 69, 19), (0, height-height*(61/486), width, height*(61/486)))
        pygame.draw.rect(screen, (101, 67, 33), (0, height-height*(26/486), width, height*(26/486)))

        pygame.draw.rect(screen, "Red", (width*668.7/1728, height*225/972, width*390.6/1728, height*97.2/972), )
        pygame.draw.rect(screen, "Black", (width*668.7/1728, height*225/972, width*390.6/1728, height*97.2/972), int(height*10/972))
        screen.blit(font.render("Bullet Rain", True, (245, 245, 245)), (width*682.5/1728, height*240/972))

        pygame.draw.rect(screen, "Red", play_button)
        pygame.draw.rect(screen, "Black", play_button, int(height*10/972))
        screen.blit(font.render("PLAY", True, (245, 245, 245)), (width*775/1728, height*365/972))

        screen.blit(font.render("High Score:", True, "Black"), (width*30/1728, height*30/972))
        screen.blit(font.render(str(h_score), True, "Black"), (width*420/1728, height*30/972))
        screen.blit(font.render("Latest Score:", True, "Black"), (width*30/1728, height*110/972))
        screen.blit(font.render(str(score), True, "Black"), (width*475/1728, height*110/972))





    elif main == "pause":
        screen.fill((135, 206, 235))


        screen.blit(tb, ( to1x- width*35/1728, to1y- height*22/972))
        screen.blit(tb, ( to2x- width*35/1728, to2y- height*22/972))
        screen.blit(lb, ( lox- width*22/1728, loy- height*35/972))
        screen.blit(rb, ( rox- width*22/1728, roy- height*35/972))


        pygame.draw.rect(screen, (124, 252, 0), (0, height-height*(131/486), width, height*(131/486)))
        pygame.draw.rect(screen, (205, 133, 63), (0, height-height*(121/486), width, height*(121/486)))
        pygame.draw.rect(screen, (139, 69, 19), (0, height-height*(61/486), width, height*(61/486)))
        pygame.draw.rect(screen, (101, 67, 33), (0, height-height*(26/486), width, height*(26/486)))


        screen.blit(font.render("Lives:", True, "Black"), (width*1200/1728, height*790/972))
        pygame.draw.circle(screen, life1c, (width*1460/1728, height*805/972), height*40/972)
        pygame.draw.circle(screen, life2c, (width*1560/1728, height*805/972), height*40/972)
        pygame.draw.circle(screen, life3c, (width*1660/1728, height*805/972), height*40/972)


        screen.blit(font.render("Score:", True, "Black"), (width*30/1728, height*790/972))
        screen.blit(font.render(str(score), True, "Black"), (width*250/1728, height*790/972))


        screen.blit(ball, (blue_player_x - height*80/972, blue_player_y - height*80/972))


        pygame.draw.rect(screen, (50, 50, 50), (width*600/1728, height*730/972, width*528/1728, height*242/972))
        pygame.draw.rect(screen, "Black", (width*600/1728, height*730/972, width*528/1728, height*242/972), int(height*10/972))


        pygame.draw.rect(screen, "Black", p_resume)
        pygame.draw.rect(screen, "Blue", p_resume, int(height*10/972))
        screen.blit(font.render("resume[esc]", True, "White"), (width*659/1728, height*765/972))

        pygame.draw.rect(screen, "Black", p_home)
        pygame.draw.rect(screen, "Red", p_home, int(height*10/972))
        screen.blit(font.render("home screen", True, "White"), (width*649/1728, height*870/972))


    elif main == "game":

        screen.fill((135, 206, 235))

        br1 = pygame.Rect(0, 0, width, height*10/972)
        br2 = pygame.Rect(0, 0, width*10/1728, height*710/972)
        br3 = pygame.Rect(width*1718/1728, 0, width*10/1728, height*710/972)
        to1 = pygame.Rect(to1x, to1y, width*30/1728, height*100/972)
        to2 = pygame.Rect(to2x, to2y, width*30/1728, height*100/972)
        lo = pygame.Rect(lox, loy, width*100/1728, height*30/972)
        ro = pygame.Rect(rox, roy, width*100/1728, height*30/972)


        pygame.draw.rect(screen, "Red", br1)
        pygame.draw.rect(screen, "Red", br2)
        pygame.draw.rect(screen, "Red", br3)


        screen.blit(tb, ( to1x- width*35/1728, to1y- height*22/972))
        screen.blit(tb, ( to2x- width*35/1728, to2y- height*22/972))
        screen.blit(lb, ( lox- width*22/1728, loy- height*35/972))
        screen.blit(rb, ( rox- width*22/1728, roy- height*35/972))



        pygame.draw.rect(screen, (124, 252, 0), (0, height-height*(131/486), width, height*(131/486)))
        pygame.draw.rect(screen, (205, 133, 63), (0, height-height*(121/486), width, height*(121/486)))
        pygame.draw.rect(screen, (139, 69, 19), (0, height-height*(61/486), width, height*(61/486)))
        pygame.draw.rect(screen, (101, 67, 33), (0, height-height*(26/486), width, height*(26/486)))

        screen.blit(font.render("Lives:", True, "Black"), (width*1200/1728, height*790/972))
        pygame.draw.circle(screen, life1c, (width*1460/1728, height*805/972), height*40/972)
        pygame.draw.circle(screen, life2c, (width*1560/1728, height*805/972), height*40/972)
        pygame.draw.circle(screen, life3c, (width*1660/1728, height*805/972), height*40/972)

        screen.blit(font.render("Score:", True, "Black"), (width*30/1728, height*790/972))
        screen.blit(font.render(str(score), True, "Black"), (width*250/1728, height*790/972))


        screen.blit(ball, (blue_player_x - height*80/972, blue_player_y - height*80/972))
        br1c = pygame.Rect(blue_player_x - height*5/81, blue_player_y - height*5/81, 2*(height*5/81), 2*(height*5/81))


        if keys.get(pygame.K_d):
            blue_player_x += width*10/1728
        if keys.get(pygame.K_a):
            blue_player_x -= width*10/1728
        if keys.get(pygame.K_s) and blue_player_y < height*635/972:
            blue_player_y += height*15/972
        if keys.get(pygame.K_w):
            blue_player_y -= height*10/972

        if not keys.get(pygame.K_w):
            blue_player_y += height*15/972
        if keys.get(pygame.K_LSHIFT) and keys.get(pygame.K_a):
            blue_player_x -= width*15/1728
        if keys.get(pygame.K_LCTRL) and keys.get(pygame.K_a):
            blue_player_x += width*5/1728
        if keys.get(pygame.K_LSHIFT) and keys.get(pygame.K_d):
            blue_player_x += width*15/1728
        if keys.get(pygame.K_LCTRL) and keys.get(pygame.K_d):
            blue_player_x -= width*5/1728
        if blue_player_y > height*635/972:
            blue_player_y = height*635/972


        if to1y == 0-height*100/972:
            to1s = random_speed_giver(r1, r2)
            to1x = to_x_giver()
        to1y += to1s
        if to1y > height*710/972:
            to1y = 0-height*100/972
            score += 1
            if score/10 == int(score/10):
                r2 += 1
            if score/25 == int(score/25):
                r1 += 1

        if to2y == 0-height*100/972:
            to2s = random_speed_giver(r1, r2)
            to2x = to_x_giver()
        to2y += to2s
        if to2y > height*710/972:
            to2y = 0-height*100/972
            score += 1
            if score/10 == int(score/10):
                r2 += 1
            if score/25 == int(score/25):
                r1 += 1

        if lox == 0-width*100/1728:
            los = random_speed_giver(r1, r2)
            loy = random_y_giver()
        lox += los
        if lox > width:
            lox = 0-width*100/1728
            score += 1
            if score/10 == int(score/10):
                r2 += 1
            if score/25 == int(score/25):
                r1 += 1


        if rox == width:
            ros = random_speed_giver(r1, r2)
            roy = random_y_giver()
        rox -= ros
        if rox < 0-width*100/1728:
            rox = width
            score += 1
            if score/10 == int(score/10):
                r2 += 1
            if score/25 == int(score/25):
                r1 += 1


        if br1c.colliderect(br1) or br1c.colliderect(br2) or br1c.colliderect(br3) or br1c.colliderect(to1) or br1c.colliderect(to2) or br1c.colliderect(lo) or br1c.colliderect(ro):
            collision += 1
            if collision == 1:
                life3c = (50, 50, 50)
            elif collision == 2:
                life3c = (50, 50, 50)
                life2c = (50, 50, 50)
            elif collision == 3:
                life3c = (50, 50, 50)
                life2c = (50, 50, 50)
                life1c = (50, 50, 50)
            blue_player_x, blue_player_y = width/2, height-height*337/972
            to1y = 0-height*100/972
            to2y = 0-height*100/972
            lox = 0-width*100/1728
            rox = width
            if score > h_score:
                high_score.write_high_score(score)
                h_score = high_score.read_high_score()
            if collision == 3:
                r1, r2 = 5, 20
                main = "title_screen"


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
