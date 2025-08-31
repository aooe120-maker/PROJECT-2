import threading
import scene; import os
from bridge import UIBridge
import time
"""
game.py

씬에서 접근 가능한 슈퍼초고수준 API클래스입니다
다양한 로직을 간단한 함수로 변환, 브릿지에 전달하여 main에 적용합니다

"""




class Game():
    def __init__(self, bridge: UIBridge):
        self.bridge = bridge
        self.all_scenes = scene.load_scenes(self)
        self.played_scenes = []

        # 변수들
        self.like = 0 # 호감도
        self.interest = 0 # 흥미도
        self.belive = 0 # 신뢰도
        self.mental = 100 # 멘탈 수치

        self.stage = 0 # 현재 스테이지
        self.is_couple = False # 커플인지
        self.choice = 0 # 반환하는 선택지
        self.current_scene: scene.Scene | None = None
        self._worker: threading.Thread | None = None

    def p(self, script, effect=None):
        self.bridge.show_text("써니", script) # 상대가 하는 말을 다이얼로그로 출력

    def me(self, script):
        self.bridge.show_text("나", script) # 내가 하는 말

    def other(self, script, name="?", effect=None):
        self.bridge.show_text(name, script) # 제 3의 등장인물

    def n(self, script): # 나레이션 , 혼잣말 등 처리
        self.bridge.show_text("", f"[ {script} ]")

    def background(self, file): # 배경이미지 변경 함수
        if file[0:8] == "sprites/":
            self.bridge.set_bg(file)
        else:
            self.bridge.set_bg("sprites/bg/" + file)

    def img(self, file): # 캐릭터 이미지 교체 함수
        if file[0:8] == "sprites/":
            self.bridge.set_img(file)
        else:
            self.bridge.set_img("sprites/" + file)

    def sel(self, *choice): # 선택지를 만든는 함수
        idx = self.bridge.ask_choice(list(choice))
        self.choice = idx + 1
        return self.choice

    def fade_in(self): # 배경 밝게
        self.bridge.start_fade("in")
    def fade_out(self): # 배경 어둡게
        self.bridge.start_fade("out")

    def end(self): # scene에서 종료를 호출하는 함수
        self.next_scene()

    def gameover(self):
        self.fade_out()
        time.sleep(1)
        self.n("플레이 해 주셔서 감사합니다")
        self.n("제작 : 프로젝트 2 팀")
        self.n("클릭하여 메인메뉴로 이동")
        self.bridge.mark_end()

    def _run_scene(self): # main에서 game 불러오는 함수
        self.next_scene()

    def next_scene(self): # 다음 씬을 stage만 검사하여 불러옴
        for scene in self.all_scenes:
            if scene.stage == self.stage:
                self.current_scene = scene
        self.played_scenes.append(self.current_scene)
        self.current_scene.play()
        self.end()
    
    def scene_picker(self): #다양한 분기 구현 못함 ㅜ ㅜ 대본쓸 시간 부족 (요구 호감도와 커플인지 여부 검사합니다!)
        scenes_filtered = []
        for scene in self.all_scenes:
            if scene.stage == scene.stage and scene.is_couple == self.is_couple:
                if (scene.req_like[1] == "<" and scene.req_like[0] < self.like) or (scene.req_like[1] == ">" and scene.req_like[0] >= self.like):
                    scenes_filtered.append(scene)
        self.current_scene = scenes_filtered[0]
        self.played_scenes.append(self.current_scene)
        self.current_scene.play()
        self.end()

    def play(self): # 서브스레드 관련 동작
        if self._worker and self._worker.is_alive():
            return
        self._worker = threading.Thread(target=self._run_scene, daemon=True)
        self._worker.start()