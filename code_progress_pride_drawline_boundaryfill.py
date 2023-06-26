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


# xs = bytes([0  , 40, 40, 0 ])
# ys = bytes([0  , 0,  40, 40])
#
# bitmaptools.draw_polygon(flag_bmp, xs, ys, 9, close=True)

bitmaptools.draw_line(flag_bmp, 51, 0, 152, 120, 9)
bitmaptools.draw_line(flag_bmp, 152, 120, 51, 240, 9)

bitmaptools.boundary_fill(flag_bmp, 1, 1, 9)
bitmaptools.boundary_fill(flag_bmp, 1, 45, 9)
bitmaptools.boundary_fill(flag_bmp, 1, 85, 9)
bitmaptools.boundary_fill(flag_bmp, 1, 125, 9)
bitmaptools.boundary_fill(flag_bmp, 1, 165, 9)
bitmaptools.boundary_fill(flag_bmp, 1, 205, 9)

bitmaptools.draw_line(flag_bmp, 26, 0, 127, 120, 8)
bitmaptools.draw_line(flag_bmp, 127, 120, 26, 240, 8)

bitmaptools.boundary_fill(flag_bmp, 18, 5, 8)


bitmaptools.draw_line(flag_bmp, 0, 0, 101, 120, 7)
bitmaptools.draw_line(flag_bmp, 101, 120, 0, 240, 7)

bitmaptools.boundary_fill(flag_bmp, 6, 20, 7)


bitmaptools.draw_line(flag_bmp, 0, 31, 75, 120, 6)
bitmaptools.draw_line(flag_bmp, 75, 120, 0, 240-31, 6)

bitmaptools.boundary_fill(flag_bmp, 6, 48, 6)


bitmaptools.draw_line(flag_bmp, 0, 61, 50, 120, 10)
bitmaptools.draw_line(flag_bmp, 50, 120, 0, 240-61, 10)

bitmaptools.boundary_fill(flag_bmp, 24, 95, 10)

main_group.append(flag_tg)


display.root_group = main_group
while True:
    pass
