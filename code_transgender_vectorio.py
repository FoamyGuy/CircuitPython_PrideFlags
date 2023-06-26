import displayio
import board
import vectorio

pink = 0xf5abb9
blue = 0x5bcffa
white = 0xffffff

palette = displayio.Palette(3)

palette[0] = pink
palette[1] = blue
palette[2] = white

display = board.DISPLAY

main_group = displayio.Group()

top_stripe = vectorio.Rectangle(pixel_shader=palette, width=display.width, height=display.height // 5,
                                x=0, y=0,
                                color_index=1)

top_middle_stripe = vectorio.Rectangle(pixel_shader=palette, width=display.width, height=display.height // 5,
                                       x=0, y=display.height // 5,
                                       color_index=0)

middle_stripe = vectorio.Rectangle(pixel_shader=palette, width=display.width, height=display.height // 5,
                                       x=0, y=(display.height // 5)*2,
                                       color_index=2)

bottom_middle_stripe = vectorio.Rectangle(pixel_shader=palette, width=display.width, height=display.height // 5,
                                       x=0, y=(display.height // 5)*3,
                                       color_index=0)

bottom_stripe = vectorio.Rectangle(pixel_shader=palette, width=display.width, height=display.height // 5,
                                       x=0, y=(display.height // 5)*4,
                                       color_index=1)

main_group.append(top_stripe)
main_group.append(top_middle_stripe)
main_group.append(middle_stripe)
main_group.append(bottom_middle_stripe)
main_group.append(bottom_stripe)

display.root_group = main_group
while True:
    pass
