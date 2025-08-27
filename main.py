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
