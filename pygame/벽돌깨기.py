import pygame
import sys
import random
import time

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Breakout Game')

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)

# 폰트 설정
font_large = pygame.font.SysFont(None, 74)
font_small = pygame.font.SysFont(None, 36)

# 공 설정
ball_radius = 10
ball_speed = 7  # 공 기본 속도
ball_color = WHITE
ball_speed_multiplier = 1  # 공 속도 배수

# 패들 설정
paddle_width = 150
paddle_height = 10
paddle_speed = 8

# 벽돌 설정
brick_width = 60
brick_height = 20
brick_gap = 10  # 벽돌 사이 간격
space_above_paddle = 300  # 패들 위 빈 공간

# 아이템 설정
item_active = False
item_type = None
item_start_time = 0
item_duration = 3  # 아이템 지속 시간 (초)
item_effects = ['Increase Ball Size', 'Increase Ball Speed', 'Decrease Ball Speed', 'Add Extra Ball']
showing_roulette = False
roulette_duration = 1  # 룰렛이 돌아가는 시간 (초)

# 게임 상태 변수
game_over = False
game_success = False
consecutive_hits = 0
level = 1
countdown_time = 3  # 카운트다운 시간 (초)
countdown_started = False
countdown_end_time = 0

# 다중 공 리스트
balls = []

def generate_random_bricks():
    global bricks
    bricks = []
    num_bricks = random.randint(1, 100)  # 벽돌의 개수 랜덤 설정
    rows = (screen_height - space_above_paddle) // (brick_height + brick_gap)  # 패들 위 빈 공간을 제외한 최대 행 수
    cols = screen_width // (brick_width + brick_gap)  # 화면의 너비에 기반한 최대 열 수

    placed_bricks = 0
    while placed_bricks < num_bricks:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        brick_rect = pygame.Rect(col * (brick_width + brick_gap) + 35, row * (brick_height + brick_gap) + 35, brick_width, brick_height)
        
        # 패들 위 100픽셀 공간을 제외한 영역에 벽돌 배치
        if brick_rect.bottom <= screen_height - (paddle_height + 10):
            if not any(brick.colliderect(brick_rect) for brick in bricks):
                bricks.append(brick_rect)
                placed_bricks += 1

def reset_game():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, paddle_x, consecutive_hits, balls, level
    # 공 초기 위치 및 속도
    ball_x = screen_width // 2
    ball_y = screen_height - 30
    ball_speed_x = ball_speed * random.choice((1, -1))
    ball_speed_y = -ball_speed

    # 패들 초기 위치
    paddle_x = (screen_width - paddle_width) // 2

    # 벽돌 설정
    generate_random_bricks()

    # 게임 상태 초기화
    global game_over, game_success, consecutive_hits
    game_over = False
    game_success = False
    consecutive_hits = 0

    # 공 리스트 초기화
    global balls
    balls = [{'x': ball_x, 'y': ball_y, 'speed_x': ball_speed_x, 'speed_y': ball_speed_y, 'radius': ball_radius}]

    # 레벨 증가
    level += 1

def reset_item_effects():
    global ball_radius, ball_speed_multiplier, balls, item_active, item_type
    ball_radius = 10
    ball_speed_multiplier = 1
    if item_type == 'Add Extra Ball':
        balls = balls[:1]  # 공 개수를 원래대로 되돌리기
    item_active = False
    item_type = None

def activate_item(item):
    global item_active, item_start_time, ball_radius, ball_speed_multiplier, balls
    item_active = True
    item_start_time = time.time()

    if item == 'Increase Ball Size':
        ball_radius = 20
    elif item == 'Decrease Ball Speed':
        ball_speed_multiplier = 0.5
    elif item == 'Add Extra Ball':
        for _ in range(2):  # 공 2개 추가
            balls.append({'x': ball_x, 'y': ball_y, 'speed_x': ball_speed_x * random.choice([1, -1]),
                          'speed_y': ball_speed_y * random.choice([1, -1]), 'radius': ball_radius})

def spin_roulette():
    global item_type
    roulette_end_time = time.time() + roulette_duration
    while time.time() < roulette_end_time:
        item_type = random.choice(item_effects)
        screen.fill(BLACK)
        roulette_text = font_large.render(f'Item: {item_type}', True, YELLOW)
        roulette_rect = roulette_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(roulette_text, roulette_rect)
        pygame.display.flip()
        pygame.time.delay(100)  # 룰렛 속도 조절

def countdown():
    global countdown_started, countdown_end_time
    countdown_started = True
    countdown_end_time = time.time() + countdown_time

reset_game()

# 메인 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if game_over or game_success:
                retry_button = pygame.Rect(screen_width // 2 - 50, screen_height // 2 + 50, 100, 50)
                if retry_button.collidepoint(mouse_x, mouse_y):
                    reset_item_effects()  # 아이템 효과 초기화
                    reset_game()
                    countdown()  # 게임 재시작 시 카운트다운 시작
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and showing_roulette:
                activate_item(item_type)
                showing_roulette = False

    # 카운트다운 처리
    if countdown_started:
        remaining_time = max(countdown_end_time - time.time(), 0)
        if remaining_time <= 0:
            countdown_started = False
        else:
            screen.fill(BLACK)
            countdown_text = font_large.render(f'Starting in {int(remaining_time)}', True, WHITE)
            countdown_rect = countdown_text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(countdown_text, countdown_rect)
            pygame.display.flip()
            pygame.time.wait(100)  # 100ms 대기
            continue

    # 게임 일시 중지 및 아이템 룰렛 처리
    if showing_roulette:
        spin_roulette()
        activate_item(item_type)
        showing_roulette = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    if not game_over and not game_success:
        # 공 이동 및 충돌 처리
        for ball in balls:
            ball['x'] += ball['speed_x'] * ball_speed_multiplier
            ball['y'] += ball['speed_y'] * ball_speed_multiplier

            # 공 충돌 처리 (화면 경계)
            if ball['x'] - ball['radius'] <= 0 or ball['x'] + ball['radius'] >= screen_width:
                ball['speed_x'] = -ball['speed_x']
            if ball['y'] - ball['radius'] <= 0:
                ball['speed_y'] = -ball['speed_y']

            # 공이 패들과 충돌하는지 확인
            paddle_rect = pygame.Rect(paddle_x, screen_height - paddle_height - 10, paddle_width, paddle_height)
            if paddle_rect.collidepoint(ball['x'], ball['y'] + ball['radius']):
                ball['speed_y'] = -ball['speed_y']

            # 공이 벽돌과 충돌하는지 확인
            for brick in bricks:
                if brick.collidepoint(ball['x'], ball['y']):
                    ball['speed_y'] = -ball['speed_y']
                    bricks.remove(brick)
                    consecutive_hits += 1
                    
                    # 5번 연속 벽돌을 깰 때 아이템 룰렛을 보여줌
                    if consecutive_hits % 10 == 0:
                        showing_roulette = True

        # 게임 종료 조건 처리
        if len(bricks) == 0:
            game_success = True
        if all(ball['y'] > screen_height for ball in balls):
            game_over = True

    # 화면 그리기
    screen.fill(BLACK)

    # 벽돌 그리기
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    # 공 그리기
    for ball in balls:
        pygame.draw.circle(screen, ball_color, (int(ball['x']), int(ball['y'])), ball['radius'])

    # 패들 그리기
    pygame.draw.rect(screen, BLUE, (paddle_x, screen_height - paddle_height - 10, paddle_width, paddle_height))

    # 아이템 효과 및 카운트다운 상태 표시
    if item_active:
        elapsed_time = time.time() - item_start_time
        if elapsed_time > item_duration:
            reset_item_effects()  # 아이템 효과 종료
    if showing_roulette:
        spin_roulette()
        activate_item(item_type)
        showing_roulette = False

    if game_over:
        game_over_text = font_large.render('Game Over', True, WHITE)
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
        retry_button = pygame.Rect(screen_width // 2 - 50, screen_height // 2 + 50, 100, 50)
        pygame.draw.rect(screen, GRAY, retry_button)
        retry_text = font_small.render('Retry', True, BLACK)
        screen.blit(retry_text, (retry_button.x + (retry_button.width - retry_text.get_width()) // 2, retry_button.y + (retry_button.height - retry_text.get_height()) // 2))
    elif game_success:
        success_text = font_large.render('Success', True, WHITE)
        screen.blit(success_text, (screen_width // 2 - success_text.get_width() // 2, screen_height // 2 - success_text.get_height() // 2))

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
