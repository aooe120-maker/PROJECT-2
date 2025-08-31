import time
# 씬 정보
name = "엔딩"
stage = 5 # 작동하는 스테이지
req_like=(-100,'>')
is_couple=False # 커플일때만 발동되는 씬인지

def script(game):
    game.img("blank.png") # 화면에 보일 캐릭터 이미지 변경 (아무것도 없는 이미지파일 : blank.png)
    game.fade_out()
    game.background("room_morning.jpg")
    time.sleep(1)
    game.n("다음날...")
    game.n("...")
    # 집착 엔딩
    if game.like >= 110:
        game.n("띵동-")
        game.me("이 시간에 누구지...")
        game.fade_in()
        game.p("파이야 나야!")
        game.n("현관문 뒤로 외치는 써니의 목소리가 희미하게 들린다")
        game.n("무슨일이래..")
        game.n("그것보다 우리집은 어떻게 알아낸거지..?")
        game.n("알려 준 적 있었나...")
        game.me("써니 맞지..? 조금만 기다려!")
        game.p("빨리 나와야해!")
        game.me("뭐가 저렇게 급한거람...")
        game.fade_out()
        game.background("apt.jpg")
        game.img("thony/Brightly.png")
        game.n("나는 대충 준비를 마치고 문을 열었다")
        game.fade_in()
        game.p("파이!!")
        game.me("써니구나.. 무슨일이래?")
        game.p("보고싶어서 찾아왔지")
        game.n("적극적인건 알았는데 이정도였나..?")
        game.n("살짝 당혹스럽다")
        game.p("있지 나 파이가 너무 좋은거같아!")
        game.p("파이가 너무너무 좋은거같아")
        game.p("... 아니 사랑하는거같아...")
        game.n("나도 어느정도 호감이 있기에 기쁜 말이지만")
        game.n("어딘가 섬뜩하게 들리는 것 같다")
        game.p("파이는 나 어떻게 생각해?")
        game.sel("음...","잘 모르겠어...","갑자기 왜 그래")
        game.img("thony/stay.png")
        game.p("응?")
        game.sel("나도 써니가 좋아!", "나도 써니가 좋아!!","나도 써니가 좋아!!!")
        game.img("thony/Brightly.png")
        game.p("그치? 헤헤헤")
        game.p("그래서 그런데...")
        game.p("우리 영원히 함께하지 않을래?")
        game.sel("그게 무슨...")
        game.img("thony/stay.png")
        game.p("응? 뭐라고?")
        game.sel("영원히 함께하자!","영원히 함께하자!!","영원히 함께하자!!!")
        game.img("thony/Brightly.png")
        game.p("헤헤 파이야 너도 내가 좋구나!")
        game.n("써니의 미소가 섬뜩하게 보인다")
        game.n("뭔가 잘못 되어가는것 같다...")
        game.p("오늘 같이 산책 하지 않을래?")
        game.sel("(도망친다)","(받아들인다)")
        if game.choice == 1:
            game.fade_out()
            game.img("blank.png")
            game.n("나는 있는 힘껏 도망치기 시작했다")
            game.background("runaway.png")
            game.fade_in()
            game.p("파이!!")
            game.p("거기 서!!")
            game.fade_out()
            game.n("나는 앞만 보고 달리기 시작했다")
            game.n("얼마나 달렸을까")
            game.n("뒤를 돌아봐도 쫓아오는 사람은 없었다")
            game.background("street3.jpg")
            game.img("blank.png")
            game.fade_in()
            game.n("하아... 하아...")
            game.n("이제 어쩌지...")
            game.fade_out()
            game.n("밖에서 시간을 좀 보낸 뒤 집으로 귀가한다")
            game.n("집 앞에서 기다릴까 걱정과는 달리")
            game.n("현관문 앞엔 아무도 없었다")
            game.me("학교에선 어쩌지...")
            game.n("휴대폰은 그날 밤 조용했다")
            game.n("... 며칠 뒤")
            game.n("써니는 며칠동안 학교에서 보이지 않았다")
            game.n("최근엔 전학을 간다는 얘기를 들었다")
            game.n("나는 안도의 한숨을 들이킨다")
            time.sleep(1)
            game.n("[ 엔딩 4 ] 이상해진 그녀")
            game.gameover()
    
        elif game.choice == 2:
            game.img("thony/Brightly.png")
            game.me("좋아 산책하자!")
            game.p("헤헤헤.....")
            game.fade_out()
            game.n("나는 그녀와 손을 잡고 거릴 나섰다")
            game.n("이상한 낌새가 있었지만 막상 나오니 평범한.. 어쩌면 연인같은 하루를 보냈다")
            game.n("산책을 잠깐 하고")
            game.n("파이썬 얘기도 했고...")
            game.n("늘 하던 코딩문제 풀기도 하였다")
            game.background("moonlight.jpg")
            game.fade_in()
            game.p("오늘도 즐거웠어")
            game.p("파이야...")
            game.me("응?")
            game.p("우리 오늘부터 사귀는거... 맞지?")
            game.sel("물론이지")
            game.p("헤헤헤...")
            game.p("파이가 너무 좋아")
            game.sel("나도 써니가 좋아")
            game.p("진짜로?")
            game.sel("물론")
            game.p("파이야")
            game.sel("응..?")
            game.p("눈 감아봐")
            game.fade_out()
            game.n("그녀는 내게 입맞춤을 해왔다")
            game.n("당혹스러움보단 이상한 안도감과 안정감이 든다...")
            game.n("[ 엔딩 3 ] 해피엔딩...?")
            game.gameover()

    elif game.like >= 90:
        happy_scene()

    elif game.like >= 60:
        game.n("써니랑 많은 시간을 보낸 것 같다")
        game.n("나는 아마도 써니를 좋아하는 것 같다")
        game.n("이 감정을 전할까..?")
        game.sel("전한다","전하지 않는다")

        # 연인엔딩
        if game.choice == 1:
            park_scene()

        # 친구엔딩
        if game.choice == 2:
            game.n("말로하긴 부끄럽네...")
            friend_scene()
    
    # 친구 엔딩
    elif game.like >= 30:
        game.n("써니랑은 좋은 친구가 된 것 같다")
        game.n("더 다가가곤 싶지만...")
        friend_scene()

    # 싸움 엔딩
    else:
        game.n("써니랑은 다툰 이후로 연락을 하지 않았다")
        game.n("어디서부터 잘못된건지 모르겠다")
        game.n("그냥 잠깐의 설렘이었던 것 같다")
        game.n("[ 엔딩 5 ] 멀어진 그녀")
        game.gameover()

    def friend_scene():
        game.n("몇 주 뒤...")
        game.n("나는 그녀와 둘도 없는 친구가 되었다")
        game.n("조금의 로멘스는 중간중간 있었을지도..?")
        game.n("그래도 이런 알싸한 관계도 괜찮은거 같다")
        game.background("school.png")
        game.img("thony/greet.png")
        game.fade_in()
        game.p("여 잠은 잘 잤는가~~~~")
        game.me("으어 피곤해 죽겠어...")
        game.p("파이썬 공부하느라 피곤한거 맞지?")
        game.me("...")
        game.img("thony/grumpy.png")
        game.p("!!")
        game.me("오늘은 진짜 할게")
        game.p("너 그러고 안할거잖아!!")
        game.me("이번엔 진짜로 할게")
        game.img("thony/disap.png")
        game.p("...")
        game.me("알았어 알았어 오늘도 파이썬 문제는 있지?")
        game.p("이따 쉬는시간에 찾아간다...")
        game.me("그럼 무슨 문제를 내든 맞춰주마")
        game.p("틀리면 벌칙으로 밥사")
        game.sel("...그래","싫은데~")
        if game.choice == 2:
            game.img("밥 사.")
            game.me("... 알겠어;; 맞추면 되잖아")
        game.img("thony/Brightly.png")
        game.p("꽁짜밥이다~")
        game.me("뭐?!?!")
        game.me("진짜 다 맞춰주마")
        game.n("...")
        if game.like >= 60:
            game.n("암만생각해도 써니는 나한테 호감 있는거 같은데..")
            game.n("복잡하게 생각말자...")
        game.n("지금 이런 관계도 좋은 것 같다.")
        game.n("지금의 거리감이 좋은 것 같다")
        game.n("써니도 지금이 제일 맘에 들지도 모르겠다")
        game.fade_out()
        time.sleep(1)
        game.n("[ 엔딩 2 ] 최고의 친구?")
        game.gameover()



























    def park_scene():
        game.p("")
























    def happy_scene():
        game.n("써니랑 많은 시간을 보낸 것 같다")
        game.n("나는 아마도 써니를 좋아하는 것 같다...")
        game.n("어쩌면 내가 먼저 고백을...")
        game.fade_in()
        game.n("써니에게서 전화가 왔다")
        game.me("괜히 긴장되네...")
        game.p("여보세요...? 파이!")
        game.n("어딘가 써니의 목소리에서 떨림이 느껴진다")
        game.me("써니 무슨일이야?")
        game.p("")

        pass















    game.gameover()