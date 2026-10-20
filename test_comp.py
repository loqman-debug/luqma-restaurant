from PIL import Image

im = Image.open("assets/bun_top.png")
bg = Image.new("RGBA", im.size, (255, 248, 238, 255))
comp = Image.alpha_composite(bg, im)
comp.convert("RGB").save("assets/test_comp_cream.jpg")
print("Saved assets/test_comp_cream.jpg")
