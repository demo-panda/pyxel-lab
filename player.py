import pyxel

FRAME_W = 32
FRAME_H = 32
FRAME_COUNT = 4
ANIM_SPEED = 6
SPEED = 1
COLKEY = 8  # 圖集背景為調色盤索引 8（洋紅 #d4186c）

# 方向索引 -> 圖集列（0:下 1:上 2:左 3:右）
DIR_DOWN = 0
DIR_UP = 1
DIR_LEFT = 2
DIR_RIGHT = 3


class Player:
    """WASD 移動與四方向走路動畫的貓熊角色。"""

    def __init__(self, x=None, y=None):
        if x is None:
            x = (pyxel.width - FRAME_W) // 2
        if y is None:
            y = (pyxel.height - FRAME_H) // 2
        self.x = x
        self.y = y
        self.dir = DIR_DOWN
        self.frame = 0
        self.timer = 0

    def update(self):
        dx = 0
        dy = 0
        if pyxel.btn(pyxel.KEY_A):
            dx -= 1
        if pyxel.btn(pyxel.KEY_D):
            dx += 1
        if pyxel.btn(pyxel.KEY_W):
            dy -= 1
        if pyxel.btn(pyxel.KEY_S):
            dy += 1

        if dx != 0 or dy != 0:
            # 斜向時以水平方向優先，保持朝向穩定
            if dx < 0:
                self.dir = DIR_LEFT
            elif dx > 0:
                self.dir = DIR_RIGHT
            elif dy < 0:
                self.dir = DIR_UP
            else:
                self.dir = DIR_DOWN

            self.x += dx * SPEED
            self.y += dy * SPEED
            self.x = max(0, min(pyxel.width - FRAME_W, self.x))
            self.y = max(0, min(pyxel.height - FRAME_H, self.y))

            self.timer += 1
            if self.timer >= ANIM_SPEED:
                self.timer = 0
                self.frame = (self.frame + 1) % FRAME_COUNT
        else:
            self.frame = 0
            self.timer = 0

    def draw(self):
        u = self.frame * FRAME_W
        v = self.dir * FRAME_H
        pyxel.blt(self.x, self.y, 0, u, v, FRAME_W, FRAME_H, COLKEY)
