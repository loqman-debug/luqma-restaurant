from PIL import Image, ImageDraw, ImageFilter

def proper_white_removal(src_name, dst_name):
    im = Image.open(f"assets/{src_name}").convert("RGBA")
    w, h = im.size
    
    # Create binary mask: 255 if white background, 0 if object
    mask = Image.new("L", (w, h), 0)
    for x in range(w):
        for y in range(h):
            r, g, b, _ = im.getpixel((x, y))
            # Background is clean white
            if r > 236 and g > 236 and b > 236:
                mask.putpixel((x, y), 255)
    
    # Floodfill ONLY connected white from borders with 128
    for pt in [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1), 
               (w//2, 0), (w//2, h-1), (0, h//2), (w-1, h//2)]:
        if mask.getpixel(pt) == 255:
            ImageDraw.floodfill(mask, pt, 128)
            
    # Now: 128 is connected outside background -> alpha = 0
    # Everything else (including any light toppings inside the pizza/broast) -> alpha = 255
    alpha = Image.new("L", (w, h), 255)
    for x in range(w):
        for y in range(h):
            if mask.getpixel((x, y)) == 128:
                alpha.putpixel((x, y), 0)
                
    feathered = alpha.filter(ImageFilter.GaussianBlur(1.0))
    im.putalpha(feathered)
    im.save(f"assets/{dst_name}", "PNG")
    
    hist = feathered.histogram()
    print(f"Done {dst_name}: Alpha 0 count={hist[0]}, Alpha 255 count={hist[255]}, Center={feathered.getpixel((w//2, h//2))}")

proper_white_removal("pizza_hero.jpg", "pizza_plate.png")
proper_white_removal("broast_hero.jpg", "broast_board.png")
