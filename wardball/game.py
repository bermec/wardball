import sdl2.ext
from .paths import PADDLE


class Game:
    window = sdl2.ext.Window("WardBall", size=(640, 480))

    def init_game(self):
        sdl2.ext.init()
        self.window.show()

    def render_paddle(self):
        factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
        sprite = factory.from_image(PADDLE)

        sprite_renderer = factory.create_sprite_render_system(self.window)
        sprite_renderer.render(sprite)

    def event_loop(self):
        processor = sdl2.ext.TestEventProcessor()
        processor.run(self.window)


def launch_game():
    game = Game()
    game.init_game()




