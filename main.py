import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)

    dt = 0  # delta time

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    # my asteroid.split() returns a tuple of 2 values, each a tuple of 3 values with the asteroid properties (radius, position, velocity)
                    try:
                        new_asteroid_1, new_asteroid_2 = asteroid.split() 
                        # if the old asteroid was below min size, split returns None. this will cause a TypeError
                        # upon unpacking, so we need to handle this
                    except TypeError:
                        break

                    asteroidfield.spawn(*new_asteroid_1) 
                    asteroidfield.spawn(*new_asteroid_2)

                    ### From solution code, they use this one line instead of 3 as the split method handles spawning the new asteroids
                    ### it doesn't return the new asteroid values, so there's no unpacking, and no need to handle the TypeError
                    # asteroid.split()  
                    shot.kill()

                    
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000  # limit game's framerate to 60 FPS


if __name__ == "__main__":
    main()
