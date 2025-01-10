import arcade
from arcade.examples.dual_stick_shooter import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Ping Pong'

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('circle.png', 0.15)
        self.change_x = 5
        self.change_y = 5

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x

        if self.left <= 0:
            self.change_x = -self.change_x

        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y

class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('line.png', 0.3)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 100
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()

    def update(self, delta):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.bar.update()
        if self.ball.bottom <= 0:
            view = Game_over_view()
            self.window.show_view(view)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 7
        if key == arcade.key.LEFT:
            self.bar.change_x = -7

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0

class Game_over_view(arcade.View):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture('game_over.jpg')

    def on_draw(self):
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

if __name__ == '__main__':
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = GameView()
    window.show_view(start_view)
    start_view.setup()
    arcade.run()