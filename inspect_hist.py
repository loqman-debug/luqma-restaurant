from PIL import Image

im = Image.open("assets/pizza_hero.jpg").convert("RGBA")
p_alpha = Image.open("assets/pizza_plate.png").split()[-1]
print("Pixel (512, 512) alpha:", p_alpha.getpixel((512, 512)))

# let us see where alpha is 255
import collections
hist = p_alpha.histogram()
print("Alpha histogram count 0:", hist[0], "count 255:", hist[255])
