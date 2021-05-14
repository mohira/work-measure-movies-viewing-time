from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import cv2


@dataclass(frozen=True)
class Sec:
    value: int

    def __add__(self, other: Sec) -> Sec:
        return Sec(self.value + other.value)

    def to_mmss(self) -> str:
        ss = self.value % 60
        mm = (self.value // 60) % 60

        if self.value < 3600:
            return f'{mm:02}:{ss:02}'
        else:
            hh = self.value // 3600
            return f'{hh:02}:{mm:02}:{ss:02}'


def count_sec(p: Path) -> Sec:
    capture = cv2.VideoCapture(str(p))
    frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(capture.get(cv2.CAP_PROP_FPS))

    return Sec(frames // fps)
