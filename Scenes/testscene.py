from scene import *
def scene_test(game:Game):
    game.background("sprites/cover.png")
    game.img("sprites/smile.png") # 캐릭터 이미지 변경 (직접 추가해도 됩니다)
    game.n("")
    game.p("안녕!") # 상대 대사 출력
    game.p("이건 테스트 씬이야!")
    game.sel("반가워","저리가") # 선택지
    if game.choice == 1: #받아온 선택지
        game.like += 10 #호감도 증가
        game.p("나도 반가워!")
        game.me("내 이름은 오즈야") # 내 대사
    elif game.choice == 2:
        game.like -= 10 #호감도 감소
        game.img("sprites/angry.png")
        game.p("저리가라니!")
        game.me("말이 헛나왔구나 미안하다")
    game.stage += 1
    game.end()

game.scenes.append(Scene(
name="테스트",
stage=0, # 작동하는 스테이지
script=scene_test, # 작성한 스크립트
game=game, # 게임 객체
req_like=(0,'='), # (요구 호감도 , '=' : 같을때 '<' : 같거나 높을때 '>' : 같거나 낮을때)
is_couple=False # 커플일때만 발동되는 이벤트인지
))