from __future__ import annotations
import importlib
import inspect
import pygame
import sys
from typing import Callable, Optional

from . import graphics, input as love_input, timer, window

_DEF_NAMES = [
    "load", "update", "draw", "keypressed", "keyreleased",
    "mousepressed", "mousereleased", "mousemoved", "wheelmoved",
    "resize",
]

class LoveApp:
    def __init__(self, width: int = 800, height: int = 600, title: str = "PyLove2D", fps: int = 60):
        pygame.init()
        window._init_window(width, height, title)
        graphics._init_graphics()
        love_input._init_input()  # safe now
        timer._init_timer()

        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = fps

        # User callbacks
        self.cb_load: Optional[Callable] = None
        self.cb_update: Optional[Callable[[float], None]] = None
        self.cb_draw: Optional[Callable[[graphics], None]] = None
        self.cb_keypressed: Optional[Callable[[str], None]] = None
        self.cb_keyreleased: Optional[Callable[[str], None]] = None
        self.cb_mousepressed: Optional[Callable[[int, int, int], None]] = None
        self.cb_mousereleased: Optional[Callable[[int, int, int], None]] = None
        self.cb_mousemoved: Optional[Callable[[int, int, int, int], None]] = None
        self.cb_wheelmoved: Optional[Callable[[int, int], None]] = None
        self.cb_resize: Optional[Callable[[int, int], None]] = None

    def set_callbacks(self, module=None, **kwargs):
        if module is not None:
            if isinstance(module, str):
                module = importlib.import_module(module)
            for name in _DEF_NAMES:
                if hasattr(module, name) and callable(getattr(module, name)):
                    setattr(self, f"cb_{name}", getattr(module, name))
        for k, v in kwargs.items():
            if k in _DEF_NAMES:
                setattr(self, f"cb_{k}", v)

    def _dispatch_event(self, ev: pygame.event.Event):
        love_input._pump_event(ev)

        if ev.type == pygame.QUIT:
            self.running = False
        elif ev.type == pygame.KEYDOWN and self.cb_keypressed:
            self.cb_keypressed(love_input.key_name(ev.key))
        elif ev.type == pygame.KEYUP and self.cb_keyreleased:
            self.cb_keyreleased(love_input.key_name(ev.key))
        elif ev.type == pygame.MOUSEBUTTONDOWN and self.cb_mousepressed:
            x, y = ev.pos
            self.cb_mousepressed(x, y, ev.button)
        elif ev.type == pygame.MOUSEBUTTONUP and self.cb_mousereleased:
            x, y = ev.pos
            self.cb_mousereleased(x, y, ev.button)
        elif ev.type == pygame.MOUSEMOTION and self.cb_mousemoved:
            x, y = ev.pos
            relx, rely = ev.rel
            self.cb_mousemoved(x, y, relx, rely)
        elif ev.type == pygame.MOUSEWHEEL and self.cb_wheelmoved:
            self.cb_wheelmoved(ev.x, ev.y)
        elif ev.type == pygame.WINDOWRESIZED and self.cb_resize:
            self.cb_resize(ev.x, ev.y)

    def run(self):
        if self.cb_load:
            self.cb_load()
        while self.running:
            dt = self.clock.tick(self.fps) / 1000.0

            for ev in pygame.event.get():
                self._dispatch_event(ev)

            timer._update(dt)
            if self.cb_update:
                self.cb_update(dt)

            graphics._begin_frame()
            if self.cb_draw:
                self.cb_draw(graphics)
            graphics._end_frame()

        pygame.quit()
        sys.exit(0)


def run(**kwargs):
    app = LoveApp(**kwargs)
    main_mod = sys.modules.get("__main__")
    if main_mod:
        app.set_callbacks(main_mod)
    app.run()
