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
    game.p("좋은 아침이네?")
    game.sel("라면 먹고 잤어? 얼굴이..", "니가 말걸어서 더 좋은아침.", "졸리다 말걸지마")
    if game.choice == 1:
        game.p("응^^. 넌 소금을 퍼먹었니?")
        game.p("하.. 그건그렇고! 파이썬 공부한다며. 잘 돼가?")
        game.like -= 5
    elif game.choice == 2:
        game.p("(웬일로 좀 멋있네..)")
        game.p("혹시..파이썬 공부는 잘 돼가?")
        game.like += 5
    else:
        game.p("또 저러네..")
        game.p("됐고. 파이썬 공부는 하긴 했니?")
        game.like -= 5
    game.me("당연히 했지. 문제 내볼래?")
    game.img("thony/greet.png")
    game.p("자신 있나보네~ 좋아 !")
    game.img("thony/idle.png")
    game.p("첫번째 문제!")
    game.img("thony/idle.png")
    game.p("정수를 입력받아 4를 입력했을때 결과가 True인 함수는?")
    game.sel("is_even = lambda a: a%2 == 0; is_even(4)",
             "is_even = lambda a: a%2; is_even(4)",
             "is_even = lambda a: a//2; is_even(4)")
    if game.choice == 1:
        game.img("thony/blush.png")
        game.p("오 짜식 제법인데..")
        game.p("이따 나랑 같이 공부할래?")
        game.p("물어보고 싶은게 많아..")
        game.like += 5
        game.me("그래. 내가 좀 가르쳐줄게 ")
    else:
        game.img("thony/angry.png")
        game.p("뭐시?! 땡 ~ 공부했다더니!")
        game.p("밤새 게임한거 아니고?")
        game.like -= 5
        game.me("(들켰네..)")
        game.me("알거 없어! 가서 청소나해")
    game.img("thony/disap.png")
    game.p("치..심심한데 문제하나 더 낼게")
    game.me("응 얼마든지. 쉽기만 해봐.")
    game.img("thony/idle1.png")
    game.p("나 요즘 다이어트 중이라 헬스 다녀")
    game.p("칼로리 계산을 부탁해!")
    game.p("cal = '200', exercise = 300 \n print(exercise>cal)")
    game.sel("1. True. 종아리 튼실해보이고 좋은데 왜?", "2. False. 지금 팔뚝 건강해보이고 좋은데 왜?","3. Error. 네가 뺄 살이 어디있어? 너 쓰러져")        
    if game. choice == 3:
        game.img("thony/idle1.png")
        game.p("어쭈~ 제법인데")
        game.img("thony/disap.png")
        game.p("요즘 귀멸의 칼날 재밌다는데..")
        game.p("주말에 나랑 보러 가던가! 흥")
        game.like += 5
    
    else:
        game.img("thony/idle1.png")
        game.p("약먹었니?")
        game.img("thony/angry.png")
        game.p("기대한 내가 바보다 바보!")
        game.img("thony/disap.png")
        game.p("에휴 됐고 ~ 주말에 영화나 보자 표 하나 남는데!")
        game.like -= 5
    game.me("(갑자기 왜이러지;)")
    game.me("내 시간되는지 먼저 물어봐야지?")
    game.img("thony/angry.png")
    game.p("아오 이런..ㅆ #%@%@$%$")
    game.me("ㅋㅋㅋㅋㅋㅋㅋ하하 농담이야 농담. 정색하지마")
    game.me("그래 좋아. 영화보고 파이썬이나 실컷 공부하자")
    game.img("thony/disap.png")
    game.p("진짜 사람 화나게 하는데 뭐 있다니까..")

    game.p("")
    game.stage += 1
    game.end()