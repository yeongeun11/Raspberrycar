import pygame

# pygame 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Movement")

# 색상 정의
white = (255, 255, 255)

# 이미지 로드
blue_image = pygame.image.load("blue_rect.png")