# 씬 정보
name = "오프닝"
stage = 0 # 작동하는 스테이지
req_like=(-100,'>') # (요구 호감도 , '=' : 같을때 '<' : 같거나 높을때 '>' : 같거나 낮을때)
is_couple=False # 커플일때만 발동되는 씬인지

def script(game):
    game.background("sprites/bg/day.jpg")
    game.img("sprites/blank.png") # 화면에 보일 캐릭터 이미지 변경 (아무것도 없는 이미지파일 : blank.png)
    game.n("화창한 날씨다.") # n = 나레이션 / 혼잣말
    game.img("sprites/thony/greet.png") # 화면에 보일 캐릭터 이미지 변경
    game.p("저기, 안녕!") # print()
    game.n("어디서 본거같은데...")
    game.n("같은 수업을 듣는 학생이었나..?")
    game.me("어.. 안녕?") # 플레이어가 하게 될 대사
    game.img("sprites/thony/idle1.png")
    game.p("너 혹시 파이썬 재밌어하니..?")
    game.sel("누구더라...","파이썬 정말 재밌지","좋아하진 않아") # 선택지
    if game.choice == 1: #받아온 선택지
        game.like -= 1 # 호감도 감도
        game.sel("1","2","3")
    elif game.choice == 2:
        game.like += 5 # 호감도 증가
    elif game.choice == 3:
        game.img("sprites/thony/angry.png")
        game.p("!!!!!!!!!!!")
        game.me("왜.. 왜그래...")
        game.img("sprites/thony/blush.png")
        game.p("미안.. 나도모르게...")

    game.img("sprites/thony/idle1.png")
    game.p("나는 써니야 전에 (   )에서 본거같은데...") # 설정미정
    game.me("근데?")
    game.p("가방에 파이썬 교재가 있는걸 봤어")
    game.me("그래서...?")
    game.p("내가 파이썬을 진짜 좋아하거든")
    game.me("그래보인다")
    game.p("그래서! 친구하고 싶어서 말 걸었어!")
    game.stage += 1
    game.end() # 게임오버가 아니라 씬의 종료를 알리는 함수입니다