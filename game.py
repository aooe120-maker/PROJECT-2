import threading
import scene; import os
from bridge import UIBridge

class Game():
    def __init__(self, bridge: UIBridge):
        self.bridge = bridge
        self.all_scenes = scene.load_scenes(self)
        self.played_scenes = []

        # 변수들
        self.like = 0 # 호감도
        self.interest = 0 # 흥미도
        self.belive = 0 # 신뢰도

        self.stage = 0 # 현재 스테이지
        self.is_couple = False # 커플인지
        self.choice = 0
        self.current_scene: scene.Scene | None = None
        self._worker: threading.Thread | None = None

    def p(self, script, effect=None):
        self.bridge.show_text("써니", script)

    def me(self, script):
        self.bridge.show_text("나", script)

    def other(self, script, name="?", effect=None):
        self.bridge.show_text(name, script)

    def n(self, script):
        self.bridge.show_text("", f"[ {script} ]")

    def background(self, file):
        if file[0:8] == "sprites/":
            self.bridge.set_bg(file)
        else:
            self.bridge.set_bg("sprites/bg/" + file)

    def img(self, file):
        if file[0:8] == "sprites/":
            self.bridge.set_img(file)
        else:
            self.bridge.set_img("sprites/" + file)

    def sel(self, *choice):
        idx = self.bridge.ask_choice(list(choice))
        self.choice = idx + 1
        return self.choice

    def fade_in(self):
        self.bridge.start_fade("in")
    def fade_out(self):
        self.bridge.start_fade("out")

    def end(self):
        self.bridge.mark_end()

    def _run_scene(self):
        self.pick_a_scene()

    def pick_a_scene(self):
        scenes_filtered = []
        for scene in self.all_scenes:
            if scene.stage == scene.stage and scene.is_couple == self.is_couple:
                if (scene.req_like[1] == "<" and scene.req_like[0] < self.like) or (scene.req_like[1] == ">" and scene.req_like[0] >= self.like):
                    scenes_filtered.append(scene)
        self.current_scene = scenes_filtered[0]
        self.played_scenes.append(self.current_scene)
        self.current_scene.play()
        self.end()

    def play(self):
        if self._worker and self._worker.is_alive():
            return
        self._worker = threading.Thread(target=self._run_scene, daemon=True)
        self._worker.start()