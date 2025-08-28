import scenes.testscene as testscene
import scenes.opening as opening
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
def load_scenes(game):
    return[
    Scene(testscene.name,testscene.req_like,testscene.script,game,testscene.stage,testscene.is_couple),
    Scene(opening.name,opening.req_like,opening.script,game,opening.stage,opening.is_couple)
    ]