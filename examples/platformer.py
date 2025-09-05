# =============================
# File: examples/platformer/main.py
# =============================
import pylove2d as love

WIDTH, HEIGHT = 800, 480

# Player state
player = {"x": 100, "y": 300, "w": 40, "h": 60, "vx": 0, "vy": 0, "on_ground": False}
GRAVITY = 800
SPEED = 250
JUMP = 450

# Platforms: list of (x, y, w, h)
platforms = [
    (0, HEIGHT-40, WIDTH, 40),
    (150, 360, 120, 20),
    (350, 280, 120, 20),
    (600, 200, 150, 20),
]

def load():
    love.window.set_title("PyLove2D Platformer")
    love.graphics.set_background_color(0.1, 0.15, 0.2)


def update(dt):
    # Horizontal movement
    player['vx'] = 0
    if love.input.key_down('left'): player['vx'] = -SPEED
    if love.input.key_down('right'): player['vx'] = SPEED

    # Apply gravity
    player['vy'] += GRAVITY * dt

    # Jump
    if love.input.key_down('space') and player['on_ground']:
        player['vy'] = -JUMP
        player['on_ground'] = False

    # Update position
    player['x'] += player['vx'] * dt
    player['y'] += player['vy'] * dt

    # Simple collision with platforms
    player['on_ground'] = False
    for plat in platforms:
        px, py, pw, ph = plat
        if (player['x'] + player['w'] > px and player['x'] < px + pw and
            player['y'] + player['h'] > py and player['y'] + player['h'] < py + ph + 20 and player['vy'] >=0):
            player['y'] = py - player['h']
            player['vy'] = 0
            player['on_ground'] = True


def draw(g):
    g.clear(0.1, 0.15, 0.2)
    # Draw player
    g.set_color(0.9, 0.4, 0.2)
    g.rectangle('fill', player['x'], player['y'], player['w'], player['h'], radius=6)

    # Draw platforms
    g.set_color(0.3, 0.7, 0.4)
    for plat in platforms:
        px, py, pw, ph = plat
        g.rectangle('fill', px, py, pw, ph, radius=4)

if __name__ == "__main__":
    love.run(width=WIDTH, height=HEIGHT, title="Platformer", fps=60)
