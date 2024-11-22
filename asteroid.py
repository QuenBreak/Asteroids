import random
import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        new_vector1 = pygame.Vector2(self.velocity).rotate(self.rotation + angle)
        new_vector2 = pygame.Vector2(self.velocity).rotate(self.rotation - angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position[0],self.position[1],new_radius)
        new_asteroid2 = Asteroid(self.position[0],self.position[1],new_radius)
        new_asteroid1.velocity = new_vector1 * 1.2
        new_asteroid2.velocity = new_vector2 * 1.2
