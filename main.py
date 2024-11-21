# this allows us to use code from
# the open-source pygame library
# throughout this file
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
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, Asteroids)
    AsteroidField.containers = (updatable)
    Asteroid_Field = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)
    # CREATING OBJECTS IN GAME

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
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
        pygame.display.flip()
        dt = clock.tick(60)/1000 

if __name__ == "__main__":
    main()