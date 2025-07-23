import pygame
import random

pygame.init()

ekran = pygame.display.set_mode((300, 400))
pygame.display.set_caption("Balloon Pop Game")

font = pygame.font.SysFont(None, 36)
score = 0

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

game_over = False
running = True
while running:
clock.tick(60)
ekran.fill((173, 216, 230))

elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

for event in pygame.event.get():
if event.type == pygame.QUIT:
running = False

if not game_over:
# Oyun aktifken göstereceğin şeyler
skor_yazi = font.render(f"Score: {score}", True, (0, 0, 0))
ekran.blit(skor_yazi, (10, 10))

kalan_sure = max(0, 120 - int(elapsed_time))
sure_yazi = font.render(f"Time Left: {kalan_sure}s", True, (0, 0, 0))
ekran.blit(sure_yazi, (10, 50))

if elapsed_time >= 120:
game_over = True

# Balonlar vs. burada olacak (senin animasyonlar)

else:
# Oyun bittiğinde gösterilecek ekran
over_text = font.render("Game Over!", True, (255, 0, 0))
score_text = font.render(f"Your Score: {score}", True, (0, 0, 0))
ekran.blit(over_text, (80, 150))
ekran.blit(score_text, (80, 200))

pygame.display.update()

pygame.quit()
