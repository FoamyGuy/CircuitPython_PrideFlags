import displayio
import board
import vectorio
from adafruit_display_shapes.rect import Rect

dark_orange = 0xd62900
orange = 0xff9b55
white = 0xffffff
pink = 0xd462a6
dark_pink = 0xa50062

colors = (
    dark_orange,
    orange,
    white,
    pink,
    dark_pink
)

display = board.DISPLAY

main_group = displayio.Group()

for index, color in enumerate(colors):
    palette = displayio.Palette(2)
    palette[1] = color
    stripe_shape = displayio.Shape(display.width, display.height // len(colors))

    stripe_tg = displayio.TileGrid(bitmap=stripe_shape, pixel_shader=palette)
    stripe_tg.y = display.height // len(colors) * index
    main_group.append(stripe_tg)


display.root_group = main_group
while True:
    pass
