
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
    FUNC = 2  # "enemy.hp -=" , 같은 카드
    COMB = 3 # ("enemy.hp -= 50") 같이 FUNC + VALUE가 이미 결합된 카드
    LOOP = 4 # 루프문 전용
    IF = 5 # if문을 포함하는 카드

class Color(Enum):
    WHITE = 0  # 어디에든 대응 가능한 범용 카드
    RED = 1    # 캐릭터 hp 사칙연산 관련, 높은 값을 가지는 카드
    BLUE = 2   # 특수효과 카드
    YELLOW = 3 # if문과 setter 를 포함하는 카드 (강력하다)

class Func():
    def __init__(self,func:str,is_enemy:bool):
        self.func = func
        self.is_enemy = is_enemy
    def cast(self, target, *args, **kwargs):
        return getattr(target, self.func)(*args, **kwargs)

class Value():
    def __init__(self,e,p,func):
        self.enemy = e
        self.player = p
        self.func = func

class Line():
    def __init__(self,enemy,player):
        self.enemy = enemy
        self.player = player
        pass
    value:Value = None
    func:Func = None
    cards = None
    def runable(self) ->bool:
        return self.code and self.func
    def set_value(self,value,mul=False):
        if mul:
            self.value *= value
        else:
            if self.value:
                self.value += value
            else: self.value = value
    def set_func(self,func):
        if not self.func:
            self.func = func
            self.target = self.enemy if self.func.is_enemy else self.player
            return True
        return False
    def run(self):
        self.func.cast(self.target,self.value)
        pass
    def __str__(self):
        return self.string + "\n"

class IF(Line):
    condition = None
    lines = []
    def runable (self) -> bool:
        try:
            return self.condition()
        except:
            return False
    def run(self):
        for line in self.lines:
            line.run()
class LOOP(Line):
    count = 0
    lines = []
    def runable(self) -> bool:
        return True
class Card:
    def __init__(
        self,
		name: str,
		desc: str = "",
		cat: Category = Category.VALUE,
		cast = 0,
		color: Color = Color.WHITE,
		cost: int = 0,
		is_once: bool = False,
    ):
        self.name = name # 카드의 이름
        self.desc = desc # 카드의 설명
        self.category = cat
        self.cast = cast # VALUE: 값/람다, FUNC: "obj.attr +=", COMB: (op_str, 값/람다)
        self.color = color
        self.cost = cost # 카드의 비용
        self.once = is_once # 적마다 한번만 사용가능