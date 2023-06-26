import displayio
import board
import vectorio
from adafruit_display_shapes.rect import Rect

yellow = 0xfff42f
purple = 0x9c59d1
white = 0xffffff
black = 0x292929
#
# palette = displayio.Palette(3)


display = board.DISPLAY

main_group = displayio.Group()

top_stripe = Rect(fill=yellow, width=display.width, height=display.height // 4,
                                x=0, y=0)

top_middle_stripe = Rect(fill=white, width=display.width, height=display.height // 4,
                                x=0, y=display.height // 4)


bottom_middle_stripe = Rect(fill=purple, width=display.width, height=display.height // 4,
                                x=0, y=(display.height // 4) * 2)

bottom_stripe = Rect(fill=black, width=display.width, height=display.height // 4,
                                x=0, y=(display.height // 4) * 3)

main_group.append(top_stripe)
main_group.append(top_middle_stripe)

main_group.append(bottom_middle_stripe)
main_group.append(bottom_stripe)

display.root_group = main_group
while True:
    pass
