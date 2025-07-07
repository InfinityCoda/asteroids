import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    
    def update(self, dt):
        self.position += (self.velocity * dt)


    ### Below code is taken from the solution file
    ### Study this and try to understand how they accomplished this and why it's written this way
    def split(self):
        self.kill()   # first we destroy this asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:    # if it's alreay the smallest type of asteroid 
            return                                # then it won't split and will just return out of the function

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        # set 2 variables for the new asteroids' velocities
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS                        # reduce new asteroid size
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)     # spawn first new asteroid
        asteroid.velocity = a * 1.2       # set velocity using the first random angle, and speed it up
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)     # and repeat
        asteroid.velocity = b * 1.2