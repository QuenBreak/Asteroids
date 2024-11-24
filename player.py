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
        self.sheild_color = (65, 170, 255)
        self.sheild_strength = 4
        self.PLAYER_TEMP_SPEED = 0

    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen, "gray", self.triangle(),2)
        if self.lives > 1:
            pygame.draw.polygon(screen, self.sheild_color, self.triangle(),self.sheild_strength)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.PLAYER_TEMP_SPEED * dt

    def acceleration(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * (self.PLAYER_TEMP_SPEED + 100) * dt

    def shoot(self):
            if self.timer <= 0:
                bullet = Shot(self.position[0],self.position[1])
                bullet.velocity = (pygame.Vector2(0,1).rotate(bullet.rotation + self.rotation)) * PLAYER_SHOOT_SPEED
                self.timer += PLAYER_SHOOT_COOLDOWN

    def death_check(self):
        if self.invincible_timer > 0:
            return
        self.lives -=1
        self.invincible_timer += PLAYER_IMMUNE_TIME

    def score_down():
        self.score -= 1
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.PLAYER_TEMP_SPEED = PLAYER_SPEED
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
        if self.lives == 2:
            self.sheild_color = (165, 170, 255)
            self.sheild_strength = 3
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
        if keys[pygame.K_LSHIFT]:
            self.acceleration(dt) 
        if keys[pygame.K_F11]:
            pygame.display.toggle_fullscreen()
        if keys[pygame.K_END]:
             sys.exit(f"""
                Goodbye Thanks For Playing!
                Your Score Was {self.score}!
                """)

class Shot(CircleShape):
    def __init__(self, x, y ):
        super().__init__(x, y, SHOT_RADIUS)
        self.timer = 0

    def draw(self,screen):
        pygame.draw.circle(screen,"red",self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
