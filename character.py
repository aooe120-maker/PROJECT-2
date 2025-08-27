class Character():
    def __init__ (self,name:str = "", max_hp:int = 100):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
    def is_alive(self):
        return self.hp > 0
    armor = 0
class Enemy(Character):
    def __init__(self,name:str,max_hp:int,image_path:str,level=int):
        super().__init__(name,max_hp)
        self.name = name
        self.image_path = image_path
        self.level = level
    acts = []

class Player(Character):
    def __init__(self,name:str,max_hp:int):
        super().__init__(name,max_hp)
    cards = []
    lines = []
    mana = 10