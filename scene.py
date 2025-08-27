from Scenes import testscene

class Scene():
    def __init__(self,name,req_like,script,game,stage=0,is_couple=False):
        self.name = name
        self.req_like = req_like
        self.script = script
        self.game = game
        self.stage = stage
        self.is_couple = is_couple
    def play(self):
        self.script(self.game)
class Game():
    like = 0
    stage = 0
    is_couple = False
    choice = 0
    scenes = []
    current_scene : Scene = None
    # 씬에서 불러와 사용할 함수
    def p(self,script,effect = None ): #effect는 나중에 구현해보도록 하겠습니다. (예: 효과음)
        # 상대방이 하는 말
        print(f"써니: {script}") # 임시로 콘솔출력
        input()
        pass
    def me(self,script):
        # 플레이어가 하는 말
        print(f"나: {script}") # 임시로 콘솔출력
        input()
    def other(self,script,name = "?",effect = None):
        # 다른 캐릭터가 하는말
        print(f"{name}: {script}") # 임시로 콘솔출력
        input()
    def n(self,script):
        # 나레이션이 하는말
        print(f"[ {script} ]")
        input()
    def background(self,file):
        #change background to file
        pass
    def img(self,file):
        #change chracter(thony) img to file
        pass
    def sel(self,*choice):
        for choice in choice:
            print(choice)
        # make button to choose
        self.choice = input() #pass
    def end():
        # close the scene
        pass
    # 게임 시스템 관련
    def pick_scene(self):
        scenes_filtered = [scene for scene in self.scenes if scene.req_like[0] <= self.like]
        self.current_scene = scenes_filtered[self.stage]
        self.current_scene.play()
        pass
    def save_game(self):
        pass
    def load_game(self):
        pass
game = Game()