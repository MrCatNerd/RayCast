import pygame
import math

from ray import Ray
from settings import *

pygame.init()


class Particle:
    def __init__(self, position: tuple) -> None:
        self.position = pygame.Vector2(*position)
        self.rays = []

        for a in range(0, 360, 1):
            self.rays.append(Ray(self.position, math.radians(a)))

    def look(self, walls, window: pygame.Surface) -> None:
        for ray in self.rays:
            closest: pygame.Vector2 = None
            record = float("inf")
            for wall in walls:
                pt: pygame.Vector2 = ray.cast(wall)
                if pt:
                    distance = math.hypot(
                        abs(self.position.x - pt.x),
                        abs(self.position.y - pt.y),
                    )
                    if distance < record:
                        record = distance
                        closest = pt

            if closest:
                if SHOW_RAYS:
                    pygame.draw.line(
                        window, (255, 255, 255, 255), self.position, closest
                    )
                if SHOW_INTERESECTION_POINTS:
                    pygame.draw.circle(window, (255, 0, 0, 255), closest, 7)

    def update(self, mx, my):
        self.position.x = mx
        self.position.y = my

    def draw(self, window: pygame.Surface) -> None:
        if SHOW_PARTICLE_CIRCLE:
            pygame.draw.circle(
                window, (255, 255, 255, 255), self.position, PARTICLE_CIRCLE_RADIUS
            )

        if SHOW_RAY_DIRECTION:
            for ray in self.rays:
                ray.draw(window)
