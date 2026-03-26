import pygame , random 
W, H = 500,400
SPEED = 5
pygame.init()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption('Collision')
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 72)
bg = pygame.transform.scale(pygame.image.load('desert.jpg.jpg').convert(), (W,H))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((30,20))
        self.image.fill(color)
        self.rect = self = self.image.get_rect(topleft = (random.randint(0,W-30), random.randint(0,H-20)))

    def move(self,dx,dy):
            self.rect.x = max(0, min(W-30, self.rect.x + dx))
            self.rect.y = max(0, min(H-20, self.rect.y + dy))
player = Sprite(pygame.Color('black'))
enemy = Sprite(pygame.Color('red'))
group = pygame.sprite.Group(player, enemy)

running,won = True, False
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_x):
            running = False
    if not won:
        keys = pygame.key.get_pressed()
        dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * SPEED
        dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * SPEED
        player.move(dx,dy)

        if player.rect.colliderect(enemy.rect):
            group.remove(enemy)
            won = True

    screen.blit(bg,(0,0))
    group.draw(screen)

    if won:
        text = font.render('You win!', True, pygame.Color('black'))
        screen.blit(text, ((W - text.get_width()) // 2, (H - text.get_height()) // 2    ))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()
        