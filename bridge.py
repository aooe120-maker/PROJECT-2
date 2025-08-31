from dataclasses import dataclass, field
from threading import Event, Lock

"""
bridge.py

main과 game이 안전하게 통신하게 해줄 수 있는 UIbridge 입니다
State 클래스를 통해 상태를 공유하며 통신합니다
이벤트를 통해 scene의 서브스레드를 제어합니다

"""
# //
@dataclass
class UIState:
    mode: str = "idle" # "idle" , "text" , "choice" , "end"
    speaker: str = "" # 화자의 이름
    text: str = "" # 화자의 출력 텍스트
    options: list[str] = field(default_factory=list) # 선택지들 str 리스트
    bg: str = "" # background 파일
    img: str = "" # img 파일
    fade: str = ""
    is_dialog_visiable: bool = True

class UIBridge:
    def __init__(self):
        self.state = UIState()
        self._lock = Lock() # 스크립트의 진행을 막음
        self._next_ev = Event() # 다음으로 넘어가는 이벤트
        self._choice_ev = Event() # 선택지를 고르는 이벤트
        self._choice_idx = -1 # 기본 선택지 값 (ValueError , TypeError 방어)
        self._fade_ev = Event() # fade에 대한 이벤트

    def clear_text(self):
        self.state.text = ""
    
    def ui_toggle(self): # 다이얼로그 토글 만들었는데 안쓸거임 왜냐면 왜냐면 클릭입력 받는건지 까먹음...
        self.state.is_dialog_visiable is not self.state.is_dialog_visiable
    
    def show_text(self, speaker: str, text: str):
        with self._lock:
            self.state.mode = "text"
            self.state.speaker = speaker
            self.state.text = text
        self._next_ev.clear() # 대기 상태를 초기화
        self._next_ev.wait() # 대기상태를 대기로 전환

    def fade(self,status):
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
        self._next_ev.set() # 입력대기를 진행으로 변경

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