from __future__ import annotations
import pygame

_mixer_inited = False

def _ensure_mixer():
    global _mixer_inited
    if not _mixer_inited:
        pygame.mixer.init()
        _mixer_inited = True

class Source:
    def __init__(self, path: str):
        _ensure_mixer()
        self.sound = pygame.mixer.Sound(path)

    def play(self, loops: int = 0):
        self.sound.play(loops=loops)

    def stop(self):
        self.sound.stop()

    def set_volume(self, v: float):
        self.sound.set_volume(max(0.0, min(1.0, v)))


class Music:
    def __init__(self):
        _ensure_mixer()

    def load(self, path: str):
        pygame.mixer.music.load(path)

    def play(self, loops: int = -1):
        pygame.mixer.music.play(loops=loops)

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def set_volume(self, v: float):
        pygame.mixer.music.set_volume(max(0.0, min(1.0, v)))

music = Music()

