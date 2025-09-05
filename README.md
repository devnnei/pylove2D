![pylove2D](Pylove2Dreadmelogo.png)
[![PyPI version](https://img.shields.io/pypi/v/pylove2d)](https://pypi.org/project/pylove2d/)
[![Python Version](https://img.shields.io/pypi/pyversions/pylove2d)](https://www.python.org/)

PyLove2D is a Python game framework inspired by [LÖVE2D](https://love2d.org/). It allows you to quickly build **2D games** using Python and Pygame, with a simple API for graphics, input, audio, and more.

---

## Features

- **Graphics:** Draw shapes, images, and text easily.  
- **Audio:** Play sound effects and music.  
- **Input:** Keyboard, mouse, and joystick support.  
- **Timer:** Schedule delayed or repeated actions.  
- **Math utilities:** Vectors and transformations.  
- **Filesystem helpers:** Load/save data easily.

---

## Installation

PyLove2D requires **Python 3.10+** and Pygame. Install via pip:

```bash
pip install pygame-ce pylove2d
```
## Getting Started

To install PyLove2D run this command in your terminal:

```bash
pip install pylove2d
```

**Basic Game Example** :

Create a file main.py:

```python
import pylove2d as love

def load():
    love.window.set_title("Hello PyLove2D!")

def update(dt):
    pass

def draw(g):
    g.clear(0.1, 0.1, 0.2)
    g.set_color(1, 1, 1)
    g.print("Hello, World!", 200, 200)

if __name__ == "__main__":
    love.run(width=800, height=480)
```

Run your game:

```bash
python main.py
```

You should see a window with “Hello, World!” on a dark background.

## API Overview

### Graphics

```python
love.graphics.set_color(1, 0, 0)
love.graphics.rectangle("fill", 100, 100, 50, 50)
```

### Input

```python
if love.input.key_down("left"):
    print("Moving left")
```

### Audio

```python
sound = love.audio.Source("sound.wav")
sound.play()
```

### Timer

```python
love.timer.after(2, lambda: print("2s passed"))
love.timer.every(1, lambda: print("Every 1s"))
```

## Examples

### Pong :

```python
import pylove2d as love

p1 = {'y': 200}
p2 = {'y': 200}

def load():
    love.window.set_title("Pong")

def update(dt):
    if love.input.key_down("w"): p1['y'] -= 200 * dt
    if love.input.key_down("s"): p1['y'] += 200 * dt

def draw(g):
    g.clear(0, 0, 0)
    g.set_color(1, 1, 1)
    g.rectangle("fill", 50, p1['y'], 20, 100)
```

### Platformer

```python
import pylove2d as love

player = {'x':100,'y':300,'vx':0,'vy':0,'w':40,'h':60,'on_ground':False}

def update(dt):
    if love.input.key_down("left"): player['vx'] = -200
    elif love.input.key_down("right"): player['vx'] = 200
    else: player['vx'] = 0
    player['vy'] += 800 * dt
    player['x'] += player['vx'] * dt
    player['y'] += player['vy'] * dt

def draw(g):
    g.clear(0.1,0.1,0.2)
    g.set_color(0.8,0.3,0.3)
    g.rectangle("fill", player['x'], player['y'], player['w'], player['h'])
```

Project Structure

``
pylove2d/
├── pylove2d/
│   ├── __init__.py
│   ├── app.py
│   ├── graphics.py
│   ├── input.py
│   └── ...
├── examples/
├── tests/
├── README.md
├── LICENSE
├── pyproject.toml
└── setup.py
``

# Contributing :

Contributions are welcome! Please:

    Fork the repository

    Create a feature branch: git checkout -b feature/myfeature

    Commit your changes: git commit -m "Add my feature"

    Push to branch: git push origin feature/myfeature

    Open a Pull Request

# License

MIT License © 2025 nnei

## **Tips :**

    Always run in a virtual environment.

    Use pip install --upgrade pylove2d to update to the latest version.

    Check the examples/ folder for ready-to-run demos.

See `examples/pong/main.py` for a full example.
