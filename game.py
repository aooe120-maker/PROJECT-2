import scene

class Game():
    def __init__(self):
        self.all_scenes = scene.load_scenes(self)
    played_scenes = []
    like = 0
    stage = 0
    is_couple = False
    choice = 0
    current_scene : scene.Scene = None
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
        self.choice = int(input()) #pass
    def end(self):
        # close the scene
        pass
    # 게임 시스템 관련
    def pick_a_scene(self):
        scenes_filtered = [s for s in self.all_scenes if s.req_like[0] <= self.like]
        self.current_scene = scenes_filtered[0]
        self.played_scenes.append(self.current_scene)
        self.current_scene.play()
        pass
    def save_game(self):
        pass
    def load_game(self):
        pass
    def play(self):
        self.pick_a_scene()