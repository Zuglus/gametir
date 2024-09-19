import random
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/tir.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.jpg")
target_width = 50
target_height = 50

# Начальная позиция мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Скорость движения мишени
target_speed_x = random.choice([-3, 3])
target_speed_y = random.choice([-3, 3])

# Счетчик попаданий
score = 0

# Случайный фон
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                target_speed_x = random.choice([-3, 3])
                target_speed_y = random.choice([-3, 3])

    # Движение мишени
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка выхода за пределы экрана и изменение направления
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    # Отображение мишени
    screen.blit(target_img, (target_x, target_y))

    # Отображение счета
    score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
