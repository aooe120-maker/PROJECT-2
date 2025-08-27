import pygame
import sys
import random
from game import Game
import scene
class Status:
    MENU_MAIN = 0
    MENU_LOAD = 1
    IN_GAME = 2
class GameLoop:
    def __init__(self):
        pygame.init()
        self.screen_width = 1024 / 2
        self.screen_height = 1536 / 2
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("도키도키 파이썬")
        self.clock = pygame.time.Clock()
        self.running = True
        self.status = Status.MENU_MAIN
        # 색상
        self.white = (247, 247, 247)
        self.black = (0, 0, 0)
        self.text_color = self.white
        self.button_color = (51, 56, 160)
        self.button_hover_color = (252, 198, 29)
        self.button_border_color = self.white
        self.shadow_color = (50, 50, 50)
        # 폰트
        try:
            self.button_font = pygame.font.Font("font/font.otf", 25)
        except FileNotFoundError:
            self.button_font = pygame.font.Font(None, 30)
        # 이미지
        self.load_images()
        # 타이틀 신 요소
        self.particles = []
        self.buttons = []
        self.create_main_menu_buttons()
        self.game = Game()
        scene.game = self.game

    def load_images(self):
        try:
            self.background_image = pygame.image.load('sprites/cover.png').convert()
            self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))
            self.logo_image = pygame.image.load('sprites/logo.png').convert_alpha()
            self.logo_rect = self.logo_image.get_rect(center=(self.screen_width / 2, self.screen_height / 2 - 150))
            self.heart_particle_image = pygame.image.load('sprites/heart_particle.png').convert_alpha()
        except pygame.error as e:
            print(f"이미지 로드 오류: {e}")
            self.background_image = pygame.Surface((self.screen_width, self.screen_height))
            self.background_image.fill(self.black)
            self.logo_image = None
            self.heart_particle_image = None

    def create_main_menu_buttons(self):
        button_width = 280
        button_height = 70
        button_x = (self.screen_width - button_width) / 2
        button_y_start = self.screen_height / 2

        self.buttons = [
            Button("게임 시작", button_x, button_y_start, button_width, button_height, self.button_color, self.button_hover_color, self.button_border_color, self.shadow_color, self.start_game),
            Button("불러오기", button_x, button_y_start + 90, button_width, button_height, self.button_color, self.button_hover_color, self.button_border_color, self.shadow_color, self.load_game),
            Button("나가기", button_x, button_y_start + 180, button_width, button_height, self.button_color, self.button_hover_color, self.button_border_color, self.shadow_color, self.exit_game)
        ]

    def start_game(self):
        print("게임 시작 버튼 클릭됨")
        self.game.play()
    def load_game(self):
        print("불러오기 버튼 클릭됨")

    def exit_game(self):
        self.running = False

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in self.buttons:
                        if button.is_hovered:
                            button.handle_click()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.check_hover(mouse_pos)

        if self.heart_particle_image and random.randint(0, 10) == 0:
            x = random.randint(0, int(self.screen_width))
            self.particles.append(Particle(x, -100, self.heart_particle_image.copy()))
        
        self.particles = [p for p in self.particles if p.update()]

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))

        for p in self.particles:
            p.draw(self.screen)

        if self.logo_image:
            self.screen.blit(self.logo_image, self.logo_rect)

        for button in self.buttons:
            button.draw(self.screen)

        pygame.display.flip()

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
        
        # 폰트 설정
        try:
            self.font = pygame.font.Font("font/font.otf", 25)
        except FileNotFoundError:
            self.font = pygame.font.Font(None, 30)

    def draw(self, screen):
        pygame.draw.rect(screen, self.shadow_color, self.shadow_rect, border_radius=15)
        pygame.draw.rect(screen, self.border_color, self.rect, border_radius=15)
        
        current_color = self.hover_color if self.is_hovered else self.color
        inner_rect = self.rect.inflate(-6, -6)
        pygame.draw.rect(screen, current_color, inner_rect, border_radius=12)
        
        text_surf = self.font.render(self.text, True, (247, 247, 247))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_click(self):
        if self.is_hovered and self.action:
            self.action()

if __name__ == '__main__':
    gameloop = GameLoop()
    gameloop.run()