import displayio
import board

stripe_height = 34

stripe_1 = 0x018e71
stripe_2 = 0x21cfac
stripe_3 = 0x9ae9c3
stripe_4 = 0xffffff
stripe_5 = 0x7cafe4
stripe_6 = 0x4f47cc
stripe_7 = 0x3c1379

palette = displayio.Palette(7)

palette[0] = stripe_1
palette[1] = stripe_2
palette[2] = stripe_3
palette[3] = stripe_4
palette[4] = stripe_5
palette[5] = stripe_6
palette[6] = stripe_7

display = board.DISPLAY

main_group = displayio.Group()

flag_sliver_bmp = displayio.Bitmap(1, 238, 7)

for stripe_index in range(7):
    starting = stripe_index * stripe_height
    for pixel_y in range(starting, starting + stripe_height):
        flag_sliver_bmp[0, pixel_y] = stripe_index

flag_tg = displayio.TileGrid(bitmap=flag_sliver_bmp, pixel_shader=palette,
                             width=320)

main_group.append(flag_tg)

display.root_group = main_group
while True:
    pass
