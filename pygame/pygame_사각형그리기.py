import pygame

# pygame 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Recttangular Drawing")

# 색상 정의
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# 사각형 정의
rect1 = pygame.Rect(100, 100, 100, 50)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면을 흰색으로 채우기
    screen.fill(white)

    # 사각형 그리기
    pygame.draw.rect(screen, blue, rect1) # Rect 객체 이용
    pygame.draw.rect(screen, red, (200, 200, 50, 100)) # tuple 자료형 이용 

    # 화면 업데이트

# pygame 종료
pygame.quit()