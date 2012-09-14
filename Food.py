import pygame

class Food:
    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(0, surface.get_width())
        self.y = random.randint(0, surface.get_height())
        self.color = 255, 255, 255

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, 3, 3), 0)

    def erase(self):
        pygame.draw.rect(self.surface, (0, 0, 0), (self.x, self.y, 3, 3), 0)

    def check(self, x, y):
        if x < self.x or x > self.x + 3:
            return False
        elif y < self.y or y > self.y + 3:
            return False
        else:
            return True