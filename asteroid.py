import random
import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.score = 1
        if radius <= ASTEROID_MIN_RADIUS:
            self.value = 1
        elif radius == ASTEROID_MAX_RADIUS:
            self.value = 4
        else:
            self.value = 2

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        # Screen Wrap
        if self.position[0] > SCREEN_WIDTH:
            self.position[0] = 0
        if self.position[0] < 0:
            self.position[0] = SCREEN_WIDTH
        if self.position[1] > SCREEN_HEIGHT:
            self.position[1] = 0
        if self.position[1] < 0:
            self.position[1] = SCREEN_HEIGHT
        # Screen Wrap
    
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.value = -self.value
            return
        angle = random.uniform(20,50)
        new_vector1 = pygame.Vector2(self.velocity).rotate(self.rotation + angle)
        new_vector2 = pygame.Vector2(self.velocity).rotate(self.rotation - angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position[0],self.position[1],new_radius)
        new_asteroid2 = Asteroid(self.position[0],self.position[1],new_radius)
        new_asteroid1.velocity = new_vector1 * 1.2
        new_asteroid2.velocity = new_vector2 * 1.2
        new_asteroid1.score = self.score * 2
        new_asteroid2.score = self.score * 2
