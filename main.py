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

# Уменьшенная скорость движения мишени
target_speed_x = random.choice([-1.5, 1.5])
target_speed_y = random.choice([-1.5, 1.5])

# Счетчики попаданий и промахов
score = 0
misses = 0

# Лимит на промахи и попадания
limit = 10

# Случайный фон
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

font = pygame.font.Font(None, 36)

game_over = False
message = ""

running = True
while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                target_speed_x = random.choice([-1, 1])
                target_speed_y = random.choice([-1, 1])
            else:
                misses += 1

    # Проверка завершения игры
    if score >= limit:
        game_over = True
        message = "Победа! Вы набрали 10 попаданий!"
    elif misses >= limit:
        game_over = True
        message = "Игра окончена! Вы допустили 10 промахов!"

    if not game_over:
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
        score_text = font.render(f"Попадания: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Отображение промахов
        miss_text = font.render(f"Промахи: {misses}", True, (255, 255, 255))
        screen.blit(miss_text, (SCREEN_WIDTH - 150, 10))

    else:
        # Вывод сообщения при завершении игры
        message_text = font.render(message, True, (255, 255, 255))
        text_rect = message_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(message_text, text_rect)

    pygame.display.update()

pygame.quit()
