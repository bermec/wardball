import sdl2.ext

IMAGES = sdl2.ext.Resources(__file__, "images")
PADDLE = IMAGES.get_path("paddle.png")
BALL = IMAGES.get_path("ball.png")