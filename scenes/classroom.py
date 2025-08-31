import time
# 씬 정보
name = "교실"
stage = 1 # 작동하는 스테이지
req_like=(200000,'<') # (요구 호감도 , '=' : 같을때 '<' : 같거나 높을때 '>' : 같거나 낮을때)
is_couple=False # 커플일때만 발동되는 씬인지

def script(game):
    game.img("blank.png")
    game.fade_out()
    game.n("씬 작성자 : 강현정")
    game.n("월요일의 학교...")
    game.n("늦게 잔 탓인지 조금은 피곤한거 같다...")
    game.n("1교시 쉬는시간이 시작하자마자 반의 뒷문이 벌컥 열린다")
    game.n("써니는 시끌벅적한 교실 틈을 비집고 내 앞으로 왔다")
    game.background("classroom.jpg")
    game.img("thony/idle1.png")
    game.fade_in()
    game.n("진짜 바로 찾아오는구나...")
    game.p("안녕~ 좋은 아침이네?")
    game.p("문제 풀 준비는 됐지..?")
    game.sel("혹시 라면 먹고 잤어? 얼굴이..", "니가 말걸어서 더 좋은아침.", "하암..졸리다 말걸지마")
    if game.choice == 1:
        game.p("응^^. 넌 소금을 퍼먹었니?")
        game.p("하.. 그건그렇고! 파이썬 공부한다며. 잘 돼가?")
        game.like -= 5
    elif game.choice == 2:
        game.p("(습관성 플러팅..하지만 멋져)")
        game.p("혹시..파이썬 공부는 잘 돼가?")
        game.like += 5
    else:
        game.p("또 저러네..")
        game.p("됐고. 파이썬 공부는 하긴 했니?")
        game.like -= 5
    game.me("어제 밤새서 했지. 문제 내볼래?")
    game.img("thony/greet.png")
    game.p("오호라~ 자신 있나보네. 좋아 !")
    game.img("thony/idle1.png")
    game.p("첫번째 문제! 틀리면 왕딱밤 간다?")
    game.img("thony/idle1.png")
    game.p("정수를 입력받아 4를 입력했을때 결과가 True인 함수는?")
    game.sel("is_even = lambda a: a%2 == 0; is_even(4)",
             "is_even = lambda a: a%2; is_even(4)",
             "is_even = lambda a: a//2; is_even(4)")
    if game.choice == 1:
        game.img("thony/blush.png")
        game.p("정답! 이건 인정할게.")
        game.p("이따 나랑 같이 공부할래?")
        game.p("물어보고 싶은게 많아..")
        game.p("파이썬만은 아니야.")
        game.like += 5
        game.me("그래. 내가 좀 가르쳐줄게 ")
    else:
        game.img("thony/angry.png")
        game.p("뭐시여?! 땡이다 이자식아. 공부했다더니!")
        game.p("밤새 게임한거 아니고?")
        game.p("넌 딱밤 당첨이다")
        game.like -= 5
        game.n("아 겜한거 들켰네..귀신이 따로없다")
        game.me("알거 없어! 자. 딱밤이나 때려")
        game.n("딱!")
        game.n("파이가 내 이마에 딱밤을 꽂았다.")
        game.me("미치겠다 머리 파인거같아")
    game.img("thony/disap.png")
    game.p("치..심심한데 문제하나 더 낼게")
    game.me("응! 나 아직 배고파. 문제 더 줘.")
    game.img("thony/idle1.png")
    game.p("나 요즘 다이어트 중이라 헬스 다녀")
    game.p("칼로리 계산을 부탁해!")
    game.p("cal = '200', exercise = 300 \n print(exercise>cal)")
    game.sel("1. True. 종아리 튼실해보이고 좋은데 왜?", "2. False. 지금 팔뚝 건강해보이고 좋은데 왜?","3. Error. 네가 뺄 살이 어디있어? 너 쓰러져")        
    if game.choice == 3:
        game.img("thony/idle1.png")
        game.p("..그런소리를 늘 듣긴해")
        game.n("파이의 얼굴이 붉어졌다!")
        game.img("thony/disap.png")
        game.p("요즘 귀멸의 칼날 재밌다는데..")
        game.p("주말에 나랑 보러 가던가! 흥")
        game.like += 5
    else:
        game.img("thony/idle1.png")
        game.p("아 정말 화가 끓어오른다..")
        game.img("thony/angry.png")
        game.p("기대한 내가 바보다 바보! 바보를 넘어 등신이야!")
        game.img("thony/disap.png")
        game.p("에휴 내가참자! 주말에 영화나 보자 표 하나 남는데~")
        game.like -= 5
    game.n("갑자기 왜이러지? 당황스럽다.")
    game.me("내 시간이 되는지 먼저 물어야지.")
    game.img("thony/angry.png")
    game.p("이런..ㅆ1##@$@$%#. 왕딱밤 꽂아줘?")
    game.n("파이의 이두근이 움직인다.")
    game.me("하하하! 농담이야~ 팔 가만둬 무섭다")
    game.me("그래 좋아. 영화보고 파이썬이나 실컷 공부하자")
    game.img("thony/disap.png")
    game.p("진짜 넌 사람 화나게 하는데 뭐 있다니까..")
    game.me("(..그 영화 이미봤는데..)")
    game.n("어쩌면 이 바보한테 호감이 조금 생긴 것 같다")
    game.img("thony/idle1.png")
    game.p("아무튼 주말에 보는거다 알겠지?")
    game.sel("좋아","음...")
    if game.choice == 1:
        game.img("thony/Brightly.png")
        game.p("앗싸~")
        game.n("웃는게 조금 귀여워 보였다")
    elif game.choice == 2:
        game.img("thony/angry.png")
        game.p("뭐야 그 석연치 않은 반응은!")
        game.me("아아앗 알겠어 볼게 볼게")
        game.img("thony/disap.png")
        game.p("보기로 한거다")
        game.me("알겠어 꼭 나올게")
    game.n("쉬는시간의 끝을 알리는 종소리가 울렸다")
    game.img("thony/idle1.png")
    game.p("쉬는 시간이 벌써 끝났네")
    game.p("그럼 가볼게~")
    game.fade_out()
    game.me("뭔가 문제 엄청 낼거같았는데 그런건 아니었네..")
    game.stage += 1
    game.end()