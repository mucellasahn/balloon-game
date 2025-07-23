
import pygame
import random

pygame.init()

# Ekran ayarları
WIDTH, HEIGHT = 300, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Pop Game")
clock = pygame.time.Clock()

# Yazı tipi
font = pygame.font.SysFont(None, 36)

# Renkler
BALLOON_COLORS = [(255, 0, 0), (0, 128, 255), (0, 255, 0), (255, 0, 255),
                  (255, 165, 0), (128, 0, 128), (64, 224, 208)]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Balon bilgileri
class Balloon:
    def __init__(self):
        self.x = random.randint(20, WIDTH - 20)
        self.y = HEIGHT + random.randint(0, 100)
        self.radius = 20
        self.speed = random.uniform(1.5, 2.5)
        self.color = random.choice(BALLOON_COLORS)
        self.popped = False
        self.pop_timer = 0

    def move(self):
        if not self.popped:
            self.y -= self.speed
        else:
            self.pop_timer += 1

    def draw(self, surface):
        if not self.popped:
            pygame.draw.ellipse(surface, self.color, (self.x - self.radius, self.y - self.radius, 2*self.radius, 2*self.radius))
        else:
            pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.radius + self.pop_timer * 2, 2)

    def is_clicked(self, pos):
        dx = self.x - pos[0]
        dy = self.y - pos[1]
        return dx**2 + dy**2 <= self.radius**2

# Oyun başlangıcı
score = 0
start_time = None
game_over = False
game_started = False
balloons = []

# Ana döngü
running = True
while running:
    screen.fill(WHITE)
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started:
                game_started = True
                start_time = pygame.time.get_ticks()
                balloons = []
                score = 0
                game_over = False
            elif not game_over:
                pos = pygame.mouse.get_pos()
                for b in balloons:
                    if not b.popped and b.is_clicked(pos):
                        b.popped = True
                        score += 1

    if game_started and not game_over:
        # Zaman hesaplama
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        time_left = max(0, 120 - int(elapsed_time))
        if elapsed_time >= 120:
            game_over = True

        # Yeni balon oluşturma
        if random.random() < 0.03:
            balloons.append(Balloon())

        # Balonları hareket ettir ve çiz
        for b in balloons:
            b.move()
            b.draw(screen)

        # Skor ve zaman
        skor_yazi = font.render(f"Score: {score}", True, BLACK)
        screen.blit(skor_yazi, (10, 10))
        zaman_yazi = font.render(f"Time Left: {time_left}", True, BLACK)
        screen.blit(zaman_yazi, (10, 50))

    elif not game_started:
        baslat_yazi = font.render("Click to Start", True, BLACK)
        screen.blit(baslat_yazi, (WIDTH // 2 - baslat_yazi.get_width() // 2, HEIGHT // 2))

    else:
        # Game Over ekranı
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 30))
        final_score_text = font.render(f"Your Score: {score}", True, BLACK)
        screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2 + 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
