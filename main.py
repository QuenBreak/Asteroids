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
from text import Text_Box

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    in_out = True

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
    Starting_Menu = Text_Box("freesansbold.ttf", 26, STARTING_TEXT, "white")
    Asteroid_Field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)

    pygame.display.toggle_fullscreen()
    
    #Start Menu
    while in_out == True :
        keys = pygame.key.get_pressed()
        Starting_Menu.show_text( screen, "black")
        if keys[pygame.K_END]:
            sys.exit(f"""
                Goodbye Thanks For Playing!
                """)
        if keys[pygame.K_SPACE]:
            in_out = False
        if keys[pygame.K_F11]:
            pygame.display.toggle_fullscreen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()
 
        # Draws the surface object to the screen.
        pygame.display.update()


    # GAMEPLAY LOOP
    in_out = True
    while in_out == True :
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
                player.death_check()
                if player.lives <= 0:
                    in_out = False
            for b in Shots:  
                if a.collision_check(b):
                    player.score += a.score
                    if a.value == 1:   
                        Asteroid_Field.num_as -= 1
                    a.split()
                    pygame.sprite.Sprite.kill(b)
        pygame.display.flip()
        dt = clock.tick(60)/1000 
    
    #Game Over Screen
    in_out = True
    #Game Over Screen has to go after player so it can use player objects
    Game_Over_Screen = Text_Box("freesansbold.ttf", 26, ENDING_TEXT(player.score) , "white")
    while in_out == True :
        keys = pygame.key.get_pressed()
        Game_Over_Screen.show_text( screen, "black")
        if keys[pygame.K_END]:
            sys.exit(f"""
                Goodbye Thanks For Playing!
                """)
        if keys[pygame.K_SPACE]:
            in_out = False
        for event in pygame.event.get():
 
            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
 
                # deactivates the pygame library
                pygame.quit()
 
                # quit the program.
                quit()
 
        # Draws the surface object to the screen.
        pygame.display.update()


if __name__ == "__main__":
    main()