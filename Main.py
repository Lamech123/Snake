
#! /usr/bin/env python

# A simple worm game, 2nd attempt.

import pygame
import random
from Food import Food
from Worm import Worm

w = 500
h = 500

screen = pygame.display.set_mode((w, h))

clock = pygame.time.Clock()

pygame.mixer.init()
chomp = pygame.mixer.Sound("chomp.wav")

score = 0
worm = Worm(screen)
food = Food(screen)
running = True
while running:

    screen.fill((0, 0, 0))
    worm.move()
    worm.draw()
    food.draw()

    if worm.crashed:
        running = False
    elif worm.x <= 0 or worm.x >= w - 1:
        running = False
    elif worm.y <= 0 or worm.y >= h - 1:
        running = False
    elif food.check(worm.x, worm.y):
        score += 1


    worm.eat()
    chomp.play()

    print "Score: %d" % score

    food.erase()
    food = Food(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            worm.event(event)

pygame.display.flip()
clock.tick(240)