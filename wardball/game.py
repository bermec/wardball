import sdl2.ext
from .paths import IMAGES


def launch_game():
    sdl2.ext.init()

    window = sdl2.ext.Window("Hello World!", size=(640, 480))
    window.show()

    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    sprite = factory.from_image(IMAGES.get_path("paddle.png"))

    sprite_renderer = factory.create_sprite_render_system(window)
    sprite_renderer.render(sprite)

    processor = sdl2.ext.TestEventProcessor()
    processor.run(window)
