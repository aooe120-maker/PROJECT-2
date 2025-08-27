
from enum import Enum
from character import Character

"""
구현할 아이디어들
enemy.damage_every_turn(   ) # FUNC , 매턴 (    ) 만큼 데미지
enemy.clear() # FUNC , 적의 다음 턴 행동을 무력화
for i in range(   ) # FUNC , 기본적인 for 문
"""


class Category(Enum):
    VALUE = 1 # 10 , 20 같은 값을 가지는 카드
    FUNC = 2  # "enemy.hp -=" , "for i in range (  )" 같은 카드
    COMB = 3 # ("enemy.hp -= 50") 같이 FUNC + VALUE가 이미 결합된 카드


class Color(Enum):
    RED = 0    # 캐릭터 hp 사칙연산 관련, 높은 값을 가지는 카드
    WHITE = 1  # 어디에든 대응 가능한 범용 카드
    BLUE = 2   # 특수효과 카드

class Loop():
    count = 0
    lines = []

class Line():
    target: Character = None
    value = None
    code = None
    func = None
    string = ""
    def set_value(self,value,mul=False):
        if self.value:
            self.value += value
        else: self.value = value
    def set_func():
        return False
    def run():
        pass
    def __str__(self):
        return self.string

class Card:
    value = 0
    def __init__(
        self,
		name: str,
		desc: str = "",
		category: Category = Category.VALUE,
		condition: Category | None = None,
		*,
		cast = 0,
		color: Color = Color.WHITE,
		cost: int = 0,
		is_once: bool = False,
    ):
        self.name = name # 카드의 이름
        self.desc = desc # 카드의 설명
        self.condition = condition # 선행 카드 카테고리 요구사항 (없으면 None)
        self.category = category
        self.cast = cast # VALUE: 값/람다, FUNC: "obj.attr +=", COMB: (op_str, 값/람다)
        self.color = color
        self.cost = cost # 카드의 비용
        self.once = is_once # 적마다 한번만 사용가능