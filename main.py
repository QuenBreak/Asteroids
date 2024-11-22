# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import *
from circleshape import *
from asteroidfield import *
from asteroid import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # CREATING OBJECTS IN GAME
    # Containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Asteroids = pygame.sprite.Group()
    Shots = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, Asteroids)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, Shots)
    Asteroid_Field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)
    # CREATING OBJECTS IN GAME

    # GAMEPLAY LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        for draw in drawable:
            draw.draw(screen)
        for update in updatable:
            update.update(dt)
        for a in Asteroids:
            if player.collision_check(a):
                sys.exit("Game Over!")
        for a in Asteroids:
            for b in Shots:  
                if a.collision_check(b):
                     a.split()
                     pygame.sprite.Sprite.kill(b)
        pygame.display.flip()
        dt = clock.tick(100)/1000 

if __name__ == "__main__":
    main()