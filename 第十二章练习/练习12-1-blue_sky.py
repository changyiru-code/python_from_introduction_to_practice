import pygame
import sys

class CreateWindow:
    """创建一个背景为蓝色的Pygame窗口"""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (0, 0, 255)

    def display(self):
        """绘制窗口"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            pygame.display.flip()


if __name__ == '__main__':
    window = CreateWindow()
    window.display()
