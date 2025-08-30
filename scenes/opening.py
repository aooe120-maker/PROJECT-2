import time
# 씬 정보
name = "오프닝"
stage = 0 # 작동하는 스테이지
req_like=(-100,'<') # (요구 호감도 , '<' : 이상 '>' 미만)
is_couple=False # 커플일때만 발동되는 씬인지

def script(game):
    all_correct:bool = True # 이런식으로 스크립트 내부에서만 사용할 변수 컨트롤 가능!
    game.img("blank.png") # 화면에 보일 캐릭터 이미지 변경 (아무것도 없는 이미지파일 : blank.png)
    game.fade_out()
    game.n("대화창을 클릭하여 진행하여주세요")
    game.n("팀원마다 씬을 따로 만들어서 말투가 조금씩 다를 수 있습니다!")
    game.n("팀원중 이 씬을 누가 만들었는지 유추하는것도 재밌을겁니다")
    game.n("도키도키 파이썬!")
    game.n("제작: 프로젝트 2팀")
    game.n("내 이름은 김파이")
    game.n("나는 요즘 혼자 코딩을 공부한다")
    game.n("그냥 멋있어보여서 시작했는데 취미로는 괜찮다")
    game.n("코딩이란것을 처음해봐서 그런지 너무 어렵지만 열심히 해보기로 했다")
    game.n("20XX년 8월 20일 오즈고등학교 3-2반")
    game.background("classroom.jpg")
    game.img("other/teacher.png")
    game.fade_in()
    game.other("여러분들 과제가 좀 부족하시죠?", "담임선생님")
    game.n("교과목 수학의 담임선생님이다. 자꾸 어려운 수학과제를 수행평가로 내주신다...")
    game.other("네니요....", "반아이들")
    game.other("추가 과제 드리겠습니다!","담임선생님")
    game.other("다음주까지 제출해주세요","담임선생님")
    game.n("반이 순식간에 탄식으로 가득 찼다")
    game.other("그럼 여러분들 오늘도 고생하셨습니다","담임선생님")
    game.other("주말 잘 보내세요!","담임선생님")
    game.n("어제 과제도 다 안끝났는데 큰일났네...")
    game.n("집 가서 어떻게든 다 끝내야지...")
    game.fade_out()
    game.background("school.jpg")
    game.img("blank.png")
    time.sleep(1)
    game.fade_in()
    game.n("학교에서 보내는 시간은 늘 따분하다")
    game.n("새로 시작한 코딩 공부가 학교 공부보단 재밌을지도...")
    game.n("집가면 컴퓨터부터 켜야겠다")
    game.fade_out()
    game.background("day.jpg")
    game.fade_in()
    game.n("화창한 날씨라 걷기 좋은 것 같다") # n = 나레이션 / 혼잣말
    game.img("thony/greet.png") # 화면에 보일 캐릭터 이미지 변경
    game.p("저기, 안녕!") # print()
    game.n("어디서 본거같은데...")
    game.n("같은 학교 학생이었나..?")
    game.me("어.. 안녕?") # 플레이어가 하게 될 대사
    game.img("thony/idle1.png")
    game.p("너 혹시 파이썬 좋아해..?")
    game.sel("누구더라...","파이썬 정말 재밌지","아니 그닥...","파이썬 너무 좋아!") # 선택지
    if game.choice == 1: #받아온 선택지
        game.like -= 1 # 호감도 감도
    elif game.choice == 2:
        game.like += 5 # 호감도 증가
        game.p("파이썬 좋아하는구나!")
        game.p("역시 그럴 줄 알았어")
    elif game.choice == 3:
        game.like -= 3
        game.img("thony/angry.png")
        game.p("!!!!!!!!!!!")
        game.me("왜.. 왜그래...")
        game.img("thony/blush.png")
        game.p("미안.. 나도모르게...")
    elif game.choice == 4:
        game.img("thony/blush.png")
        game.p("!!!!!!!!!!")
        game.me("왜.. 왜그래..")
        game.p("그... 앗 아니야")
        game.p("나도 파이썬 좋아해서... 헤헤")
    game.img("thony/idle1.png")
    game.p("어.. 그게.. 나는 옆반의 써니라고해")
    game.p("가방에 파이썬 교재가 있는걸 봤어 우연히 봤어!")
    game.me("그래서...?")
    game.p("내가 파이썬을 진짜 좋아하거든")
    game.sel("입은 옷을 보니 그래보인다...","그렇구나")
    if game.choice == 1: # 선택지 직후에 바로 choice를 부르지 않아도 2번 선택지를 골랐던것을 불러올 수 있습니다!
        game.p("..? 그게 무슨말이야")
        game.me("어.. 아니야")
        game.n("이녀석 바보인가...")
    game.p("아무튼, 친구하고 싶어서 말 걸었어!")
    game.p("우리 친구하자")
    game.sel("그래!","음...")
    game.p("좋다고? 오늘부터 친구인거다 알았지?")
    game.p("이만 가볼게!")
    game.fade_out()
    game.n("써니는 황급히 앞질러 달려갔다")
    if game.choice == 2: # 선택지 직후에 바로 choice를 부르지 않아도 2번 선택지를 골랐던것을 불러올 수 있습니다!
        game.me("난 아직 친구하겠다고 안했는데...")
    game.img("blank.png")
    game.fade_in()
    game.me("좀 특이한 친구네...")
    game.me("머리가 이상한가...")
    game.fade_out()
    game.n("집에 도착했다")
    game.me("과제 바로 해볼까..?")
    game.me("과제 한번 더럽게 어렵네...")
    game.me("5시간 뒤...")
    game.background("room1.jpg")
    game.fade_in()
    game.me("흐아아암...")
    game.me("슬슬 잘 시간인가")
    game.me("벌써 12시네...")
    game.me("과제 다 못 끝냈는데...")
    game.me("붕어빵... 붕어빵...")
    game.me("됐다 잠이나 자자... 주말에 해야지 뭐...")
    game.n("침대에 눕자마자 잠에 들었다")
    game.fade_out()
    game.n("다음 날...")
    game.background("room1_day.png")
    time.sleep(1)
    game.fade_in()
    game.me("왜 이리 피곤하지...")
    game.me("어제 너무 늦게잤나...")
    game.n("띠링")
    game.n("핸드폰 알림이 울렸다")
    game.img("phone.png")
    game.n("써니...?")
    game.n("써니 : 파이야 안녕!")
    game.n("써니 : 우리 친구하기로 한거 맞지?")
    game.n("써니 : 번호는 수소문 해서 알아냈어!")
    game.n("갑자기 이상한 친구가 생겼네...")
    game.n("대충 답해둘까....")
    game.n("파이 : 그렇구나 잘 부탁해")
    game.n("써니 : 오늘 시간 돼?")
    game.me("너무 갑작스러운데...")
    game.n("써니 : 별거 아니야")
    game.n("써니 : 간단한 파이썬 퀴즈를 낼건데 맞추면 돼!")
    game.n("아직 파이썬 좀 어려운데...")
    game.n("파이 : 그래 한번 맞춰볼게")
    game.n("써니 : 다음 중 반복과 거리가 먼 걸 고르면 돼!")
    game.sel("if","for","while")
    if game.choice == 1:
        game.like += 5
        game.n("써니 : 너무 쉬웠지?")
        game.n("파이 : 그랬을지도")
        game.n("써니 : 그러면 이것도 맞춰봐!")
        game.n("써니 : 다음 중 올바른 변수 선언을 고르면 돼!")
        game.sel("6_number = 6","숫자 = 6","number == 6")
        if game.choice == 1:
            all_correct = False
            game.n("써니 : 틀렸어! 변수명은 숫자로 시작 할 수 없다고!")
            game.n("파이 : 배웠던거 같은데 까먹었었네...")
        elif game.choice == 2:
            game.like += 5
            game.n("써니 : 오~ 파이썬이 유니코드 식별자 인식한다는걸 잘 알고 있네?")
            game.n("써니 : 하지만 가급적 변수명은 영어로 선언하는게 좋아!")
            game.sel("알고있어","나는 한글이 더 좋은데...")
            if game.choice == 1:
                game.n("써니 : 역시 파이구나")
                game.sel("이정돈 껌이지")
            if game.choice == 2:
                game.n("써니 : 영어는 국제적 표준이라고!")
        elif game.choice == 3:
            all_correct = False
            game.n("써니 : 틀렸어! 그건 비교연산자야!")
    elif game.choice == 2 or game.choice == 3:
        all_correct = False
        game.like -= 5
        game.n("써니 : 반복과 거리가 먼 것은 if야!")
        game.n("써니 : 너 아직 기초도 모르는구나!")
        game.n("파이 : 그게 시작한지 얼마 안 돼서...")
    if not all_correct:
        game.n("써니 : 준비한 문제가 좀 더 있는데 지금은 못 풀겠다")
        game.n("파이 : 이거 미안하네")
    game.n("써니 : 용건은 여기까지야!")
    game.n("정말 파이썬을 좋아하는구나...")
    game.n("써니 : 그럼 월요일에 학교에서 보자")
    game.n("써니 : 어려운 문제들 준비할거니깐 파이썬 공부 해둬!")
    game.n("파이 : 나 아직 과제도 다 못 끝냈는걸")
    game.n("써니 : 아무튼!")
    game.n("그냥 이참에 파이썬 좀 더 해볼까...")
    if all_correct:
        game.n("써니 : 그때는 지금처럼 검색해서 답변 못 할껄?")
        game.sel("검색 안 했거든","들켰네...")
        if game.choice == 1:
            game.n("써니 : 그럼 더 더 어려운 문제를 준비 해 두지..")
        elif game.choice == 2:
            game.n("써니 : 으이구")
            game.n("써니 : 파이썬 공부 더 해야돼 알겠지?")
    game.n("파이 : 알겠어")
    game.img("blank.png")
    game.me("일단 밀린 과제부터 끝낼까...")
    game.fade_out()
    game.n("10시간 뒤...")
    game.background("room1.jpg")
    game.fade_in()
    game.me("와 드디어 끝났다...")
    game.me("과제가 뭐 이리 어려운거야...")
    game.me("파이썬 공부까지 하기엔 시간이 늦었네...")
    game.me("내일 해야겠다")
    game.fade_out()
    game.n("다음날")
    time.sleep(2)
    game.fade_in()
    game.me("흐아아암...")
    game.me("오늘은 파이썬 공부 좀 해볼까?")
    game.sel("문제 풀기(과제 문제 복습)","영상 자료 시청(스킵)")
    def answer(answer):
        if game.choice == answer:
            game.n("정답!")
        else:
            game.n("오답..")
        game.n("다음 문제")
    if game.choice == 1:
        game.n("다음 중 14 % 3의 계산 결과로 옳은 것은?")
        game.sel("4","4.6","2","1")
        answer(3)
        game.n("거듭제곱을 올바르게 표현한 식을 골라주세요")
        game.sel("2 ^^ 3","2 ** 3","2 ^* 3","2 ~~ 3")
        answer(2)
        game.n("올바른 print 문의 사용 예는?")
        game.sel('print "Hello"',"print Hello ",'print("Hello")',"print['Hello']")
        answer(3)

    
    elif game.choice == 2:
        game.fade_out()
        game.n("파이썬 학습 영상들을 시청한다")
    game.stage += 1
    game.end()