from PIL import Image, ImageDraw, ImageFont

im_open = Image.open("assets/box_open.png").convert("RGBA")
print("box_open size:", im_open.size)

im_closed = Image.open("assets/box_closed.png").convert("RGBA")
print("box_closed size:", im_closed.size)
