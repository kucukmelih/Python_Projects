import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 600))
resume = True
speed = 5
FPS = 120
score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 32)
text = font.render("Score: " + str(score), True, (255, 255, 255))
text_XY = text.get_rect()
text_XY.topleft = (240, 0)

monsterLvl1 = pygame.image.load('monster (1).png')
monsterLvl2 = pygame.image.load('monster (2).png')
monsterLvl3 = pygame.image.load('monster (3).png')
monsterLvl1_XY = monsterLvl1.get_rect(topleft = (0, 0))

ball = pygame.image.load('ball.png')
ball_XY = ball.get_rect(topleft = (0, 0))
ballRect = ball.get_rect(topleft = (0, 0))

while resume:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resume = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and monsterLvl1_XY.left > 0:
        monsterLvl1_XY.x -= speed
    elif key[pygame.K_RIGHT] and monsterLvl1_XY.right < 600:
        monsterLvl1_XY.x += speed
    elif key[pygame.K_UP] and monsterLvl1_XY.top > 0:
        monsterLvl1_XY.top -= speed
    elif key[pygame.K_DOWN] and monsterLvl1_XY.bottom < 600:
        monsterLvl1_XY.bottom += speed

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 255, 0), monsterLvl1_XY, -1)
    pygame.draw.rect(screen, (0, 255, 0), ball_XY, -1)

    if monsterLvl1_XY.colliderect(ball_XY):
        ball_XY.x = random.randint(50, 550)
        ball_XY.y = random.randint(50, 550)
        text = font.render("Score: " + str(score), True, (255, 255, 255))
        score += 1

    if score > 5:
        #monsterLvl1.pygame.image.update('monster (2).png')
     monsterLvl2_XY = monsterLvl2.get_rect(topleft = (monsterLvl1_XY.x - 16, monsterLvl1_XY.y - 16))
     monsterLvl1.set_alpha(0)
     screen.blit(monsterLvl2, monsterLvl2_XY)
     pygame.draw.rect(screen, (0, 255, 0), monsterLvl2_XY, -5)

    if score > 10:
        #monsterLvl1.pygame.image.update('monster (2).png')
     monsterLvl3_XY = monsterLvl3.get_rect(topleft = (monsterLvl2_XY.x - 16, monsterLvl2_XY.y - 16))
     monsterLvl2.set_alpha(0)
     screen.blit(monsterLvl3, monsterLvl3_XY)
     pygame.draw.rect(screen, (0, 255, 0), monsterLvl3_XY, -30)


    screen.blit(monsterLvl1, monsterLvl1_XY)
    screen.blit(ball, ball_XY)
    screen.blit(text, text_XY)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()