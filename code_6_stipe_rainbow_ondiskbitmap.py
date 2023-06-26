import displayio
import board


display = board.DISPLAY

main_group = displayio.Group()

flag_bmp = displayio.OnDiskBitmap("flags/6_stripe_rainbow.bmp")
flag_tg = displayio.TileGrid(bitmap=flag_bmp, pixel_shader=flag_bmp.pixel_shader)

main_group.append(flag_tg)

display.root_group = main_group
while True:
    pass



