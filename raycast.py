__author__ = "Alon B.R."

import pygame
import sys
import random

from settings import *
from wall import Wall
from particle import Particle


class RayCast:
    def __init__(self) -> None:
        self.app = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.run: bool = True

        ##########################################

        self.walls = []

        # adding walls in the edges of the screen

        self.walls.append(Wall(0, 1, WIDTH, 1, (255, 0, 0, 255)))
        self.walls.append(Wall(WIDTH - 1, 0, WIDTH - 1, HEIGHT, (255, 0, 0, 255)))
        self.walls.append(Wall(WIDTH, HEIGHT - 1, 0, HEIGHT - 1, (255, 0, 0, 255)))
        self.walls.append(Wall(0, HEIGHT, 0, 0, (255, 0, 0, 255)))

        # adding random walls
        for i in range(5):
            x1 = random.randint(0, WIDTH)
            x2 = random.randint(0, WIDTH)

            y1 = random.randint(0, HEIGHT)
            y2 = random.randint(0, HEIGHT)
            self.walls.append(Wall(x1, y1, x2, y2))

        self.particle = Particle(pygame.Vector2(500, 500))

    def draw(self) -> None:
        for wall in self.walls:
            wall.draw(self.app)
        self.particle.draw(self.app)

    def play(self) -> None:
        while self.run:

            pygame.display.set_caption(
                f"RayCast by Alon B.R. {round(self.clock.get_fps(),2)} FPS"
            )

            mx, my = pygame.mouse.get_pos()
            self.app.fill(BG_COLOR)

            self.draw()

            self.particle.update(mx, my)

            if SHOW_RAYS:
                self.particle.look(self.walls, self.app)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    sys.exit()

            self.clock.tick()
            pygame.display.update()


if __name__ == "__main__":
    raycast = RayCast()
    raycast.play()
