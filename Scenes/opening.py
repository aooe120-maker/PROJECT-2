# 씬 정보
name = "오프닝"
stage = 0 # 작동하는 스테이지
req_like=(-100,'>') # (요구 호감도 , '=' : 같을때 '<' : 같거나 높을때 '>' : 같거나 낮을때)
is_couple=False # 커플일때만 발동되는 씬인지

def script(game):
    game.background("sprites/bg/school.jpg")

    game.n("하교 시간은 늘 따분하다")

    game.n("새로 시작한 코딩 공부가 학교 공부보단 재밌을지도...")

    game.n("집가면 컴퓨터부터 켜야겠다")

    game.background("sprites/bg/day.jpg")

    game.img("sprites/blank.png") # 화면에 보일 캐릭터 이미지 변경 (아무것도 없는 이미지파일 : blank.png)
    game.n("화창한 날씨라 걷기 좋은 것 같다") # n = 나레이션 / 혼잣말

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
    elif game.choice == 2:
        game.like += 5 # 호감도 증가
        game.p("파이썬 좋아하는구나!")
        game.p("역시 그럴 줄 알았어")
    elif game.choice == 3:
        game.like -= 3
        game.img("sprites/thony/angry.png")
        game.p("!!!!!!!!!!!")
        game.me("왜.. 왜그래...")
        game.img("sprites/thony/blush.png")
        game.p("미안.. 나도모르게...")
    
    game.img("sprites/thony/idle1.png")

    game.p("어.. 그게.. 나는 옆반의 써니라고해")

    game.p("가방에 파이썬 교재가 있는걸 봤어")

    game.me("그래서...?")

    game.p("내가 파이썬을 진짜 좋아하거든")

    game.sel("입은 옷을 보니 그래보인다...","그래서 인사했구나")

    game.p("친구하고 싶어서 말 걸었어!")

    game.p("우리 친구하자")

    game.sel("좋아","음...")

    game.p("오늘부터 친구인거다 알았지?")

    game.p("이만 가볼게!")
    
    game.n("써니는 황급히 앞질러 달려갔다")

    if game.choice == 2: # 선택지 직후에 바로 choice를 부르지 않아도 2번 선택지를 골랐던것을 불러올 수 있습니다!
        game.p("난 아직 말도 안했는데...")

    game.stage += 1
    game.end() # 게임오버가 아니라 씬의 종료를 알리는 함수입니다