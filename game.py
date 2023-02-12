#!/bin/python
import sys
import pygame

pygame.init()

size = width, height = 600, 600

black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball = pygame.image.load("intro_ball.gif")

ballrect = ball.get_rect()
print(ballrect)
ballXpos = ballrect.left
ballYpos = ballrect.top

while True:
    ballrect.left = ballXpos
    ballrect.top = ballYpos
    pygame.key.set_repeat(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                ballXpos -= 1
            if event.key == pygame.K_d:
                ballXpos += 1
            if event.key == pygame.K_w:
                ballYpos -= 1
            if event.key == pygame.K_s:
                ballYpos += 1

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
