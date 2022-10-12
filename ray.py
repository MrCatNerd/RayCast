__author__ = "Alon B.R."

import pygame
import numpy as np
import math

from settings import RAY_DIRECTION_LENGTH_MULTIPLIER, RAY_DIRECTION_THICKNESS

pygame.init()


class Ray:
    def __init__(self, position, angle) -> None:
        self.position = position
        # angle = math.radians(angle)
        self.direction = pygame.Vector2(math.sin(angle), math.cos(angle))
        # self.direction = pygame.math.Vector2.angle_to(
        #     position, pygame.Vector2(angle, angle)
        # )

    def LookAt(self, x, y) -> None:
        self.direction.x = x - self.position.x
        self.direction.y = y - self.position.y

        try:
            # self.direction = self.direction.normalize()
            div = float(
                np.linalg.norm((self.direction.x, self.direction.y))
            )  # i do it because its more accurate (in a fue)
            self.direction.x /= div
            self.direction.y /= div
        except ZeroDivisionError:
            self.direction.x = 1
            self.direction.y = 0

    def draw(self, window: pygame.Surface) -> None:
        pygame.draw.line(
            window,
            (255, 255, 255, 255),
            (
                (self.position.x),
                (self.position.y),
            ),
            (
                (self.direction.x * RAY_DIRECTION_LENGTH_MULTIPLIER + self.position.x),
                (self.direction.y * RAY_DIRECTION_LENGTH_MULTIPLIER + self.position.y),
            ),
            RAY_DIRECTION_THICKNESS,
        )

    def cast(self, wall) -> None:
        # THANKS FOR THE MATH THE CODING TRAIN https://www.youtube.com/c/TheCodingTrain
        x1 = wall.a.x
        y1 = wall.a.y

        x2 = wall.b.x
        y2 = wall.b.y

        x3 = self.position.x
        y3 = self.position.y

        x4 = self.position.x + self.direction.x
        y4 = self.position.y + self.direction.y

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if den == 0:
            return

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if t > 0 and t < 1 and u > 0:
            # pt = pygame.Vector2(x1 + t * (x2 - x1), y1 + t * (y2 - y1))
            pt = pygame.Vector2(0.0, 0.0)
            pt.x = x1 + t * (x2 - x1)
            pt.y = y1 + t * (y2 - y1)
            return pt
        return
