import time
# 씬 정보
name = "오프닝"
stage = 0 # 작동하는 스테이지
req_like=(0,'>') # (요구 호감도 , '<' : 이상 '>' 미만)
is_couple=False # 커플일때만 발동되는 씬인지

def script(game):
    all_correct:bool = True # 이런식으로 스크립트 내부에서만 사용할 변수 컨트롤 가능!
    game.img("blank.png") # 화면에 보일 캐릭터 이미지 변경 (아무것도 없는 이미지파일 : blank.png)
    game.fade_out()
    game.n("대화창을 클릭하여 진행하여주세요")
    game.n("팀원마다 씬을 따로 만들어서 말투가 조금씩 다를 수 있습니다!")
    game.n("씬을 순서대로 만든것이 아니라 상황이 매끄럽지 않을 수 있습니다.")
    game.n("대본쓰는데 2일밖에 없었어서 양해좀 ㅎㅎ;;;;;")
    game.n("도키도키 파이썬!")
    game.n("제작: 프로젝트 2팀")
    game.n("...")
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
    game.sel("파이썬 시험 풀기(14기 과제 문제 복습!)","영상 자료 시청(스킵)")
    answers = 0
    corrects = 0
    def answer(answer):
        if game.choice == answer:
            game.n("정답!")
            corrects += 1
        else:
            game.n("오답..")
            game.me("이런....")
        answers += 1
        game.n("다음 문제")
    if game.choice == 1:
        game.n("다음 중 14 % 3의 계산 결과로 옳은 것을 골라주세요")
        game.sel("4","4.6","2","1")
        answer(3)
        game.n("거듭제곱을 올바르게 표현한 식을 골라주세요")
        game.sel("2 ^^ 3","2 ** 3","2 ^* 3","2 ~~ 3")
        answer(2)
        game.n("올바른 print 문의 사용 예는?")
        game.sel('print "Hello"',"print Hello ",'print("Hello")',"print['Hello']")
        answer(3)
        game.n("변수를 생성하는 방법으로 올바른 것을 골라주세요")
        game.sel("number == 20","100 == number","number(7)","number = 7")
        answer(4)
        game.n("다음 중 변수 이름으로 사용 할 수 있는것을 골라주세요")
        game.n("78abc","_aBc","for","abc%2")
        answer(2)
        game.n("다음 중 int로 선언 된 것을 골라주세요")
        game.sel("a = 7.0","a = 7810","a = float(10)")
        answer(2)
        game.n("type(3.0 + 7.0)의 결과로 올바른 것을 골라주세요")
        game.sel("<class 'float>","10","10.0","<class int>")
        answer(1)
        game.n("비교 연산자의 결과로 올바르지 않은 것을 골라주세요")
        game.sel("8 == 2 * 4 (True)","4 != 2 + 2(False)","2 * 3 is 3 + 3(True)","8 is 4 * 2.0(True)")
        answer(2)
        game.n("안녕 and True의 결과로 올바른 것을 골라주세요")
        game.n("False","안녕","True","None")
        answer(3)
        game.n("x는 5와 같지 않다 라는 뜻과 동일한 것을 골라주세요")
        game.sel("x <= 5","x != 5","x & 5","x ! 5")
        answer(2)
        game.n("논리 연산의 결과를 뒤집는 연산자를 골라주세요")
        game.sel("is not","not","!=","end","and","or")
        answer(2)
        game.n(f"맞춘 문제: {corrects}개")
        game.n(f"틀린 문제: {answers - corrects}개")
        game.n(f"전체 문제: {answers}개")
        game.n("써니한테 문제 푼거 공유할까...")
        game.sel("공유한다")
        game.img("phone.png")
        score = int(corrects / answers * 100)
        if game.choice == 1:
            game.n(f"파이 : 파이썬 온라인 시험 쳐서 {score}점 받았어")
            if score >= 85:
                game.like += corrects
                game.n("써니 : 오 잘했는데?")
                game.n("써니 : 공부해달라고 진짜 할줄은 몰랐어")
                game.sel("그래도 소중한 친구의 부탁인데 들어줘야지","심심해서 했어")
                if game.choice == 1:
                    game.like += 5
                    game.n("써니 : 진짜? 감동이다")
                if game.choice == 2:
                    game.n("써니 : 그래도 감동인걸")
            elif score >= 65:
                game.like += 3
                game.n("써니 : 열심히 했구나!")
                game.n("써니 : 조금은 분발 해야겠어!")
                game.n("파이 : 열심히 푼거라고!")
                game.n("써니 : ㅋㅋㅋㅋ 미안")
            else:
                game.like += 1
                game.n("써니 : 노력은 했구나...")
                game.n("파이 : 응...")
                game.n("써니 : 내일 문제 난이도 좀 낮춰줄까..?")
                game.sel("아니","응")
                if game.choice == 2:
                    game.n("써니 : 그런건 없다! 이미 문제는 다 만들어놨어")
                    game.n("파이 : 그럼 왜 물어본거야 ㅋㅋ")
    elif game.choice == 2:
        game.fade_out()
        game.n("파이썬 학습 영상들을 시청한다")
        game.fade_in()
        game.me("후우 공부가 많이 됐다")
        game.n("띠링")
        game.n("핸드폰 알림이 울렸다")
        game.img("phone.png")
        game.n("써니네... 무슨 용건이지?")
        game.n("써니 : 안녕")
        game.n("파이 : 안녕")
        game.n("써니 : 파이썬 공부는 했니..?")
        game.sel("물론이지","많이는 못 했어")
        game.n("써니 : 그래? 내일 내가 내는 문제 풀 자신 있어?")
        game.sel("자신있어!","음....")
        if game.choice == 1:
            game.like += 5
            game.n("써니 : 자신있다니...")
        elif game.choice == 2:
            game.n("써니 : 뭐가 그 반응은!")
            game.n("파이 : 노력은 해볼게")
    game.n("써니 : 바로 옆반이지?")
    game.n("파이 : 그럴껄?")
    game.n("써니 : 내일 쉬는시간에 찾아간다!")
    game.n("파이 : 긴장해야겠는걸")
    game.n("써니 : 그럼 내일 학교에서 보자!")
    game.n("파이 : 그래 내일 봐")
    game.n("이 녀석에게 거리감이란 뭘까...")
    game.n("괜히 말려드는거 같은 기분...")
    game.n("그래도 싫지만은 않다")
    game.n("써니랑 조금은 친해 진 것 같다...")
    game.n("남은 시간동안 뭘 할까")
    game.sel("당연히 파이썬 공부","어제 못한 게임")
    if game.choice == 1:
        game.mental -= 10
        game.fade_out()
        game.n("파이썬 공부를 열심히 하며 하루를 보냈다")
        time.sleep(1)
    if game.choice == 2:
        game.mental += 10
        game.fade_out()
        game.n("휴식도 필요한법. 공부도 했겠다 게임정도는 해도 되잖아?")
        time.sleep(1)
    game.n("다음 날")
    game.stage += 1
    game.end()