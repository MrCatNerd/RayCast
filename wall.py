import pygame

pygame.init()


class Wall:
    def __init__(self, x1, y1, x2, y2, color: tuple = (255, 255, 255, 255)) -> None:
        self.a = pygame.Vector2(x1, y1)
        self.b = pygame.Vector2(x2, y2)
        self.color: tuple = color

    def draw(self, window: pygame.Surface) -> None:
        pygame.draw.line(window, self.color, self.a, self.b)
