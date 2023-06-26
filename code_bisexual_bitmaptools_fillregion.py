import displayio
import board
import bitmaptools


pink = 0xd70071
blue = 0x0035aa
purple = 0x9c4e97

palette = displayio.Palette(3)

palette[0] = pink
palette[1] = purple
palette[2] = blue

display = board.DISPLAY

main_group = displayio.Group()


flag_bmp = displayio.Bitmap(320, 240, 3)
flag_tg = displayio.TileGrid(bitmap=flag_bmp, pixel_shader=palette)

bitmaptools.fill_region(flag_bmp, 0, 0, 320, 96, 0)
bitmaptools.fill_region(flag_bmp, 0, 96, 320, 144, 1)
bitmaptools.fill_region(flag_bmp, 0, 144, 320, 240, 2)


main_group.append(flag_tg)


display.root_group = main_group
while True:
    pass
