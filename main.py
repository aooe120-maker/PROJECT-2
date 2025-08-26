"""
파이썬 코딩 컨셉의 덱빌딩 로그라이크 게임
pygame 라이브러리를 활용합니다

예시 상황)
for i in range(   ) # 카드 시전
10 # 카드 시전
enemy.hp -= # 카드 시전
50 # 카드 시전
적 hp - 500

개요.
죽으면 초기화되는 로그라이크 형식의 덱 빌딩 게임입니다.

게임 세부 규칙:
game의 level은 1부터 시작합니다
해당하는 레벨의 몬스터들중 랜덤으로 한개를 골라 전투를 시작합니다.
플레이어는 게임 시작시 기본 카드 15장을 덱에 가지고 시작합니다 (기본적인 진행이 가능한 사전에 준비한 카드세트로 구성)

(전투 시작)
플레이어가 선공 적이 후공합니다.

(턴 시작)
5장의 카드를 핸드로 뽑습니다.
뽑아야 할 카드가 남았는데 더이상 덱에 카드가 없다면 사용한 카드더미중 is_once 가 False인 카드들을
다시 덱에 셔플하여 추가한 후 남은 드로우를 마칩니다.

(카드)
같은줄엔 같은 색 카드만 사용 할 수 있습니다. (WHITE는 어디든 사용가능)
플레이어의 mana가 카드의 cost보다 높고 현재 작성중인 줄의 문법 상 사용 가능하며 올바른 색상일 경우 시전 가능 합니다.
시전 불가능한 카드의 밝기값을 낮춰 유저에게 표기합니다.
플레이어는 카드를 시전할시 vsc 와 유사한 ui를 가진 입력창에 코드줄로 작성됩니다.
for 같은 다음줄 들여쓰기가 필요한 카드를 사용할시 자동으로 들여써집니다.
for문으로 들여써질때 언제든 들여쓰기를 지울 수 있습니다.
사용한 카드는 사용한 카드 목록으로 이동합니다.
시전한 카드는 실행 전 언제든 undo 가능합니다.

(기타 동작)
플에이어는는 FUNC + VALUE (혹은 COMB)를 완성했을시 줄바꿈을 할 수 있습니다 줄바꿈을 하지 않는다면 VALUE 카드를 추가로 시전하여 값을 추가 할 수 있습니다
'코드가 구동가능할시' 언제든 구동가능 한턴에 여러번도 가능합니다.

사용하지 않은 카드들은 턴 종료시 핸드에 들고있습니다.

(적)


(규칙)
hp가 0 이하가 되면 게임 오버입니다.
적의 hp가 0이하가 되면 승리합니다.
카드풀에서 랜덤한 카드를 5장 보여줍니다. 플레이어는 최대 2장의 카드를 보상으로 선택 하거나 보상을 넘길 수 있습니다.
hp를 정확히 0으로 맞춰서 처치시 3장의 카드를 선택 가능합니다.
3번의 적을 상대 후 level이 상승합니다
"""

import pygame
import random
import sys
from card import Card, Category, Color
from character import Player, Enemy

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Slay The Python")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# 트 설정
font = pygame.font.SysFont('malgungothic', 20)
small_font = pygame.font.SysFont('malgungothic', 14)

# 게임 객체 생성
# 플레이어와 적 객체 생성
player = Player(name="Player", max_hp=100)
enemy = Enemy(name="Slime", max_hp=50, image_path="", level=1) # image_path는 현재 사용되지 않습니다.

# 테스트 카드
all_cards = [
    Card(name="5", category=Category.VALUE, cast=5, color=Color.WHITE, cost=1),
    Card(name="10", category=Category.VALUE, cast=10, color=Color.WHITE, cost=2),
    Card(name="player.hp +=", category=Category.FUNC, cast="player.hp +=", color=Color.RED, cost=3, desc="플레이어 체력 회복"),
    Card(name="enemy.hp -=", category=Category.FUNC, cast="enemy.hp -=", color=Color.RED, cost=2, desc="적에게 데미지"),
    Card(name="enemy.hp -= 20", category=Category.COMB, cast=("enemy.hp -=", 20), color=Color.RED, cost=4, desc="적에게 20 데미지"),
]

# 플레이어의 덱, 핸드, 사용한 카드 목록을 초기화
deck = random.choices(all_cards, k=15) # 시작 덱을 15장으로 구성
random.shuffle(deck)
hand = []
discard_pile = []
player.mana = 10 # 매 턴 시작 시 초기화될 마나

# 게임 상태 변수
selected_card_index = None # 선택된 FUNC 카드의 인덱스
selected_value_card_index = None # 선택된 VALUE 카드의 인덱스
message = "" # 화면에 표시할 메시지

# 함수 정의

def draw_cards(num_to_draw):
    """
    덱에서 카드를 뽑아 핸드로 가져옵니다. 덱이 비면 사용한 카드를 섞어 다시 채웁니다.
    """
    for _ in range(num_to_draw):
        if not deck:
            # 덱이 비었을 경우, 사용한 카드 목록(is_once=False인 카드만)을 섞어서 덱으로 만듭니다.
            for card in discard_pile:
                if not card.is_once:
                    deck.append(card)
            discard_pile.clear()
            random.shuffle(deck)
            if not deck: # 그래도 덱이 비어있으면 더 이상 뽑을 카드가 없음
                return
        hand.append(deck.pop())

def draw_text(text, font, color, surface, x, y):
    # 화면에 텍스트를 그리는 함수
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_game_state():
    # 게임의 현재 상태(플레이어/적 정보, 핸드 등)를 화면에 그림
    screen.fill(WHITE)

    # 플레이어 정보 표시
    draw_text(f"{player.name}: HP {player.hp}/{player.max_hp}", font, BLACK, screen, 20, 20)
    draw_text(f"Mana: {player.mana}", font, BLUE, screen, 20, 50)

    # 적 정보 표시
    draw_text(f"{enemy.name} (Lv.{enemy.level}): HP {enemy.hp}/{enemy.max_hp}", font, BLACK, screen, 550, 20)

    # 덱과 사용한 카드 수 표시
    draw_text(f"Deck: {len(deck)}", font, BLACK, screen, 20, 550)
    draw_text(f"Discard: {len(discard_pile)}", font, BLACK, screen, 120, 550)
    
    # 메시지 표시
    if message:
        draw_text(message, font, RED, screen, 250, 20)

    # 핸드에 있는 카드 표시
    for i, card in enumerate(hand):
        card_rect = pygame.Rect(100 + i * 120, 400, 110, 140)
        pygame.draw.rect(screen, GRAY, card_rect)
        pygame.draw.rect(screen, BLACK, card_rect, 2)
        
        # 카드 정보 표시
        draw_text(card.name, small_font, BLACK, screen, card_rect.x + 5, card_rect.y + 5)
        draw_text(f"Cost: {card.cost}", small_font, BLUE, screen, card_rect.x + 5, card_rect.y + 25)
        if card.desc:
            # 설명이 길 경우 여러 줄로 나누어 표시 (간단한 버전)
            desc_lines = card.desc.split('\n')
            for j, line in enumerate(desc_lines):
                 draw_text(line, small_font, BLACK, screen, card_rect.x + 5, card_rect.y + 50 + j * 15)

# --- 메인 게임 루프 ---
draw_cards(5) # 게임 시작 시 5장의 카드를 뽑습니다.
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 카드 클릭 처리
            for i, card in enumerate(hand):
                card_rect = pygame.Rect(100 + i * 120, 400, 110, 140)
                if card_rect.collidepoint(event.pos):
                    message = "" # 메시지 초기화
                    # 카드를 사용하기에 마나가 충분한지 확인
                    if player.mana >= card.cost:
                        # COMB 카드는 즉시 발동
                        if card.category == Category.COMB:
                            try:
                                card.apply(enemy, player)
                                player.mana -= card.cost
                                discard_pile.append(hand.pop(i))
                                message = f"'{card.name}' 사용!"
                            except Exception as e:
                                message = f"사용 불가: {e}"
                            break # 한 번에 한 카드만 사용
                        
                        # FUNC 카드를 선택한 경우
                        elif card.category == Category.FUNC:
                            selected_card_index = i
                            message = f"'{card.name}' 선택. 사용할 숫자(VALUE) 카드를 고르세요."

                        # VALUE 카드를 선택했고, 이전에 FUNC 카드가 선택된 상태일 경우
                        elif card.category == Category.VALUE and selected_card_index is not None:
                            func_card = hand[selected_card_index]
                            value_card = card
                            
                            # FUNC + VALUE 조합 비용 계산
                            total_cost = func_card.cost + value_card.cost
                            if player.mana >= total_cost:
                                try:
                                    # VALUE 카드의 값을 FUNC 카드에 적용하여 사용
                                    value_to_apply = value_card.apply(enemy, player)
                                    func_card.apply(enemy, player, arg_value=value_to_apply)
                                    
                                    player.mana -= total_cost
                                    
                                    # 사용한 카드들을 discard_pile로 이동
                                    discard_pile.append(hand.pop(selected_card_index))
                                    # pop으로 인해 인덱스가 바뀌었을 수 있으므로 value_card를 다시 찾아서 제거
                                    hand.remove(value_card)
                                    discard_pile.append(value_card)
                                    
                                    message = f"'{func_card.name}{value_to_apply}' 사용!"
                                    selected_card_index = None # 선택 초기화
                                except Exception as e:
                                    message = f"사용 불가: {e}"
                                    selected_card_index = None # 오류 발생 시 선택 초기화
                            else:
                                message = "마나가 부족합니다."
                                selected_card_index = None # 선택 초기화
                            break
                    else:
                        message = "마나가 부족합니다."

    # 게임 상태 업데이트 (적의 턴 등)
    # (아직 적의 턴 로직은 구현되지 않음)

    # 화면 그리기
    draw_game_state()
    pygame.display.flip()

    # 승리/패배 조건 확인
    if not player.is_alive():
        draw_text("패배...", font, RED, screen, 350, 250)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False
    
    if not enemy.is_alive():
        draw_text("승리!", font, GREEN, screen, 350, 250)
        pygame.display.flip()
        pygame.time.wait(3000)
        # (다음 스테이지로 넘어가는 로직이 필요)
        running = False # 임시로 게임 종료

# 종료
pygame.quit()
sys.exit()
