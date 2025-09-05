from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, List

_time = 0.0
_tasks: List["_Task"] = []


def _init_timer():
    global _time, _tasks
    _time = 0.0
    _tasks = []


def get_time() -> float:
    return _time


def after(seconds: float, fn: Callable[[], None]):
    _tasks.append(_Task(interval=seconds, repeat=False, fn=fn))


def every(seconds: float, fn: Callable[[], None]):
    _tasks.append(_Task(interval=seconds, repeat=True, fn=fn))


def _update(dt: float):
    global _time
    _time += dt
    to_add = []
    for t in list(_tasks):
        t.elapsed += dt
        if t.elapsed >= t.interval:
            try:
                t.fn()
            finally:
                t.elapsed -= t.interval
                if not t.repeat:
                    _tasks.remove(t)
    _tasks.extend(to_add)


@dataclass
class _Task:
    interval: float
    repeat: bool
    fn: Callable[[], None]
    elapsed: float = 0.0
