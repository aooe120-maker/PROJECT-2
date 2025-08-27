import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
SCREEN_WIDTH = 1024 / 2
SCREEN_HEIGHT = 1536 / 2
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("도키도키 파이썬")

# 색상들 (더 나은 RGB 있으면 넣어주세요!)
WHITE = (247, 247, 247)
BLACK = (0, 0, 0)
TEXT_COLOR = WHITE
BUTTON_COLOR = (51, 56, 160)
BUTTON_HOVER_COLOR = (252, 198, 29)
BUTTON_BORDER_COLOR = (255, 255, 255)
SHADOW_COLOR = (50, 50, 50)


# 폰트 설정
try:
    button_font = pygame.font.Font("font/font.otf", 25)
except FileNotFoundError:
    button_font = pygame.font.Font(None, 30)

# 이미지 로드
try:
    background_image = pygame.image.load('sprites/cover.png').convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    logo_image = pygame.image.load('sprites/logo.png').convert_alpha()
    logo_rect = logo_image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150))
    heart_particle_image = pygame.image.load('sprites/heart_particle.png').convert_alpha()
except pygame.error as e:
    print(f"이미지 로드 오류: {e}")
    background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image.fill(BLACK)
    logo_image = None
    heart_particle_image = None

# 파티클 클래스
class Particle:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.speed = random.uniform(5, 10)
        self.alpha = 255

    def update(self):
        self.y += self.speed
        self.alpha -= 2
        if self.alpha <= 0:
            return False
        self.image.set_alpha(self.alpha)
        return True

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# --- 버튼 클래스 ---
class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, border_color, shadow_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.shadow_rect = pygame.Rect(x + 5, y + 5, width, height)
        self.color = color
        self.hover_color = hover_color
        self.border_color = border_color
        self.shadow_color = shadow_color
        self.text = text
        self.action = action
        self.is_hovered = False

    def draw(self, screen):
        # 그림자
        pygame.draw.rect(screen, self.shadow_color, self.shadow_rect, border_radius=15)
        # 보더
        pygame.draw.rect(screen, self.border_color, self.rect, border_radius=15)
        # 버튼
        current_color = self.hover_color if self.is_hovered else self.color
        inner_rect = self.rect.inflate(-6, -6)
        pygame.draw.rect(screen, current_color, inner_rect, border_radius=12)
        
        text_surf = button_font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_click(self):
        if self.is_hovered and self.action:
            self.action()

# 버튼 액션 함수
def start_game():
    print("게임 시작 버튼 클릭됨")

def load_game():
    print("불러오기 버튼 클릭됨")

def exit_game():
    pygame.quit()
    sys.exit()

# 버튼 인스턴스
button_width = 280
button_height = 70
button_x = (SCREEN_WIDTH - button_width) / 2
button_y_start = SCREEN_HEIGHT / 2

buttons = [
    Button("게임 시작", button_x, button_y_start, button_width, button_height, BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_BORDER_COLOR, SHADOW_COLOR, start_game),
    Button("불러오기", button_x, button_y_start + 90, button_width, button_height, BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_BORDER_COLOR, SHADOW_COLOR, load_game),
    Button("나가기", button_x, button_y_start + 180, button_width, button_height, BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_BORDER_COLOR, SHADOW_COLOR, exit_game)
]


particles = []

#메인 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # 왼쪽 마우스 버튼
                for button in buttons:
                    button.handle_click()
    # 업데이트
    for button in buttons:
        button.check_hover(mouse_pos)
    # 파티클 생성
    if heart_particle_image and random.randint(0, 10) == 0:
        x = random.randint(0, int(SCREEN_WIDTH))
        particles.append(Particle(x, -100, heart_particle_image.copy()))
    # 파티클 업데이트 및 제거
    particles = [p for p in particles if p.update()]
    # 그리기
    screen.blit(background_image, (0, 0))
    # 파티클 그리기
    for p in particles:
        p.draw(screen)
    if logo_image:
        screen.blit(logo_image, logo_rect)
    for button in buttons:
        button.draw(screen)
    pygame.display.flip()
    clock.tick(60)
# --- 종료 ---
pygame.quit()
sys.exit()
