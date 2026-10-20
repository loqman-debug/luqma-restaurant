from PIL import Image, ImageDraw, ImageFilter

def make_transparent_from_white(src_name, dst_name):
    im = Image.open(f"assets/{src_name}").convert("RGBA")
    w, h = im.size
    gray = im.convert("L")
    
    # White background threshold: candidate background > 240
    thresh = gray.point(lambda p: 255 if p > 242 else 0, mode="L")
    
    # Floodfill background connected to borders with 128
    bg_canvas = thresh.copy()
    for pt in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), 
               (w // 2, 0), (w // 2, h - 1), (0, h // 2), (w - 1, h // 2)]:
        ImageDraw.floodfill(bg_canvas, pt, 128, thresh=8)
    
    # Where value is 128 (connected outside white) -> alpha = 0, else 255
    raw_alpha = bg_canvas.point(lambda p: 0 if p == 128 else 255, mode="L")
    feathered = raw_alpha.filter(ImageFilter.GaussianBlur(1.2))
    
    im.putalpha(feathered)
    im.save(f"assets/{dst_name}", "PNG", optimize=True)
    print(f"Created: assets/{dst_name}")

if __name__ == "__main__":
    make_transparent_from_white("pizza_hero.jpg", "pizza_plate.png")
    make_transparent_from_white("broast_hero.jpg", "broast_board.png")
    make_transparent_from_white("burger_hero.jpg", "burger_plate.png")
