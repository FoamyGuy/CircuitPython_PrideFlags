import displayio
import board

stripe_height = 80

pink = 0xff1b8d
yellow = 0xffd900
blue = 0x1bb3ff

palette = displayio.Palette(7)

palette[0] = pink
palette[1] = yellow
palette[2] = blue

display = board.DISPLAY

main_group = displayio.Group()

flag_sliver_bmp = displayio.Bitmap(1, 240, 3)

for stripe_index in range(3):
    starting = stripe_index * stripe_height
    for pixel_y in range(starting, starting + stripe_height):
        flag_sliver_bmp[0, pixel_y] = stripe_index

flag_tg = displayio.TileGrid(bitmap=flag_sliver_bmp, pixel_shader=palette,
                             height=3, width=320,
                             tile_height=80)

for tile_x in range(320):
    flag_tg[tile_x, 0] = 0
    flag_tg[tile_x, 1] = 1
    flag_tg[tile_x, 2] = 2

main_group.append(flag_tg)

display.root_group = main_group
while True:
    pass
