from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Color:
    r: float
    g: float
    b: float
    a: float = 1.0


    def to255(self):
        return (int(self.r*255), int(self.g*255), int(self.b*255), int(self.a*255))

