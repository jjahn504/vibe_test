import pygame
import os

# Pygame 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flying UFO")

# 색상 정의
WHITE = (255, 255, 255)

# UFO 이미지 로드 및 크기 조정
# UFO 이미지 파일 경로를 'ufo.png'로 가정합니다.
# 실제 파일 이름과 경로에 맞게 수정하세요.
try:
    # 이미지 파일이 없으면 오류가 발생할 수 있습니다.
    ufo_image = pygame.image.load(os.path.join('.', 'ufo.png'))
    UFO_SIZE = 80
    ufo_image = pygame.transform.scale(ufo_image, (UFO_SIZE, UFO_SIZE))
except pygame.error as e:
    print(f"Error loading image: {e}")
    # 이미지 로드 실패 시 대체 사각형으로 표시
    ufo_image = pygame.Surface([UFO_SIZE, UFO_SIZE])
    ufo_image.fill((100, 200, 100)) # 대체 색상

# UFO 초기 위치 및 속도 설정
ufo_x = WIDTH // 2 - UFO_SIZE // 2 # 화면 중앙
ufo_y = HEIGHT // 4 # 화면 위쪽
ufo_speed_x = 3 # 가로 이동 속도

# 게임 루프를 위한 Clock 설정
clock = pygame.time.Clock()
FPS = 60 # 초당 프레임 수

# 메인 게임 루프
running = True
while running:
    # 1. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. 게임 상태 업데이트 (UFO 움직임)
    ufo_x += ufo_speed_x

    # 화면 경계에 닿으면 방향 전환
    if ufo_x + UFO_SIZE > WIDTH or ufo_x < 0:
        ufo_speed_x *= -1

    # 3. 화면 그리기
    SCREEN.fill(WHITE) # 배경을 흰색으로 채우기
    
    # UFO 그리기
    SCREEN.blit(ufo_image, (ufo_x, ufo_y))

    # 4. 화면 업데이트
    pygame.display.flip()

    # FPS 설정 (프레임 속도 유지)
    clock.tick(FPS)

# Pygame 종료
pygame.quit()
