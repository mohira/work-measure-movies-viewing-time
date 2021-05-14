from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import List

from measure.measure import Sec


@dataclass(frozen=True)
class Video:
    path: Path
    sec: Sec

    def viewing_time(self) -> str:
        return self.sec.to_mmss()


@dataclass(frozen=True)
class Videos:
    values: List[Video] = field(default_factory=list)

    def add(self, video: Video) -> Videos:
        return Videos(self.values + [video])

    def __len__(self) -> int:
        return len(self.values)

    def __getitem__(self, index: int) -> Video:
        return self.values[index]

    def total_sec(self) -> Sec:
        total = Sec(0)
        for video in self.values:
            total += video.sec
        return total
