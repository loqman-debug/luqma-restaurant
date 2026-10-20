from PIL import Image

p = Image.open("assets/pizza_hero.jpg")
b = Image.open("assets/broast_hero.jpg")
print("Pizza:", p.size, p.mode)
print("Broast:", b.size, b.mode)
