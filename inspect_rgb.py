from PIL import Image

p = Image.open("assets/pizza_hero.jpg")
print("Corner (0,0):", p.getpixel((0,0)))
print("Corner (500,0):", p.getpixel((500,0)))
print("Center (512,512):", p.getpixel((512,512)))
