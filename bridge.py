from dataclasses import dataclass, field
from threading import Event, Lock

@dataclass
class UIState:
    mode: str = "idle" # "idle" , "text" , "choice" , "end"
    speaker: str = ""
    text: str = ""
    options: list[str] = field(default_factory=list)
    bg: str = ""
    img: str = ""
    fade: bool = False

class UIBridge:
    def __init__(self):
        self.state = UIState()
        self._lock = Lock()
        self._next_ev = Event()
        self._choice_ev = Event()
        self._choice_idx = -1
        self._fade_ev = Event()

    def show_text(self, speaker: str, text: str):
        with self._lock:
            self.state.mode = "text"
            self.state.speaker = speaker
            self.state.text = text
        self._next_ev.clear()
        self._next_ev.wait()

    def fade(self,status=True):
        with self._lock:
            self.state.fade = status
        self._next_ev.clear()
        self._next_ev.wait()
        pass

    def ask_choice(self, options: list[str]) -> int:
        with self._lock:
            self.state.mode = "choice"
            self.state.options = options[:]
        self._choice_ev.clear()
        self._choice_ev.wait()
        return self._choice_idx

    def ui_next(self):
        self._next_ev.set()

    def ui_choose(self, idx: int):
        self._choice_idx = idx
        self._choice_ev.set()

    def mark_end(self):
        with self._lock:
            self.state.mode = "end"

    def set_bg(self, path: str):
        with self._lock:
            self.state.bg = path

    def set_img(self, path: str):
        with self._lock:
            self.state.img = path

    def get_state(self) -> UIState:
        with self._lock:
            return UIState(**self.state.__dict__)
    
    def start_fade(self, direction: str):
        with self._lock:
            self.state.fade = direction
        self._fade_ev.clear()
        self._fade_ev.wait()

    def ui_fade_done(self):
        with self._lock:
            self.state.fade = ""
        self._fade_ev.set()