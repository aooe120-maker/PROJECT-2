# pygame 라이브러리 호출
import pygame
pygame.init()

screen_width = 720 # 창 가로 크기
screen_height = 720 # 창 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 창 띄우기
pygame.display.set_caption("Slay The Python") # 창 제목 설정

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 게임 루프 실행
running = True
while running:
    # 이벤트 핸들러
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # 그리기
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (screen_width // 2, screen_height // 2), 50)

    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
