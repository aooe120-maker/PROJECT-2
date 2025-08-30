import time
name = ""
stage = 0 # 작동하는 스테이지
req_like=(50,'<') # (요구 호감도 , '=' : 같을때 '<' : 같거나 높을때 '>' : 같거나 낮을때)
is_couple=False # 커플일때만 발동되는 씬인지

def script(game):
    game.stage += 1
    game.end()