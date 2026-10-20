from PIL import Image
import glob

for f in sorted(glob.glob("assets/*.png")):
    im = Image.open(f)
    alpha = im.split()[-1]
    print(f, im.size, "alpha min/max:", alpha.getextrema(), "bbox:", alpha.getbbox())
