import os
from PIL import Image, ImageDraw, ImageFilter

def make_transparent(name):
    src_path = os.path.join("assets", f"{name}.jpg")
    dst_path = os.path.join("assets", f"{name}.png")
    
    if not os.path.exists(src_path):
        print(f"File not found: {src_path}")
        return

    im = Image.open(src_path).convert("RGBA")
    w, h = im.size
    gray = im.convert("L")
    
    # Background in our generated images is pure black (< 18)
    # Binary: 0 if candidate background, 255 if foreground
    thresh = gray.point(lambda p: 255 if p > 16 else 0, mode="L")
    
    # Invert so background candidate is 255, foreground is 0
    inv = thresh.point(lambda p: 0 if p == 255 else 255)
    
    # Floodfill background connected to borders with 128
    bg_canvas = inv.copy()
    for pt in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), 
               (w // 2, 0), (w // 2, h - 1), (0, h // 2), (w - 1, h // 2)]:
        ImageDraw.floodfill(bg_canvas, pt, 128, thresh=5)
    
    # Create mask: where value is 128 (connected outside background) -> alpha = 0, else 255
    raw_alpha = bg_canvas.point(lambda p: 0 if p == 128 else 255, mode="L")
    
    # Smooth edges with slight blur to remove harsh pixelation
    feathered = raw_alpha.filter(ImageFilter.GaussianBlur(1.0))
    
    im.putalpha(feathered)
    im.save(dst_path, "PNG", optimize=True)
    print(f"Successfully created: {dst_path} ({w}x{h})")

if __name__ == "__main__":
    items = ["bun_top", "patty", "cheese", "lettuce_tomato", "bun_bottom", "box_open", "box_closed"]
    for item in items:
        make_transparent(item)
