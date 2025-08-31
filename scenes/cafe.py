name = "카페"
stage = 3 # 작동하는 스테이지
req_like=(200000,'<') # (요구 호감도 , '=' : 같을때 '<' : 같거나 높을때 '>' : 같거나 낮을때)
is_couple=False # 커플일때만 발동되는 씬인지

def script(game):
    game.img("blank.png")
    game.fade_out()
    game.n("씬 작성자 : 최재흥")
    game.background("cafe.jpg")
    game.n("몇 주 뒤")
    game.n("써니와는 쉬는시간마다 찾아오고는 대화를 나누거나,")
    game.n("하굣길을 같이 걷거나 하며 시간을 보냈다")
    game.n("물론 파이썬 공부도 계속 해왔다")
    game.n("누구 덕분에 의욕이 나는 것 같기도")
    game.n("오늘은 써니를 카페에서 만나기로 했다.")
    game.n("카페에 오면 항상..") 
    game.n("생각도 잠시 재촉하는 써니의 말소리가 들린다.")
    game.fade_in()
    game.img("thony/greet.png")
    game.p("파이! 빨리 좀 와 설마 카페에 처음 와보는건 아니겠지?")
    game.n("닥달하면 뭐 빨라지는것도 아닌데...잔소리...")
    game.me("아니야 처음은 아닌데...")
    game.p("그럼 자주 오는 편이야? 넌 왜 그렇게 쭈뼛대는거야 마음에 안 들어??")
    game.n("마음에 안든다는건 아닌데... 그냥 카페는 좀...")
    game.p("대답을 좀 해봐")
    game.sel("카페는 쓸데없이 비싸잖아","사람들이 너무 많은걸 안좋아해..","너가 너무 다그치니까 당황스러워서..")
    if game.choice == 1: #받아온 선택지
        game.like -= 5 #호감도 감소
        game.img("thony/sigh.png")
        game.p("뭐야 너 돈없구나?")
        game.me("아니 그런게 아니라...")
    elif game.choice == 2:
        game.like += 10 #호감도 증가
        game.p("아.. 그런거구나")
        game.me("응..")
    elif game.choice == 3:
        game.like += 5
        game.p("아.. 미안 내가 너무 그랬나?")
        game.me("응.. 조금 혼나는것 같았어")
    game.p("그래도 여기 분위기 좋지 않아?")
    game.me("장소의 가치도 중요하지만 누구랑 함께하냐가 중요하지")
    game.img("thony/Brightly.png")
    game.p("그럼 나랑 자주 오자!")
    game.n("환하게 웃는 써니의 모습에 나도 모르게 미소가 지어진다.")
    game.me("응.. 좋아")
    game.n("따뜻한 햇살이 비추는 카페에서의 시간이 흘러간다.")
    game.p("이렇게 자유로운게 얼마만이야 매일 학교만다니고")
    game.n("어차피 집가도 파이썬만 죽어라 할거면서..뭐가 다르지?")
    game.me("그냥.. 가끔은 이렇게 여유롭게 생각할 시간도 필요한 것 같아")
    game.p("그런가.. 나도 가끔은 여유를 가져야겠다.")
    game.p("아참, 파이썬 공부 같이할래?")
    
    game.sel("정말? 기다렸다구!","아..그래..","난 너랑 노는게 더 좋은데..")
    if game.choice == 1:
        game.like += 10
        game.p("응, 나도 너랑 같이 공부하면 더 열심히 할 수 있을 것 같아")
    elif game.choice == 2:
        game.like -= 5
        game.me("아.. 그래..")
        game.img("thony/stay.png")
        game.p("싫어? 너는 파이썬이싫어!? 별로야!")
    elif game.choice == 3:
        game.like += 5
        game.img("thony/blush2.png")
        game.p("음..파이썬도 좋지만 너랑 노는것도 좋아!")
    game.me("근데 파이썬은 언제부터 좋아한거야?")
    game.img("thony/think.png")
    game.n("...........")
    game.img("thony/greet.png")
    game.p("어렸을때부터 컴퓨터를 좋아했는데 파이썬이 제일 쉬워서 시작했어")
    game.n("나는 시작한지 얼마 안됬는데 자랑하고싶나..?")
    game.img("thony/angry.png")
    game.p("또, 혼자 멍때리면서 무슨생각해? 속으로 내욕했지!?")
    game.n("뭐지 얜..?섬뜩한 기분이 든다")
    game.img("thony/smile.png")
    game.p("아하핫 농담이야 쫄기는!")
    game.p("자... 게임을 시작하지..")
    game.img("thony/work.png")
    game.n("써니는 노트북을 꺼내더니 파이썬 코딩을 시작한다.")
    game.p("그럼 시작할게!?")
    game.n("이게 맞는건진 모르겠지만 나는 반사적으로 고개를 끄덕였다.")
    game.n("별안간 불안한 마음이 엄습했다.")
    game.n("다음중 옳은 표현을 구해보세요!")
    game.sel("컴프리헨션은 이터러블 객체의 원소가 항목 변수에 바인딩된다.","표현식if항목for이터러블in조건문.","if...else는 담을 값을 선택하지않는다")
    if game.choice == 1:
        game.like += 10
        game.img("thony/shy.png")
        game.p("오! 너 좀 친다?")
    elif game.choice == 2:
        game.like -= 5
        game.img("thony/grumpy.png")
        game.p("뒤.질.래.?")
    elif game.choice == 3:
        game.like -= 10
        game.img("thony/stay.png")
        game.p("너 생각보다 파이썬에 관심이 없구나? 조금 실망이야")
    
    game.background("cafe_night.jpg")
    game.n("잠깐의 침묵이 흘렀다...")
    game.n("내가 뭘 잘못했나?")
    game.n("갑자기 써니가 노트북을 덮는다.")
    game.img("thony/blush2.png")
    game.p("미안.. 파이썬을 주제로 대화할 상대가 있다는게 너무 좋아서 그만...")
    game.me("응.. 괜찮아")
    game.img("thony/smile.png")
    game.p("이해해줘서 고마워.")
    game.p("그럼, 우리 그만 갈까?")
    game.n("조용히 고개를 끄덕였다.")

    game.background("street_night.jpg")
    game.n("카페를 나서는데 써니가 갑자기 뒤를 돈다.")
    game.p("오늘 정말 즐거웠어 파이썬도 배우고 너랑도 같이 있고...")
    game.n("!?!?!?!?!?!?!?!?")
    game.img("thony/Hands.png")
    game.n("!?!?!?!?!?!?!?!?")
    game.n("써니가 조용히 내손을 잡았다.")
    game.n("작고 따뜻한 손이 내 손을 부드럽게 감싼다.")
    game.me("응.. 나도 좋았어")
    game.n("놀란 가슴을 진정시키려 애썼다.")
    game.p("그럼, 우리 다음에 또 만나자.")
    game.n("조용히 고개를 끄덕였다.")
    game.img("blank.png")

    game.n("써니가 떠난자리엔..")
    game.n("따뜻한 손의 온기가 한동안 내 손에 남아있었다.")
    game.n("그러다 문득 하늘을 바라봤을때.")
    game.background("moonlight2.jpg")
    game.n("내마음을 대변하듯 밝은 달이 밤하늘을 다삼킬듯 떠 있었다.")
    game.n("그 순간, 모든 것이 멈춘 듯한 기분이 들었다.")
    game.me("아무래도 오늘 잠드는건 무리일지도..")

    game.n("써니의 시점")
    game.background("night.jpg")
    game.img("thony/Think2.png")
    game.n("파이와 함께한 시간들이 떠올랐다.")
    game.p("왠지 앞으로 파이와 함께할 시간들이 기대된다.")
    game.p("아무래도 오늘 잠자긴 글른거 같네")

    game.img("blank.png")
    game.n("...........")
    game.background("moonlight3.jpg")
    game.n("달이 어느새 두사람을 바라보며 환하게 웃었다.")
    game.fade_out()


    game.stage += 1
    game.end() # 게임오버가 아니라 씬의 종료를 알리는 함수입니다