import sys
import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.timer = 0
        self.score = 0
        self.lives = 3
        self.invincible_timer = 0
        self.health = "green"

    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen, self.health, self.triangle(),2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
            if self.timer <= 0:
                bullet = Shot(self.position[0],self.position[1])
                bullet.velocity = (pygame.Vector2(0,1).rotate(bullet.rotation + self.rotation)) * PLAYER_SHOOT_SPEED
                self.timer += PLAYER_SHOOT_COOLDOWN

    def death_check(self):
        if self.invincible_timer > 0:
            return
        elif self.lives == 1:
            sys.exit(f"""
                Game Over!
                Your Score Was {self.score}!
                """)
        elif self.lives > 0:
            self.lives -=1
            self.invincible_timer += PLAYER_IMMUNE_TIME

    def score_down():
        self.score -= 1
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.lives == 2:
            self.health = "yellow"
        elif self.lives == 1:
            self.health = "red"
        if self.invincible_timer > 0:
            self.invincible_timer -= dt
        if self.timer > 0:
            self.timer -= dt
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_F11]:
            pygame.display.toggle_fullscreen()
        if keys[pygame.K_END]:
             pygame.QUIT()

class Shot(CircleShape):
    def __init__(self, x, y ):
        super().__init__(x, y, SHOT_RADIUS)
        self.timer = 0

    def draw(self,screen):
        pygame.draw.circle(screen,"green",self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
