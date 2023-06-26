import displayio
import board
import bitmaptools


red = 0xe50000
orange = 0xff8d00
yellow = 0xffee00
green = 0x008121
dark_blue = 0x004cff
purple = 0x760188

pink = 0xffb1c9
light_blue = 0x75d8ef
brown = 0x61360d
black = 0x000000
white = 0xffffff

palette = displayio.Palette(11)

palette[0] = red
palette[1] = orange
palette[2] = yellow
palette[3] = green
palette[4] = dark_blue
palette[5] = purple
palette[6] = pink
palette[7] = light_blue
palette[8] = brown
palette[9] = black
palette[10] = white


display = board.DISPLAY

main_group = displayio.Group()


flag_bmp = displayio.Bitmap(320, 240, 11)
flag_tg = displayio.TileGrid(bitmap=flag_bmp, pixel_shader=palette)

stripe_height = display.height//6

bitmaptools.fill_region(flag_bmp, 0, 0, display.width, display.height//6, 0)
bitmaptools.fill_region(flag_bmp, 0, stripe_height, display.width, stripe_height*2, 1)
bitmaptools.fill_region(flag_bmp, 0, stripe_height*2, display.width, stripe_height*3, 2)
bitmaptools.fill_region(flag_bmp, 0, stripe_height*3, display.width, stripe_height*4, 3)
bitmaptools.fill_region(flag_bmp, 0, stripe_height*4, display.width, stripe_height*5, 4)
bitmaptools.fill_region(flag_bmp, 0, stripe_height*5, display.width, stripe_height*6, 5)



main_group.append(flag_tg)


display.root_group = main_group
while True:
    pass
