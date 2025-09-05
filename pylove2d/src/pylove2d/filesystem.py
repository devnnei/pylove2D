from __future__ import annotations
from pathlib import Path

class _FS:
    def read(self, path: str, mode: str = 'rb'):
        return Path(path).read_bytes() if 'b' in mode else Path(path).read_text()

    def write(self, path: str, data, mode: str = 'wb'):
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        if 'b' in mode:
            p.write_bytes(data)
        else:
            p.write_text(data)

    def exists(self, path: str) -> bool:
        return Path(path).exists()

    def mkdir(self, path: str):
        Path(path).mkdir(parents=True, exist_ok=True)

fs = _FS()
