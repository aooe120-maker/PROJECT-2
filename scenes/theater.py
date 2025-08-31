import time
# 씬 정보
name = "영화"
stage = 0 # 작동하는 스테이지
req_like=(-100,'<') # (요구 호감도 , '<' : 이상 '>' 미만)
is_couple=False # 커플일때만 발동되는 씬인지

def script(game):
    # 화면에 보일 캐릭터 이미지 변경 (아무것도 없는 이미지파일 : blank.png)
 
    game.background("cgv.jpg")
    game.img("thony/grumpy.png")
    game.p("왜이렇게 늦어! 아주 습관성이야")
    game.sel("어제부터 너무 떨려서 잠을 못잤어","넌 팝콘도 안사놓고 뭐해? 센스가 꽝이다")
    if game.choice == 1:
        game.background("cgv.jpg")
        game.img("thony/think.png")
        game.p("왜떨어. 내가 너 잡아먹니?")
        game.img("thony/shy.png")
        game.me("하하 그러게.")
        game.like += 5
    else:
        game.background("cgv.jpg")
        game.img("thony/sigh.png")
        game.p("팝콘 말고.. 주먹을 먹여줄게")
        game.like -= 5
        game.me("장난이야 장난. 미안해 어제 떨려서 잠을 못잤어")
    

    game.img("thony/smile.png")
    game.p("또 밤새 게임한건 아니고?")
    game.n("파이는 귀신이 맞다!")
    game.img("thony/sigh.png")
    game.p("어휴~ 영화 시작한다. 들어가기나 하자.")
    game.background("movie02.jpg")
    game.img("blank.png")
    game.p("나 너한테 못한말이 있어")
    game.p("사실.. 이런곳 남자랑 처음와봐.")
    game.me("나도 엄마 다음으로 니가 처음이야")
    game.p("영화 곧시작해. 혹시 우리도 시작인건가?")
    game.n("큰일이다. 내 급격한 심장 소리때문에 영화 광고 소리가 묻힌다.")
    game.me("무서우면 내 손 잡는거 허락할게")
    game.p("...")
    game.background("movieo3.jpg")
    game.p("뭐야!")
    game.me("저게뭐야. 또 니가 만든거야?")
    game.img("thony/angry2.png")
    game.p("겠냐? 또 왜저래")
    game.me("미안미안 너 문제광이잖아.")
    game.img("thony/oo.png")
    game.other("안녕하세요 관객여러분. 파이썬Day를 맞아 문제를 준비했습니다.박수!","CGV직원")
    game.n("놀랍도록 고요하다.")
    game.other("맞추시는 분들께는 놀이공원 이용권 2매를 드리니 열심히 참여해주세요!","CGV직원")
    game.img("thony/happy.png")
    game.p("놀이공원 티켓 2장! 받으면 영화공짜다. 안할 이유가없다.")
    game.p("저건 무조건 우리거야")
    game.n("우리? 파이가 우리라고 했다!")
    game.img("thony/oo.png")
    game.other("자 거두절미 하고 바로 문제 쏩니다!", "CGV직원")
    game.background("movie03.jpg")
    game.other("1번. 아래코드를 실행했을 때 출력 결과는?","CGV직원")
    game.other("a=10 \n if a % 2 == 0 and a > 5: \n print('조건 충족') \n else: \n print('조건 불충족')","CGV직원")
    game.sel("조건 불충족", "조건 충족","에러발생")
    if game.choice == 2:
        game.img("thony/oo.png")
        game.other("오 저기 모델 같으신분! 정답입니다~","CGV직원")
        game.img("thony/happy.png")
        game.p("대박! 앞으로 널 파이썬의 신으로 부를게")
        game.me("하하 좋아. 아~ 티켓 두장 맛있다.")
        game.img("thony/ii.png")
        game.p("근데 저분 후하다 모델 이라니")
        game.me("미감이 훌륭하신거같아")
        game.like += 5
    else:
        game.img("thony/oo.png")
        game.other("땡 !땡땡 !~ 완전 땡입니다. 다른분 있나요?","CGV직원")
        game.img("thony/angry2.png")
        game.p("아 뭐해 내 놀이공원 티켓!")
        game.me("아 헷갈렸다. 내가 이런실수를 하다니. 오늘 밤샘 파이썬공부 각이다!")
        game.p("너 다음 문젠 무조건 맞춰야 나랑도 승산있어")
        game.me("알겠어!")
        game.like -= 5
    game.img("thony/oo.png")
    game.other("자. 그럼 두번째 문제 쏩니다!","CGV직원")
    game.other("다음 코드에서 출력되는 결과는?","CGV직원")
    game.other("nums = [1, 2, 3, 4, 5] \n print(nums[1:4])")
    game.sel("[2, 3, 4]","[1, 2, 3]", "[2, 3, 4, 5]")
    if game.choice == 1:
        game.img("thony/oo.png")
        game.other("wow 정답~ 정말 대단해요! ","CGV직원")
        game.img("thony/happy.png")
        game.p("너 뭐야 ? 갑자기 영화관이 밝아졌는데 니 후광이었어")
        game.me("또 비행기 태운다. 그러지마 별거 아니니까.")
        game.p("별거 아니긴! 놀이공원 티켓이 두장! 침나온다")
        game.me("귀엽긴")
        game.like += 5
    else:
        game.img("thony/oo.png")
        game.other("땡땡~땡땡~ 이런이런 ","CGV직원")
        game.img("thony/angry2.png")
        game.p("아 이걸틀려? 이건 왕딱밤 각이다")
        game.me("원숭이도 나무에서 떨어질때가 있는 법이야")
        game.p("나한테 파이썬 한 수 배워야겠어")
        game.like -=5
    game.img("thony/oo.png")
    game.other("제가 준비한 문제는 여기까지. 모두들 훌륭해요!","CGV직원")
    game.other("이제 영화상영 시작합니다!","CGV직원")
    game.background("movie02.jpg")
    game.img("blank.png")
    game.me("귀멸의 칼날!  ! 드디어 시작이다. 콧김 나와 ")
    game.p("진짜 별로다..")
    game.img("thony/kal.png")
    game.n("'''")
    game.img("thony/kal2.png")
    game.n("'''")
    game.p("저기..")
    game.me("왜? 나 집중 중인데")
    game.img("thony/soshy.png")
    game.p("아까 무서우면 니 손 잡아도 된다고했지?")
    game.me("응 왜?")
    game.p("지금 무서워서")
    game.me("?")
    game.background("hand.jpg")
    game.img("blank.png")
    game.n("......")
    game.n("꿈?")
    game.n("손 평생 안씻는다")




    time.sleep(1)
    game.fade_in()
    game.stage += 1
    game.end()