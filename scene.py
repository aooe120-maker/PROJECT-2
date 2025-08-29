import importlib
import pkgutil

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


def load_scenes(game):
	scenes = []
	# scenes 패키지 안의 모든 모듈을 탐색
	package = "scenes"
	for _, module_name, _ in pkgutil.iter_modules([package]):
		module = importlib.import_module(f"{package}.{module_name}")
		# 각 모듈에 필요한 속성이 있다고 가정
		scene = Scene(
			module.name,
			module.req_like,
			module.script,
			game,
			module.stage,
			module.is_couple
		)
		scenes.append(scene)
	return scenes