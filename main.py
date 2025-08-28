import pygame
import sys
import random
from bridge import UIBridge
from game import Game
import scene

class Status:
    MENU_MAIN = 0
    IN_GAME = 1
    MENU_DEBUG = 2

class GameLoop:
    def __init__(self):
        pygame.init()
        self.screen_width = 1024 // 2
        self.screen_height = 1536 // 2
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("도키도키 파이썬")
        self.clock = pygame.time.Clock()
        self.running = True
        self.status = Status.MENU_MAIN
        self.d_alpha = 0
        self.is_fading = False
        self.is_unfading = False

        # 색상
        self.white = (247, 247, 247)
        self.black = (0, 0, 0)
        self.text_color = self.white
        self.box_color = (0, 0, 0, 180)  # 반투명
        self.button_color = (51, 56, 160, 180)
        self.button_hover_color = (252, 198, 29, 180)
        self.button_border_color = self.white
        self.shadow_color = (50, 50, 50, 50)
        self.name_plate_color = (255, 255, 255)

        # 폰트
        try:
            self.button_font = pygame.font.Font("font/font.otf", 20)
            self.text_font = pygame.font.Font("font/font.otf", 24)
            self.name_font = pygame.font.Font("font/font.otf", 22)
        except FileNotFoundError:
            self.button_font = pygame.font.Font(None, 30)
            self.text_font = pygame.font.Font(None, 24)
            self.name_font = pygame.font.Font(None, 24)

        # 리소스
        self.menu_background = self.safe_load_image('sprites/cover.jpg', scale_to=(self.screen_width, self.screen_height))
        self.logo_image = self.safe_load_image('sprites/logo.png', alpha=True)
        self.logo_rect = self.logo_image.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 150)) if self.logo_image else None

        # IN_GAME용 동적 리소스
        self.bg_cache = {}
        self.char_cache = {}
        self.current_bg_path = ""
        self.current_img_path = ""
        self.current_bg = None
        self.current_char = None

        # 메뉴 버튼
        self.buttons = []
        self.create_main_menu_buttons()

        # 브리지/게임
        self.bridge = UIBridge()
        self.game = Game(self.bridge)
        scene.game = self.game

        # 대화 UI 레이아웃
        self.dialog_box_rect = pygame.Rect(20, self.screen_height - 200, self.screen_width - 40, 150)
        self.text_rect = pygame.Rect(self.dialog_box_rect.x + 16, self.dialog_box_rect.y + 48, self.dialog_box_rect.width - 32, self.dialog_box_rect.height - 60)
        self.name_plate_rect = pygame.Rect(self.dialog_box_rect.x + 16, self.dialog_box_rect.y - 26, 200, 26)

        # 페이드
        self.fade_rect = pygame.Rect(0,self.screen_height,self.screen_width,0)
        self.fade_alpha = 0

        # 타이핑 이펙트
        self.typing_full = ""
        self.typing_len = 0
        self.typing_speed = 60.0  # cps
        self.last_mode = ""
        self.last_text_fingerprint = ("", "")

        # 선택지 버튼 동적 리스트
        self.choice_buttons = []
        self.choice_last_labels = ()

    def safe_load_image(self, path, alpha=False, scale_to=None):
        try:
            img = pygame.image.load(path)
            img = img.convert_alpha() if alpha else img.convert()
            if scale_to:
                img = pygame.transform.smoothscale(img, scale_to)
            return img
        except Exception:
            return None

    def create_main_menu_buttons(self):
        button_width = 280
        button_height = 70
        button_x = (self.screen_width - button_width) // 2
        button_y_start = self.screen_height // 2

        self.buttons = [
            Button("게임 시작", button_x, button_y_start, button_width, button_height, self.button_color, self.button_hover_color, self.button_border_color, self.shadow_color, self.start_game),
            Button("불러오기", button_x, button_y_start + 90, button_width, button_height, self.button_color, self.button_hover_color, self.button_border_color, self.shadow_color, self.load_game),
            Button("나가기", button_x, button_y_start + 180, button_width, button_height, self.button_color, self.button_hover_color, self.button_border_color, self.shadow_color, self.exit_game)
        ]

    def start_game(self):
        self.status = Status.IN_GAME
        self.game.play()

    def load_game(self):
        print("불러오기 버튼 클릭됨")

    def exit_game(self):
        self.running = False


    # 실행 (메인함수)
    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0
            self.handle_events()
            self.update(dt)
            self.draw()
        pygame.quit()
        sys.exit()

    # 디버그 진입
    def _start_debug_scene(self, scene_obj):
        self.status = Status.IN_GAME
        self.bridge.state.mode = "idle"
        self.game.current_scene = scene_obj
        self.game.played_scenes.append(scene_obj)

        import threading
        t = threading.Thread(target=scene_obj.play, daemon=True)
        t.start()
    
    # 이벤트 핸들러
    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos() # 마우스 좌표받기
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False # 종료
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.status == Status.MENU_MAIN:
                    for b in self.buttons:
                        if b.is_hovered:
                            b.handle_click()
                elif self.status == Status.MENU_DEBUG:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        for b in self.debug_buttons:
                            if b.is_hovered:
                                b.handle_click()
                    mouse_pos = pygame.mouse.get_pos()
                    for b in self.debug_buttons:
                        b.check_hover(mouse_pos)
                elif self.status == Status.IN_GAME:
                    state = self.bridge.get_state()
                    if state.mode == "text" and self.dialog_box_rect.collidepoint(mouse_pos):
                        if self.typing_len < len(self.typing_full):
                            self.typing_len = len(self.typing_full)
                        else:
                            self.bridge.ui_next()
                    elif state.mode == "choice":
                        for b in self.choice_buttons:
                            if b.is_hovered:
                                b.handle_click()
                                break
                #키보드 입력 처리
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F2:
                    self.status = Status.MENU_DEBUG
                    self.debug_buttons:Button = self._build_debug_scene_buttons()
        if self.status == Status.MENU_MAIN:
            for b in self.buttons:
                b.check_hover(mouse_pos)
        elif self.status == Status.IN_GAME:
            state = self.bridge.get_state()
            if state.mode == "choice":
                for b in self.choice_buttons:
                    b.check_hover(mouse_pos)
    def update(self, dt: float):
        if self.status != Status.IN_GAME:
            return
        state = self.bridge.get_state()
        if state.bg != self.current_bg_path:
            self.current_bg_path = state.bg
            if self.current_bg_path:
                self.current_bg = self.bg_cache.get(self.current_bg_path)
                if not self.current_bg:
                    img = self.safe_load_image(self.current_bg_path, alpha=False)
                    if img:
                        self.current_bg = pygame.transform.smoothscale(img, (self.screen_width, self.screen_height))
                        self.bg_cache[self.current_bg_path] = self.current_bg
        if state.img != self.current_img_path:
            self.current_img_path = state.img
            if self.current_img_path:
                self.current_char = self.char_cache.get(self.current_img_path)
                if not self.current_char:
                    img = self.safe_load_image(self.current_img_path, alpha=True)
                    if img:
                        h = self.screen_height
                        w = int(img.get_width() * (h / img.get_height()))
                        self.current_char = pygame.transform.smoothscale(img, (w, h))
                        self.char_cache[self.current_img_path] = self.current_char
        if state.fade == "out" and not self.is_fading:
            self.is_fading = True
            self.is_unfading = False
        elif state.fade == "in" and not self.is_unfading:
            self.is_unfading = True
            self.is_fading = False

        speed = 600  # alpha per second
        if self.is_fading:
            self.fade_alpha = min(255, self.fade_alpha + int(speed * dt))
            if self.fade_alpha >= 255:
                self.is_fading = False
                self.bridge.ui_fade_done()

        if self.is_unfading:
            self.fade_alpha = max(0, self.fade_alpha - int(speed * dt))
            if self.fade_alpha <= 0:
                self.is_unfading = False
                self.bridge.ui_fade_done()

        fingerprint = (state.mode, state.text)
        if fingerprint != self.last_text_fingerprint:
            self.last_text_fingerprint = fingerprint
            self.typing_full = state.text or ""
            self.typing_len = 0

        if state.mode == "text" and self.typing_len < len(self.typing_full):
            self.typing_len = min(len(self.typing_full), self.typing_len + int(self.typing_speed * dt * 1.8))

        if state.mode == "choice":
            labels = tuple(state.options)
            if labels != self.choice_last_labels:
                self.choice_last_labels = labels
                self.choice_buttons = self._build_choice_buttons(labels)
    def _game_over():
        pass

    def _build_choice_buttons(self, labels):
        buttons = []
        if not labels:
            return buttons
        max_width = self.screen_width - 50
        btn_h = 45
        total_h = len(labels) * (btn_h + 10) - 10
        start_y = self.dialog_box_rect.y - 100 - total_h
        x = (self.screen_width - max_width) // 2
        for i, text in enumerate(labels):
            btn = Button(text, x, start_y + i * (btn_h + 10), max_width, btn_h, self.button_color, self.button_hover_color, self.button_border_color, self.shadow_color, action=(lambda idx=i: self.bridge.ui_choose(idx)))
            btn.font = self.button_font
            buttons.append(btn)
        return buttons
    
    def _build_debug_scene_buttons(self):
        buttons = []
        x, y = 100, 100
        w, h = 300, 40
        gap = 10
        for i, sc in enumerate(self.game.all_scenes):
            b = Button(sc.name, x, y + i * (h + gap), w, h,
                self.button_color, self.button_hover_color, self.button_border_color, self.shadow_color,
                action=(lambda s=sc: self._start_debug_scene(s)))
            b.font = self.button_font
            buttons.append(b)
        return buttons

    def draw(self):
        bg = self.current_bg if (self.status == Status.IN_GAME and self.current_bg) else self.menu_background
        if bg:
            self.screen.blit(bg, (0, 0))
        else:
            self.screen.fill(self.black)

        if self.status == Status.MENU_MAIN:
            if self.logo_image and self.logo_rect:
                self.screen.blit(self.logo_image, self.logo_rect)
            for b in self.buttons:
                b.draw(self.screen)
        elif self.status == Status.MENU_DEBUG:
            self.screen.fill((30, 30, 30))
            for b in self.debug_buttons:
                b.draw(self.screen)
        elif self.status == Status.IN_GAME:
            if self.current_char:
                char_rect = self.current_char.get_rect()
                char_rect.bottom = self.screen_height
                char_rect.right = self.screen_width - 20
                self.screen.blit(self.current_char, char_rect)

                if self.fade_alpha > 0:
                    overlay = pygame.Surface((self.screen_width, self.screen_height))
                    overlay.set_alpha(self.fade_alpha)
                    overlay.fill((0, 0, 0))
                    self.screen.blit(overlay, (0, 0))

            self._draw_rounded_rect(self.screen, self.dialog_box_rect, (0, 0, 0, 180), radius=12, border=2, border_color=self.white)
            
            state = self.bridge.get_state()

            if state.speaker:
                self._draw_rounded_rect(self.screen, self.name_plate_rect, (255, 255, 255, 230), radius=10, border=0)
                name_surf = self.name_font.render(state.speaker, True, (30, 30, 30))
                self.screen.blit(name_surf, (self.name_plate_rect.x + 10, self.name_plate_rect.y + 4))

            text_to_show = state.text if state.mode != "text" else state.text[:self.typing_len]
            self._draw_text_wrapped(self.screen, text_to_show, self.text_font, self.white, self.text_rect)

            if state.mode == "choice":
                for b in self.choice_buttons:
                    b.draw(self.screen)
            elif state.mode == "end":
                pass
        pygame.display.flip()

    def _draw_text_wrapped(self, surface, text, font, color, rect, line_spacing=4):
        if not text:
            return
        x, y, w, h = rect
        space_w = font.size(" ")[0]
        line = []
        line_w = 0

        def blit_line():
            nonlocal y, line, line_w
            if not line:
                return
            surf = font.render("".join(line), True, color)
            surface.blit(surf, (x, y))
            y += font.get_linesize() + line_spacing
            line = []
            line_w = 0

        words = text.split(" ")
        for wi, word in enumerate(words):
            word_w = font.size(word)[0]
            if line_w + (space_w if line else 0) + word_w <= w:
                if line:
                    line.append(" ")
                line.append(word)
                line_w += (space_w if line_w else 0) + word_w
            else:
                if not line:
                    for ch in word:
                        ch_w = font.size(ch)[0]
                        if line_w + ch_w <= w:
                            line.append(ch)
                            line_w += ch_w
                        else:
                            blit_line()
                            line.append(ch)
                            line_w = ch_w
                else:
                    blit_line()
                    if font.size(word)[0] <= w:
                        line.append(word)
                        line_w = font.size(word)[0]
                    else:
                        for ch in word:
                            ch_w = font.size(ch)[0]
                            if line_w + ch_w <= w:
                                line.append(ch)
                                line_w += ch_w
                            else:
                                blit_line()
                                line.append(ch)
                                line_w = ch_w
        if line and y + font.get_linesize() <= rect.bottom:
            blit_line()

    def _draw_rounded_rect(self, surface, rect, color_rgba, radius=8, border=0, border_color=(255, 255, 255)):
        s = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        pygame.draw.rect(s, color_rgba, pygame.Rect(0, 0, rect.width, rect.height), border_radius=radius)
        surface.blit(s, rect.topleft)
        if border > 0:
            pygame.draw.rect(surface, border_color, rect, width=border, border_radius=radius)

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
        try:
            self.font = pygame.font.Font("font/font.otf", 25)
        except FileNotFoundError:
            self.font = pygame.font.Font(None, 30)

    def draw(self, screen):
        pygame.draw.rect(screen, self.shadow_color, self.shadow_rect, border_radius=12)
        pygame.draw.rect(screen, self.border_color, self.rect, border_radius=12)
        current_color = self.hover_color if self.is_hovered else self.color
        inner = self.rect.inflate(-6, -6)
        pygame.draw.rect(screen, current_color, inner, border_radius=10)
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