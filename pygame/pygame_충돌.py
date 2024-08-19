import pygame

pygame.init()

# 3개의 Rect 객체를 생성
# (x, y, width, height)
rects = [
    pygame.Rect(20, 20, 40, 40),  # 첫 번째 Rect: (20, 20) 위치, 40x40 크기
    pygame.Rect(100, 100, 50, 50),  # 두 번째 Rect: (100, 100) 위치, 50x50 크기
    pygame.Rect(200, 200, 60, 60)  # 세 번째 Rect: (200, 200) 위치, 60x60 크기
]

# 충돌 감지를 수행할 대상 Rect 객체 생성: 파란색 사각형
moving_rect = pygame.Rect(120, 130, 100, 100)  # (120, 130) 위치, 100x100 크기

# moving_rect가 rects 리스트의 어떤 Rect와 충돌하는지 확인
# collidelist 메서드는 충돌한 Rect의 인덱스를 반환. 충돌이 없으면 -1을 반환한다
index = moving_rect.collidelist(rects)

if index != -1:
    # 충돌이 발생한 경우, 충돌한 Rect의 인덱스를 출력
    print(f"moving_rect가 rects[{index}]와 충돌했습니다.")
else:
    # 충돌이 발생하지 않은 경우, 해당 메시지를 출력
    print("충돌이 없습니다.")
