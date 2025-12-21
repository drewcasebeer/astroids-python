import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        new_angle = random.uniform(20, 50)
        first_vector = self.velocity.rotate(new_angle)
        second_vector = self.velocity.rotate(new_angle * -1)
        updated_radius = self.radius - ASTEROID_MIN_RADIUS

        first_asteroid = Asteroid(self.position.x, self.position.y, updated_radius)
        first_asteroid.velocity = first_vector * 1.2

        second_asteroid = Asteroid(self.position.x, self.position.y, updated_radius)
        second_asteroid.velocity = second_vector * 1.2
