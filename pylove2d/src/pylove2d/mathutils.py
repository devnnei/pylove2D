from __future__ import annotations
import math
from dataclasses import dataclass

@dataclass
class Vec2:
    x: float = 0.0
    y: float = 0.0

    def __add__(self, o): return Vec2(self.x+o.x, self.y+o.y)
    def __sub__(self, o): return Vec2(self.x-o.x, self.y-o.y)
    def __mul__(self, s: float): return Vec2(self.x*s, self.y*s)
    __rmul__ = __mul__
    def length(self): return math.hypot(self.x, self.y)
    def normalized(self):
        l = self.length()
        return Vec2(self.x/l, self.y/l) if l else Vec2()


def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def lerp(a, b, t):
    return a + (b - a) * t
