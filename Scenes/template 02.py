import time
# 씬 정보
name = "교실"
stage = 0 # 작동하는 스테이지
req_like=(200000,'<') # (요구 호감도 , '=' : 같을때 '<' : 같거나 높을때 '>' : 같거나 낮을때)
is_couple=False # 커플일때만 발동되는 씬인지

def script(game):
    game.fade_out()
    game.background("classroom.jpg")
    game.img("thony/idle1.png")
    game.fade_in()
    game.p("좋은아침~")
    game.sel("잘잤니?", "너도 좋은아침", "졸리다 말걸지마")
    if game.choice == 1:
        game.p("응. 파이썬공부는 좀 했어?")
        game.like += 3
    elif game.choice == 2:
        game.p("(멋있다..)파이썬 공부는 잘 돼가?!")
        game.like += 5
    else:
        game.p("(또저러네..)파이썬 공부는 했냐?")
        game.like -= 5
    game.me("당연히 했지. 문제 내볼래?")
    game.stage += 1
    game.end()