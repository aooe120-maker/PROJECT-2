import time
# 씬 정보
name = "엔딩"
stage = 5 # 작동하는 스테이지
req_like=(-100,'>')
is_couple=False # 커플일때만 발동되는 씬인지

def script(game):
    game.p("테스트!")
    game.end()