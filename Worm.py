import pygame

class Worm:

    def __init__(self, surface):
        self.surface = surface
        self.x = surface.get_width() / 2
        self.y = surface.get_height() / 2
        self.length = 1
        self.grow_to = 50
        self.vx = 0
        self.vy = -1
        self.body = []
        self.crashed = False
        self.color = 255, 255, 0

    def eat(self):
        self.grow_to += 25

    def event(self, event):
        """ Handle keyboard events. """
        if event.key == pygame.K_UP:
            if self.vy == 1: return
                self.vx = 0
                self.vy = -1
        elif event.key == pygame.K_DOWN:
            if self.vy == -1: return
                self.vx = 0
                self.vy = 1
        elif event.key == pygame.K_LEFT:
            if self.vx == 1: return
                self.vx = -1
                self.vy = 0
        elif event.key == pygame.K_RIGHT:
            if self.vx == -1: return
                self.vx = 1
                self.vy = 0

    def move(self):
        """ Move the worm. """
        self.x += self.vx
        self.y += self.vy

        if (self.x, self.y) in self.body:
            self.crashed = True

        self.body.insert(0, (self.x, self.y))

        if (self.grow_to > self.length):
            self.length += 1
        if len(self.body) > self.length:
            self.body.pop()

    def draw(self):
        #for x, y in self.body:
        #    self.surface.set_at((x, y), self.color)
        x, y = self.body[0]
        self.surface.set_at((x, y), self.color)
        x, y = self.body[-1]
        self.surface.set_at((x, y), (0, 0, 0))