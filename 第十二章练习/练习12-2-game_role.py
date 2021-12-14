import pygame
import sys

class CreateWindow:
    """创建一个背景为蓝色的Pygame窗口"""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (0, 0, 0)
        pygame.display.set_caption("Smile Display")  # Set the current window caption

        self.role = Role(self)

    def display(self):
        """绘制窗口"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.role.create()

            pygame.display.flip()


class Role:
    """管理游戏角色的类"""
    def __init__(self, ai_game):
        """初始化游戏角色"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('../alien_invasion/images/smile.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def create(self):
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    window = CreateWindow()
    window.display()
