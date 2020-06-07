from enum import Enum
from GUI.control import Control


class ControlAction(Enum):
    START = 1
    PAUSE = 2
    FFSTART = 3
    FFSTOP = 4
    NONE = 5


class ControlBar:
    controls = []

    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.ff = False
        start = Control((self.x, self.y), (100, 25), "Spawn", ControlAction.START)
        self.controls.append(start)

    def draw(self, screen):
        for control in self.controls:
            control.draw(screen)

    def getAction(self, pos):
        for control in self.controls:
            if control.inControl(pos):
                return control.control
        return ControlAction.NONE
