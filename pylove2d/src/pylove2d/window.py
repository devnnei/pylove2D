from __future__ import annotations
import pygame
from typing import Tuple

_screen = None


def _init_window(width: int, height: int, title: str):
    global _screen
    _screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption(title)


def _get_screen():
    return _screen


def set_title(title: str):
    pygame.display.set_caption(title)


def set_fullscreen(enabled: bool = True):
    flags = pygame.FULLSCREEN if enabled else pygame.RESIZABLE
    size = _screen.get_size()
    pygame.display.set_mode(size, flags)


def get_size() -> Tuple[int, int]:
    return _screen.get_size()


def set_icon(path: str):
    surf = pygame.image.load(path)
    pygame.display.set_icon(surf)

