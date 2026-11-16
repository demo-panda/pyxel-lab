import pyxel

from player import Player


class App:
    def __init__(self):
        pyxel.init(160, 120, title="Panda Walk")
        pyxel.load("my_resource.pyxres")
        self.player = Player()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()

    def draw(self):
        pyxel.cls(1)
        for gx in range(0, pyxel.width, 16):
            pyxel.line(gx, 0, gx, pyxel.height, 5)
        for gy in range(0, pyxel.height, 16):
            pyxel.line(0, gy, pyxel.width, gy, 5)

        self.player.draw()

        pyxel.text(4, 4, "WASD: MOVE", 7)


App()
