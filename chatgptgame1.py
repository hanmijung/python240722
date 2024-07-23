import pygame
import random

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("블록 깨기 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 패들 설정
paddle_width = 400
paddle_height = 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - 50
paddle_speed = 10

# 공 설정
ball_size = 10
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 5
ball_speed_y = -5

# 블록 설정
block_width = 75
block_height = 20
block_color = BLUE
blocks = []
for i in range(8):
    for j in range(6):
        blocks.append(pygame.Rect(i * (block_width + 10) + 35, j * (block_height + 10) + 50, block_width, block_height))

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽과 충돌 처리
    if ball_x <= 0 or ball_x >= screen_width - ball_size:
        ball_speed_x *= -1
    if ball_y <= 0:
        ball_speed_y *= -1

    # 패들과 충돌 처리
    if paddle_y < ball_y + ball_size and paddle_x < ball_x < paddle_x + paddle_width:
        ball_speed_y *= -1

    # 블록과 충돌 처리
    for block in blocks:
        if block.collidepoint(ball_x, ball_y):
            blocks.remove(block)
            ball_speed_y *= -1
            break

    # 공이 바닥에 닿으면 게임 종료
    if ball_y >= screen_height:
        running = False

    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_size)
    for block in blocks:
        pygame.draw.rect(screen, block_color, block)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
SystemExit
