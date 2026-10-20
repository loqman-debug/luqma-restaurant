from PIL import Image

p = Image.open("assets/pizza_plate.png")
alpha = p.split()[-1]
print("Pizza Plate alpha extrema:", alpha.getextrema())
print("Center alpha:", [alpha.getpixel((512+i, 512+i)) for i in range(10)])

b = Image.open("assets/broast_board.png")
alpha_b = b.split()[-1]
print("Broast Board alpha extrema:", alpha_b.getextrema())
print("Center alpha:", [alpha_b.getpixel((512+i, 512+i)) for i in range(10)])
