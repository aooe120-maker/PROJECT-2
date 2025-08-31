import time
# 씬 정보
name = "엔딩"
stage = 5 # 작동하는 스테이지
req_like=(-100,'>')
is_couple=False # 커플일때만 발동되는 씬인지

def script(game):
    game.img("blank.png") # 화면에 보일 캐릭터 이미지 변경 (아무것도 없는 이미지파일 : blank.png)
    game.fade_out()
    game.n("써니랑 많은 시간을")
    game.end()