from enum import Enum



"""
구현할 아이디어들
enemy.damage_every_turn(   ) # FUNC , 매턴 (    ) 만큼 데미지
enemy.clear() # FUNC , 적의 다음 턴 행동을 무력화
for i in range(   ) # FUNC , 기본적인 for 문


"""




from enum import Enum
import operator

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

    def can_play(self, prev_card) -> bool:
        if self._consumed and self.once:
            return False
        if self.condition is None:
            return True
        return bool(prev_card) and prev_card.category == self.condition

    def _parse_cast_str(self, cast_str: str):
        # "player.hp +=" -> ("player", "hp", "+=")
        # "player.somefunc" -> ("player", "somefunc", "call")
            parts = cast_str.split()
            if len(parts) == 1:
                left = parts[0]
                if "." not in left:
                    raise ValueError("cast는 'object.attr' 또는 'object.func' 형식이어야 합니다.")
                target_name, attr = left.split(".", 1)
                # 메서드 호출이면 op_str을 "call"로
                return target_name, attr, "call"
            elif len(parts) == 2:
                left, op_str = parts
                if "." not in left:
                    raise ValueError("cast는 'object.attr OP' 형식이어야 합니다.")
                target_name, attr = left.split(".", 1)
                return target_name, attr, op_str
            else:
                raise ValueError(f"cast 형식 오류: {cast_str}")

    def _resolve_target(self, enemy, player, target_name: str):
        if target_name == "player":
            return player
        if target_name == "enemy":
            return enemy
        raise ValueError(f"알 수 없는 대상: {target_name}, 오타는 아닐지?")

    def _op_func(self, op_str: str):
        table = {
            "+=": operator.add,
            "-=": operator.sub,
            "*=": operator.mul,
            "/=": operator.truediv,
        }
        if op_str not in table:
            raise ValueError(f"지원하지 않는 연산: {op_str}")
        return table[op_str]

    def _post_check(self, target):
        # 대상에 checkhp가 있으면 호출
        if hasattr(target, "checkhp"):
            func = getattr(target, "checkhp")
            if callable(func):
                func()

    def apply(self, enemy, player, arg_value=None):
        """
        반환값
        - VALUE: 계산된 값 반환
        - FUNC/COMB: 변경 후 최종 속성값 반환
        """
        if self.once and self._consumed:
            raise RuntimeError("이 카드는 이미 사용되었습니다.")

        if self.category == Category.VALUE:
            return self._resolve_value(enemy, player, self.cast)

        if self.category == Category.FUNC:
            target_name, attr, op_str = self._parse_cast_str(self.cast)
            target = self._resolve_target(enemy, player, target_name)
            if op_str == "call":
                # 메서드 호출
                func = getattr(target, attr)
                if not callable(func):
                    raise ValueError(f"{attr}는 {target_name}의 메서드가 아닙니다.")
                result = func(arg_value)
                if self.once:
                    self._consumed = True
            return result

        if self.category == Category.COMB:
            # cast 예: ("player.hp +=", 50) 또는 ("player.hp +=", lambda e,p: ...)
            if not (isinstance(self.cast, (tuple, list)) and len(self.cast) == 2 and isinstance(self.cast[0], str)):
                raise ValueError("COMB 카드는 cast에 (op_str, value) 형식이 필요합니다.")
            op_str_val, value_val = self.cast
            target_name, attr, op_str = self._parse_cast_str(op_str_val)
            target = self._resolve_target(enemy, player, target_name)
            cur = getattr(target, attr)
            amount = self._resolve_value(enemy, player, value_val)
            new_val = self._op_func(op_str)(cur, amount)
            setattr(target, attr, new_val)
            self._post_check(target)
            if self.once:
                self._consumed = True
            return new_val

        raise ValueError("잘못된 카테고리.")




#사용 예시입니다

cards = [
	# VALUE: 숫자
	Card(name="10", desc="정수 값", category=Category.VALUE, cast=10, color=Color.WHITE, cost=5),

	# VALUE: 람다
	Card(name="enemy.max_hp / 2", desc="적 최대체력 절반",
	     category=Category.VALUE, cast=lambda e, p: e.max_hp / 2,
	     color=Color.RED, cost=15, is_once=True),
	
    # FUNC의 예시: player.hp +=
	Card(name="player.hp +=", desc="플레이어 힐",
	     category=Category.FUNC, cast="player.hp +=", color=Color.RED, cost=10),
	
	# COMB의 예시: enemy.hp -= 50
	Card(name="enemy.hp -= 50", desc="직접 데미지 50",
	     category=Category.COMB, cast=("enemy.hp -=", 50),
	     color=Color.RED, cost=8),
]
