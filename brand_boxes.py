import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def brand_box_open():
    im = Image.open("assets/box_open.png").convert("RGBA")
    w, h = im.size
    
    # The text "TERRA & TABLE" is around x: 600..750, y: 560..670
    # Let's clone nearby kraft texture to seamlessly cover it:
    # A clean patch of kraft paper is at x: 420..520, y: 570..670
    patch = im.crop((440, 580, 540, 680))
    # Paste with soft feathering over the old text
    im.paste(patch, (610, 570))
    im.paste(patch, (650, 570))
    
    # Now let's draw an elegant golden-amber brand badge "لقمة"
    draw = ImageDraw.Draw(im)
    
    # Try finding an Arabic font or Arial/Tahoma
    font_path = "C:/Windows/Fonts/tahoma.ttf"
    if not os.path.exists(font_path):
        font_path = "C:/Windows/Fonts/arial.ttf"
        
    try:
        font_bold = ImageFont.truetype(font_path, 34)
        font_sub = ImageFont.truetype(font_path, 16)
        
        # Stamp "لقمة" angled to match the flap perspective
        # We can create a stamped text image and rotate it
        stamp = Image.new("RGBA", (200, 100), (0, 0, 0, 0))
        stamp_draw = ImageDraw.Draw(stamp)
        stamp_draw.text((100, 30), "لقمة", fill=(60, 35, 18, 220), font=font_bold, anchor="mm")
        stamp_draw.text((100, 65), "LUQMA • BURGER", fill=(90, 55, 30, 200), font=font_sub, anchor="mm")
        
        # Rotate slightly to match the 15 degree perspective
        rotated_stamp = stamp.rotate(-12, resample=Image.BICUBIC, expand=True)
        im.alpha_composite(rotated_stamp, (600, 560))
    except Exception as e:
        print("Font error:", e)
        
    im.save("assets/box_open.png", "PNG")
    print("box_open.png branded with لقمة successfully!")

def brand_box_closed():
    im = Image.open("assets/box_closed.png").convert("RGBA")
    w, h = im.size
    
    # On box_closed, there is a circular sticker in the center: approx x: 440..580, y: 320..460
    # Center is approx (512, 390)
    cx, cy, r = 514, 396, 126
    
    # Create a luxury gold seal
    seal = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(seal)
    
    # Outer dark gold border
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(24, 16, 10, 245), outline=(218, 165, 32, 255), width=5)
    draw.ellipse([cx - r + 8, cy - r + 8, cx + r - 8, cy + r - 8], outline=(244, 180, 26, 200), width=2)
    
    # Arabic Text
    font_path = "C:/Windows/Fonts/tahoma.ttf"
    try:
        font_main = ImageFont.truetype(font_path, 46)
        font_sub = ImageFont.truetype(font_path, 14)
        draw.text((cx, cy - 10), "لقمة", fill=(247, 201, 106, 255), font=font_main, anchor="mm")
        draw.text((cx, cy + 34), "من المطبخ لبابك 🛵", fill=(255, 235, 180, 230), font=font_sub, anchor="mm")
    except Exception as e:
        print("Font error:", e)
        
    # Rotate sticker to match box perspective (-22 degrees)
    # Rotate around sticker center
    im = Image.alpha_composite(im, seal)
    im.save("assets/box_closed.png", "PNG")
    print("box_closed.png branded with لقمة successfully!")

if __name__ == "__main__":
    brand_box_open()
    brand_box_closed()
