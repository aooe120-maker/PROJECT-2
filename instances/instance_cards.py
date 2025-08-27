from card import *
cards = [
Card(name="1",cat=Category.VALUE, cast=1 ,color=Color.WHITE, cost=1),
Card(name="2",cat=Category.VALUE, cast=2 ,color=Color.WHITE, cost=2),
Card(name="3",cat=Category.VALUE, cast=3 ,color=Color.WHITE, cost=2),
Card(name="4",cat=Category.VALUE, cast=4 ,color=Color.WHITE, cost=4),
Card(name="5",cat=Category.VALUE, cast=5 ,color=Color.WHITE, cost=4),
Card(name="6",cat=Category.VALUE, cast=6 ,color=Color.WHITE, cost=4),
Card(name="7",cat=Category.VALUE, cast=7 ,color=Color.WHITE, cost=4),
Card(name="8",cat=Category.VALUE, cast=8 ,color=Color.WHITE, cost=8),
Card(name="9",cat=Category.VALUE, cast=9 ,color=Color.WHITE, cost=8),
Card(name="10",cat=Category.VALUE, cast=10 ,color=Color.WHITE, cost=8),

Card(name="100",cat=Category.VALUE, cast=100 ,color=Color.RED, cost=10),
Card(name="100",cat=Category.VALUE, cast=200 ,color=Color.RED, cost=25),
Card(name="100",cat=Category.VALUE, cast=300 ,color=Color.RED, cost=40),
Card(name="100",cat=Category.VALUE, cast=400 ,color=Color.RED, cost=50),

Card(name="player.hp +=",cat=Category.FUNC, cast=Func("add_hp",False) ,color=Color.WHITE, cost=5),
Card(name="enemy.hp -=",cat=Category.FUNC, cast=Func("reduce_hp",True) ,color=Color.WHITE, cost=5),
Card(name="player.draw_card(   )",cat=Category.FUNC, cast=Func("draw_card",True) ,color=Color.WHITE, cost=5)
]