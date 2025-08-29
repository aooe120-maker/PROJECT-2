name = "테스트"
stage = 0 # 작동하는 스테이지
req_like=(200000,'<') # (요구 호감도 , '=' : 같을때 '<' : 같거나 높을때 '>' : 같거나 낮을때)
is_couple=False # 커플일때만 발동되는 씬인지

def script(game):
    game.background("cafe.jpg")
    game.n("카페에 오면 항상.. 생각도 잠시 재촉하는 써니의 말소리가 들린다.")
    game.p("야! 빨리 좀 와 설마 카페에 처음 와보는건 아니겠지?")
    game.n("닥달하면 뭐 얼마나 빠르다고...")
    game.me("아니야 처음은 아닌데...")
    game.p("그럼 자주 오는 편이야? 넌 왜 그렇게 쭈뼛대는거야 마음에 안 들어??")
    game.n("마음에 안든다는건 아닌데... 그냥 카페는 좀...")
    game.p("대답을 좀 해봐")
    game.sel("카페는 쓸데없이 비싸잖아","사람들이 너무 많은걸 안좋아해..","너가 너무 다그치니까 당황스러워서..")
    if game.choice == 1: #받아온 선택지
        game.like -= 10 #호감도 감소
        game.p("뭐야 너도 돈이 없구나")
        game.me("아니 그런게 아니라...")
    elif game.choice == 2:
        game.like += 10 #호감도 증가
        game.p("아.. 그런거구나")
        game.me("응..")
    elif game.choice == 3:
        game.like += 5
        game.p("아.. 미안 내가 너무 그랬나?")
        game.me("응.. 조금 혼나는것 같았어")

    game.stage += 1
    game.end() # 게임오버가 아니라 씬의 종료를 알리는 함수입니다