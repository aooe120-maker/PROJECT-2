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



# 종료
pygame.quit()
sys.exit()
