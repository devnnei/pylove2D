import pylove2d as love
import random

WIDTH, HEIGHT = 800, 480

# Game state
ball = {"x": WIDTH/2, "y": HEIGHT/2, "vx": 220, "vy": 160, "r": 8}
left = {"x": 30, "y": HEIGHT/2 - 40, "w": 14, "h": 80}
right = {"x": WIDTH-44, "y": HEIGHT/2 - 40, "w": 14, "h": 80}
score = {"l": 0, "r": 0}

speed = 320


def load():
    love.window.set_title("PyLove2D Pong")
    love.graphics.set_background_color(0.08, 0.08, 0.1)


def update(dt):
    # paddles
    if love.input.key_down('w'): left['y'] -= speed*dt
    if love.input.key_down('s'): left['y'] += speed*dt
    if love.input.key_down('up'): right['y'] -= speed*dt
    if love.input.key_down('down'): right['y'] += speed*dt

    left['y'] = max(0, min(HEIGHT-left['h'], left['y']))
    right['y'] = max(0, min(HEIGHT-right['h'], right['y']))

    # ball movement
    ball['x'] += ball['vx']*dt
    ball['y'] += ball['vy']*dt

    # top/bottom bounce
    if ball['y']-ball['r'] <= 0 or ball['y']+ball['r'] >= HEIGHT:
        ball['vy'] *= -1

    # paddle collisions
    if left['x'] < ball['x']-ball['r'] < left['x']+left['w'] and left['y'] < ball['y'] < left['y']+left['h']:
        ball['vx'] = abs(ball['vx']) * 1.03
    if right['x'] < ball['x']+ball['r'] < right['x']+right['w'] and right['y'] < ball['y'] < right['y']+right['h']:
        ball['vx'] = -abs(ball['vx']) * 1.03

    # scoring
    if ball['x'] < -10:
        score['r'] += 1
        reset_ball(direction=1)
    elif ball['x'] > WIDTH+10:
        score['l'] += 1
        reset_ball(direction=-1)


def reset_ball(direction=1):
    ball['x'] = WIDTH/2
    ball['y'] = HEIGHT/2
    ball['vx'] = direction * 220
    ball['vy'] = random.choice([-1,1]) * 160


def draw(g):
    g.clear(0.08, 0.08, 0.1)
    # middle line
    g.set_color(0.3, 0.3, 0.35)
    for y in range(0, HEIGHT, 16):
        g.rectangle('fill', WIDTH/2 - 2, y, 4, 10)

    # paddles
    g.set_color(0.9, 0.9, 0.95)
    g.rectangle('fill', left['x'], left['y'], left['w'], left['h'], radius=4)
    g.rectangle('fill', right['x'], right['y'], right['w'], right['h'], radius=4)

    # ball
    g.circle('fill', ball['x'], ball['y'], ball['r'])

    # score
    g.set_color(1, 1, 1)
    g.print(f"{score['l']}  :  {score['r']}", WIDTH/2 - 24, 12, size=32)


def keypressed(k):
    if k == 'escape':
        import sys
        sys.exit(0)


if __name__ == "__main__":
    # Bind callbacks found in this module and run
    love.run(width=WIDTH, height=HEIGHT, title="PyLove2D Pong", fps=60)
