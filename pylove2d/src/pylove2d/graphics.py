from __future__ import annotations
import pygame
from typing import Optional, Tuple
from .types import Color
from . import window

# Internal state
_screen: Optional[pygame.Surface] = None
_cur_color: Color = Color(1,1,1,1)
_bg_color: Optional[Color] = None

# Fonts cache
_font_cache = {}


def _init_graphics():
    global _screen
    _screen = window._get_screen()


def _begin_frame():
    if _bg_color is not None:
        clear(_bg_color.r, _bg_color.g, _bg_color.b, _bg_color.a)


def _end_frame():
    pygame.display.flip()


def set_color(r: float, g: float, b: float, a: float = 1.0):
    global _cur_color
    _cur_color = Color(r,g,b,a)


def set_background_color(r: float, g: float, b: float, a: float = 1.0):
    global _bg_color
    _bg_color = Color(r,g,b,a)


def clear(r: float, g: float, b: float, a: float = 1.0):
    _screen.fill((int(r*255), int(g*255), int(b*255)))


def _color_tuple(alpha_override: Optional[float] = None):
    a = _cur_color.a if alpha_override is None else alpha_override
    return (int(_cur_color.r*255), int(_cur_color.g*255), int(_cur_color.b*255), int(a*255))


def rectangle(mode: str, x: float, y: float, w: float, h: float, radius: int = 0, width: int = 1):
    rect = pygame.Rect(x, y, w, h)
    if mode == 'fill':
        if radius > 0:
            pygame.draw.rect(_screen, _color_tuple(), rect, border_radius=radius)
        else:
            pygame.draw.rect(_screen, _color_tuple(), rect)
    else:
        pygame.draw.rect(_screen, _color_tuple(), rect, width=width, border_radius=radius)


def circle(mode: str, x: float, y: float, radius: float, width: int = 1):
    if mode == 'fill':
        pygame.draw.circle(_screen, _color_tuple(), (int(x), int(y)), int(radius))
    else:
        pygame.draw.circle(_screen, _color_tuple(), (int(x), int(y)), int(radius), width)


def line(x1: float, y1: float, x2: float, y2: float, width: int = 1):
    pygame.draw.line(_screen, _color_tuple(), (x1, y1), (x2, y2), width)


def polygon(mode: str, points: list[Tuple[float, float]], width: int = 1):
    if mode == 'fill':
        pygame.draw.polygon(_screen, _color_tuple(), points)
    else:
        pygame.draw.polygon(_screen, _color_tuple(), points, width)


def points(points: list[Tuple[float, float]], radius: int = 2):
    for (x,y) in points:
        pygame.draw.circle(_screen, _color_tuple(), (int(x), int(y)), radius)


class Image:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface.convert_alpha()
        self.w = self.surface.get_width()
        self.h = self.surface.get_height()

    @classmethod
    def load(cls, path: str) -> 'Image':
        surf = pygame.image.load(path)
        return cls(surf)


def draw(img: Image, x: float, y: float, angle_deg: float = 0.0, sx: float = 1.0, sy: Optional[float] = None, origin: Tuple[float, float] = (0,0)):
    if sy is None:
        sy = sx
    surf = pygame.transform.rotozoom(img.surface, -angle_deg, sx)  # uniform scale via sx only
    # If non-uniform scaling desired, add separate scale; here keep simple
    rect = surf.get_rect()
    ox, oy = origin
    rect.topleft = (x - ox, y - oy)
    _screen.blit(surf, rect)


def _get_font(size: int, name: Optional[str] = None):
    key = (name or "default", size)
    f = _font_cache.get(key)
    if f is None:
        f = pygame.font.Font(name, size)
        _font_cache[key] = f
    return f


def print(text: str, x: float, y: float, size: int = 24, name: Optional[str] = None):
    font = _get_font(size, name)
    surf = font.render(text, True, _color_tuple(alpha_override=1.0))
    _screen.blit(surf, (x, y))
