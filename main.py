'Sumo'
'Febuary 20, 2024'
__author__ = 'Harrison Beck'

import pygame, sys, math
from pygame.locals import *

pygame.init()

textfont = pygame.font.SysFont("sfnsmono", 40)
punch = pygame.mixer.Sound("resources/punch.mp3")

pygame.display.set_caption('Sumo')

#Colors
red=pygame.Color(240,55,55)
light_blue=pygame.Color(50, 129, 168)
blue=pygame.Color(20,20,128)
black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
tan=pygame.Color(210,180,140)
grey=pygame.Color(150, 150, 150)
light_grey=pygame.Color(200, 200, 200)

#Dimensions
w=800
h=600

fpsClock=pygame.time.Clock()
screen=pygame.display.set_mode((w,h))
centerX=w//2
centerY=h//2

title = True

#Stage
stageR=250
def stage (centerX,centerY):
    pygame.draw.circle(screen, light_blue, (centerX,centerY),stageR)

#Character 1
radius=int((stageR//10))
x1=int(centerX-(stageR*0.8))
y1=centerY
x1_dir=0
y1_dir=0
win1 = 0

#Character 2
x2=int(centerX-(stageR*-0.8))
y2=centerY
x2_dir=0
y2_dir=0
win2 = 0

p1class = 'normal'
p2class = 'normal'

def char1(p1class):
    global x1,y1,radius
    if p1class=='normal':
        pygame.draw.circle(screen, red, (x1,y1),radius)
    if p1class=='bull':
        pygame.draw.circle(screen, red, (x1,y1),radius)
        pygame.draw.circle(screen, white, (x1+radius-radius/2,y1),radius/4)
        pygame.draw.circle(screen, white, (x1-radius+radius/2,y1),radius/4)
    if p1class == 'big':
        pygame.draw.circle(screen, red, (x1,y1),radius+20)

def char2(p2class):
    global x2,y2, radius
    if p2class=='normal':
        pygame.draw.circle(screen, blue, (x2,y2),radius)
    if p2class=='bull':
        pygame.draw.circle(screen, blue, (x2,y2),radius)
        pygame.draw.circle(screen, white, (x2+radius-radius/2,y2),radius/4)
        pygame.draw.circle(screen, white, (x2-radius+radius/2,y2),radius/4)
    if p2class == 'big':
        pygame.draw.circle(screen, red, (x2,y2),radius+20)


def check_collision(x1,y1):
    global stageR, centerX, centerY
    playerxdistance = abs(centerX - x1)
    playerydistance = abs(centerY - y1)
    distance = math.sqrt(playerxdistance**2 + playerydistance**2)
    if distance > stageR:
        player_out = True
    else:
        player_out = False
    return player_out

def player_collisions():
    global x1,x2,y1,y2,radius, x1_dir, y1_dir, x2_dir, y2_dir, p1class, p2class
    playerxdistance = abs(x2 - x1)
    playerydistance = abs(y2 - y1)
    distance = math.sqrt(playerxdistance**2 + playerydistance**2)
    if (p1class == 'normal' or p1class == 'bull') and (p2class == 'normal' or p2class == 'bull'):
        if distance < 2 * radius:
            pygame.mixer.Sound.play(punch)
            x1_dir, x2_dir, y1_dir, y2_dir = x2_dir, x1_dir, y2_dir, y1_dir

    elif p1class == 'big' and p2class == 'big':
        if distance < 2 * radius+40:
            pygame.mixer.Sound.play(punch)
            x1_dir, x2_dir, y1_dir, y2_dir = x2_dir * 0.75, x1_dir * 0.75, y2_dir * 0.75, y1_dir * 0.75

    elif p1class == 'big' or p2class == 'big':
        if distance < 2 * radius+20:
            pygame.mixer.Sound.play(punch)
            if p1class == 'big':
                x1_dir, x2_dir, y1_dir, y2_dir = x2_dir * 0.75, x1_dir, y2_dir * 0.75, y1_dir
            if p2class == 'big':
                x1_dir, x2_dir, y1_dir, y2_dir = x2_dir, x1_dir * 0.75, y2_dir, y1_dir * 0.75

def player1win():
    global w, h
    while True:
        screen.fill(white)
        rw = textfont.render("Red Wins", 1, (red))
        rw_w, rw_h = rw.get_rect().width, rw.get_rect().height
        screen.blit(rw, [w / 2 - rw_w / 2, h / 2 - rw_h / 2 - 50])

        pa_w, pa_h = 150, 50
        pa_x, pa_y= w / 2 - pa_w / 2, (h / 2 - pa_h / 2) + 50

        s = textfont.render("Start", 1, (black))
        s_w, s_h = s.get_rect().width, s.get_rect().height
        screen.blit(s, [w / 2 - s_w / 2, h / 2 - s_h / 2 + 50])

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                mouseX, mouseY = pygame.mouse.get_pos()
                if mouseX in range(int(pa_x), int(pa_x + pa_w)) and mouseY in range(int(pa_y), int(pa_y + pa_h)):
                    return
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return


        mouseX, mouseY = pygame.mouse.get_pos()

        if mouseX in range(int(pa_x), int(pa_x + pa_w)) and mouseY in range(int(pa_y), int(pa_y + pa_h)):
            pygame.draw.rect(screen, (light_grey), (pa_x, pa_y, pa_w, pa_h))
            screen.blit(s, [w / 2 - s_w / 2, h / 2 - s_h / 2 + 50])
        else:
            pygame.draw.rect(screen, (grey), (pa_x, pa_y, pa_w, pa_h))
            screen.blit(s, [w / 2 - s_w / 2, h / 2 - s_h / 2 + 50])

        pygame.display.update()

def player2win():
    global w, h
    while True:
        screen.fill(white)
        rw = textfont.render("Blue Wins", 1, (blue))
        rw_w, rw_h = rw.get_rect().width, rw.get_rect().height
        screen.blit(rw, [w / 2 - rw_w / 2, h / 2 - rw_h / 2 - 50])

        pa_w, pa_h = 150, 50
        pa_x, pa_y = w / 2 - pa_w / 2, (h / 2 - pa_h / 2) + 50

        s = textfont.render("Start", 1, (black))
        s_w, s_h = s.get_rect().width, s.get_rect().height
        screen.blit(s, [w / 2 - s_w / 2, h / 2 - s_h / 2 + 50])

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                mouseX, mouseY = pygame.mouse.get_pos()
                if mouseX in range(int(pa_x), int(pa_x + pa_w)) and mouseY in range(int(pa_y), int(pa_y + pa_h)):
                    return
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return

        mouseX, mouseY = pygame.mouse.get_pos()

        if mouseX in range(int(pa_x), int(pa_x + pa_w)) and mouseY in range(int(pa_y), int(pa_y + pa_h)):
            pygame.draw.rect(screen, (light_grey), (pa_x, pa_y, pa_w, pa_h))
            screen.blit(s, [w / 2 - s_w / 2, h / 2 - s_h / 2 + 50])
        else:
            pygame.draw.rect(screen, (grey), (pa_x, pa_y, pa_w, pa_h))
            screen.blit(s, [w / 2 - s_w / 2, h / 2 - s_h / 2 + 50])

        pygame.display.update()


play = True
def reset():
    global x2, y2, x1, y1, x1_dir, x2_dir, y1_dir, y2_dir
    x2 = int(centerX - (stageR * -0.8))
    y2 = centerY
    x1 = int(centerX - (stageR * 0.8))
    y1 = centerY
    x1_dir = 0
    x2_dir = 0
    y1_dir = 0
    y2_dir = 0

def score():
    global win1, win2, w
    redscore, bluescore = textfont.render(str(win1), 1, (red)), textfont.render(str(win2), 1, (blue))
    screen.blit(redscore, [50,50])
    screen.blit(bluescore, [w-50,50])

def title_screen():
    while True:
        screen.fill(white)
        title = textfont.render("Sumo", 1, (black))
        title_w, title_h = title.get_rect().width, title.get_rect().height
        screen.blit(title, [w / 2 - title_w / 2, h / 2 - title_h / 2 -150])

        s = textfont.render("Start", 1, (black))
        pa_w, pa_h = 150, 50
        pa_x, pa_y= w / 2 - pa_w / 2, (h / 2 - pa_h / 2) - 50
        s_w, s_h = s.get_rect().width, s.get_rect().height

        mouseX, mouseY = pygame.mouse.get_pos()

        if mouseX in range(int(pa_x), int(pa_x + pa_w)) and mouseY in range(int(pa_y), int(pa_y + pa_h)):
            pygame.draw.rect(screen, (light_grey), (pa_x, pa_y, pa_w, pa_h))
            screen.blit(s, [w / 2 - s_w / 2, h / 2 - s_h / 2 - 50])
        else:
            pygame.draw.rect(screen, (grey), (pa_x, pa_y, pa_w, pa_h))
            screen.blit(s, [w / 2 - s_w / 2, h / 2 - s_h / 2 - 50])

        q = textfont.render("Quit", 1, (black))
        bu_w, bu_h = 150, 50
        bu_x, bu_y= w / 2 - bu_w / 2, (h / 2 - bu_h / 2) + 50
        q_w, q_h = q.get_rect().width, q.get_rect().height

        if mouseX in range(int(bu_x), int(bu_x + bu_w)) and mouseY in range(int(bu_y), int(bu_y + bu_h)):
            pygame.draw.rect(screen, (light_grey), (bu_x, bu_y, bu_w, bu_h))
            screen.blit(q, [w / 2 - q_w / 2, h / 2 - q_h / 2 + 50])
        else:
            pygame.draw.rect(screen, (grey), (bu_x, bu_y, bu_w, bu_h))
            screen.blit(q, [w / 2 - q_w / 2, h / 2 - q_h / 2 + 50])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                exit()
            if event.type==MOUSEBUTTONUP:
                if mouseX in range(int(bu_x), int(bu_x + bu_w)) and mouseY in range(int(bu_y), int(bu_y + bu_h)):
                    pygame.quit()
                    exit()
                if mouseX in range(int(pa_x), int(pa_x + pa_w)) and mouseY in range(int(pa_y), int(pa_y + pa_h)):
                    return False

def gametype():
    while True:
        screen.fill(white)

        mouseX, mouseY = pygame.mouse.get_pos()

        q = textfont.render("Player vs Player", 1, (black))
        bu_w, bu_h = 420, 50
        bu_x, bu_y = w / 2 - bu_w / 2, (h / 2 - bu_h / 2) + 50
        q_w, q_h = q.get_rect().width, q.get_rect().height

        s = textfont.render("Player vs CPU", 1, (black))
        pa_w, pa_h = 350, 50
        pa_x, pa_y= w / 2 - pa_w / 2, (h / 2 - pa_h / 2) - 50
        s_w, s_h = s.get_rect().width, s.get_rect().height


        if mouseX in range(int(pa_x), int(pa_x + pa_w)) and mouseY in range(int(pa_y), int(pa_y + pa_h)):
            pygame.draw.rect(screen, (light_grey), (pa_x, pa_y, pa_w, pa_h))
            screen.blit(s, [w / 2 - s_w / 2, h / 2 - s_h / 2 - 50])
        else:
            pygame.draw.rect(screen, (grey), (pa_x, pa_y, pa_w, pa_h))
            screen.blit(s, [w / 2 - s_w / 2, h / 2 - s_h / 2 - 50])

        if mouseX in range(int(bu_x), int(bu_x + bu_w)) and mouseY in range(int(bu_y), int(bu_y + bu_h)):
            pygame.draw.rect(screen, (light_grey), (bu_x, bu_y, bu_w, bu_h))
            screen.blit(q, [w / 2 - q_w / 2, h / 2 - q_h / 2 + 50])
        else:
            pygame.draw.rect(screen, (grey), (bu_x, bu_y, bu_w, bu_h))
            screen.blit(q, [w / 2 - q_w / 2, h / 2 - q_h / 2 + 50])

        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.MOUSEBUTTONUP:
                if mouseX in range(int(bu_x), int(bu_x + bu_w)) and mouseY in range(int(bu_y), int(bu_y + bu_h)):
                    return 1
                if mouseX in range(int(pa_x), int(pa_x + pa_w)) and mouseY in range(int(pa_y), int(pa_y + pa_h)):
                    return 2

        pygame.display.update()


def movement(p1class, player):
    global x1_dir, y1_dir, x2_dir, y2_dir, x1, y1, x2, y2, win1, win2, title
    keys = pygame.key.get_pressed()
    if player == 1:
        if p1class == 'normal' or p1class == 'big':
            if keys[K_d] or keys[K_a]:
                x1_dir += 0.1 if keys[K_d] else -0.1
            else:
                x1_dir *= 0.98

            if keys[K_w] or keys[K_s]:
                y1_dir += 0.1 if keys[K_s] else -0.1
            else:
                y1_dir *= 0.98
        if p1class == 'bull':
            if keys[K_d] or keys[K_a]:
                if keys[K_d]:
                    if x1_dir >= 0:
                        x1_dir += 0.15
                    else:
                        x1_dir += 0.075
                else:
                    if x1_dir <= 0:
                        x1_dir -= 0.15
                    else:
                        x1_dir -= 0.075
            else:
                x1_dir *= 0.98

            if keys[K_w] or keys[K_s]:
                if keys[K_s]:
                    if y1_dir >= 0:
                        y1_dir += 0.15
                    else:
                        y1_dir += 0.075
                else:
                    if y1_dir <= 0:
                        y1_dir -= 0.15
                    else:
                        y1_dir -= 0.075
            else:
                y1_dir *= 0.98
    if player == 2:
        if p1class == 'normal' or p1class == 'big':
            if keys[K_l] or keys[K_j]:
                x2_dir += 0.1 if keys[K_l] else -0.1
            else:
                x2_dir *= 0.98

            if keys[K_i] or keys[K_k]:
                y2_dir += 0.1 if keys[K_k] else -0.1
            else:
                y2_dir *= 0.98
        if p1class == 'bull':
            if keys[K_l] or keys[K_j]:
                if keys[K_l]:
                    if x2_dir >= 0:
                        x2_dir += 0.15
                    else:
                        x2_dir += 0.075
                else:
                    if x2_dir <= 0:
                        x2_dir -= 0.15
                    else:
                        x2_dir -= 0.075
            else:
                x2_dir *= 0.98

            if keys[K_i] or keys[K_k]:
                if keys[K_k]:
                    if y2_dir >= 0:
                        y2_dir += 0.15
                    else:
                        y2_dir += 0.075
                else:
                    if y2_dir <= 0:
                        y2_dir -= 0.15
                    else:
                        y2_dir -= 0.075
            else:
                y2_dir *= 0.98


def main():
    global x1_dir, y1_dir, x2_dir, y2_dir, x1, y1, x2, y2, win1, win2, title, p1class, p2class
    if title == True:
        title = title_screen()
        game_type = gametype()
    while True:
        screen.fill(white)

        if play == True:
            movement(p1class, 1)
            movement(p2class, 2)

            if game_type == 2:
                playerxdistance = abs(centerX - x1)
                playerydistance = abs(centerY - y1)
                distance = math.sqrt(playerxdistance ** 2 + playerydistance ** 2)
                if distance < stageR - 300:
                    if x2 > centerX:
                        x2_dir -= 0.1
                    if x2 < centerX:
                        x2_dir += 0.1
                    if y2 > centerX:
                        x2_dir -= 0.1
                    if y2 < centerX:
                        x2_dir += 0.1
                else:
                    if x1 > x2:
                        x2_dir += 0.1
                    elif x1 < x2:
                        x2_dir -= 0.1
                    if y1 > y2:
                        y2_dir += 0.1
                    elif y1 < y2:
                        y2_dir -= 0.1



            score()
            stage(centerX,centerY)
            char1(p1class)
            char2(p2class)
            x1+=x1_dir
            y1+=y1_dir
            x2+=x2_dir
            y2+=y2_dir
            player_collisions()
            player1out = check_collision(x1,y1)
            player2out = check_collision(x2,y2)
            if player1out:
                reset()
                win2 += 1
                player2win()
            if player2out:
                reset()
                win1 += 1
                player1win()
        else:
            break

        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    title_screen()

        pygame.display.update()
        fpsClock.tick(60)


if __name__ == "__main__":
    main()