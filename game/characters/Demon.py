import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        super().__init__()

        # Load and scale Demon image
        self.image = pygame.image.load(os.path.join('game', 'sprites', 'Demon.png')).convert_alpha()
        self.rect = self.image.get_rect()
                
        scale_factor = int(screen_size[0] * 4) / self.rect.width
        self.image = pygame.transform.rotozoom(self.image, 0, scale_factor)
        self.rect = self.image.get_rect()