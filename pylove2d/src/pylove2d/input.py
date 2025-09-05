from __future__ import annotations
import pygame
from typing import Tuple

_held_keys = ()
_mouse_buttons = (False, False, False)
_mouse_pos = (0, 0)

_keymap = {
    pygame.K_LEFT: 'left', pygame.K_RIGHT: 'right', pygame.K_UP: 'up', pygame.K_DOWN: 'down',
    pygame.K_SPACE: 'space', pygame.K_RETURN: 'return', pygame.K_ESCAPE: 'escape',
}
_reverse_map = {v: k for k, v in _keymap.items()}

def _init_input():
    global _held_keys
    # Only call get_pressed after pygame.init() and display set
    _held_keys = pygame.key.get_pressed()

def _pump_event(ev: pygame.event.Event):
    global _held_keys, _mouse_buttons, _mouse_pos
    if ev.type in (pygame.KEYDOWN, pygame.KEYUP):
        _held_keys = pygame.key.get_pressed()
    elif ev.type == pygame.MOUSEMOTION:
        _mouse_pos = ev.pos
    elif ev.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
        _mouse_buttons = pygame.mouse.get_pressed()

def key_down(name_or_key) -> bool:
    if isinstance(name_or_key, str):
        key = _reverse_map.get(name_or_key)
        if key is None:
            try:
                key = getattr(pygame, f"K_{name_or_key}")
            except AttributeError:
                return False
    else:
        key = name_or_key
    return bool(_held_keys[key]) if _held_keys else False

def mouse_position() -> Tuple[int, int]:
    return pygame.mouse.get_pos()

def mouse_down(button: int = 1) -> bool:
    pressed = pygame.mouse.get_pressed()
    idx = max(0, min(2, button-1))
    return bool(pressed[idx])

def key_name(k: int) -> str:
    return _keymap.get(k, pygame.key.name(k))
