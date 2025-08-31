import importlib
import pkgutil

"""
scene.py
아아.. 이것은.. 씬들의 붕어빵 틀 그 이상 그 이하도 아니다...

"""

class Scene:
	def __init__(self, name, req_like, script, game, stage=0, is_couple=False):
		self.name = name
		self.req_like = req_like
		self.script = script
		self.game = game
		self.stage = stage
		self.is_couple = is_couple

	def play(self):
		self.script(self.game)



# 돚거한 코드 (맛있다)
# scenes 폴더안에 모든 scene들을 Scene 클래스 인스턴스로 변환해주는 멋쟁이코드라네~
def load_scenes(game):
	scenes = []
	package = "scenes"
	for _, module_name, _ in pkgutil.iter_modules([package]):
		module = importlib.import_module(f"{package}.{module_name}")
		scene = Scene(
			module.name,
			module.req_like,
			module.script,
			game,
			module.stage,
			module.is_couple
		)
		scenes.append(scene)
		print(scene.name)
	return scenes