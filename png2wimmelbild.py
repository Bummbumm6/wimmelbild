# Please don't use this except if you're sure you really want to...

from PIL import Image
import json
import sys

compress = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz1234567890)(,][_-',
    'NOPQRSTfVWXYZonpqrstuvxwyzABEDCFGHIJKLMac1234567890dmUghijkleb.,*/|-_')

im = Image.open(sys.argv[1])

pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
pixels = json.dumps(pixels)

image = 'WIMMELBILDFILE__OWO' + str(pixels).replace(" ","").translate(compress) + 'OwO__WIMMELBILDFILE'
image = image.replace("*U","💫")
image = image.replace("Uh","🌟")
image = image.replace("ii","🌠")
image = image.replace("hl","🧶")
image = image.replace("*,","🌌")
image = image.replace("Ui,","✨")
image = image.replace("🌟l💫🧶💫🧶💫🌠.","🪐")
image = image.replace("🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐","🌕")
image = image.replace("/*|,","🧣")
image = image.replace("🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐","🌦️")
image = image.replace("🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌","🌨️")
image = image.replace("🌨️🪐🌨️🪐🌨️🪐","🧤")
image = image.replace("🧤🧤🧤🧤🧤🧤","⭐")
image = image.replace(".🌌Uih💫ih💫ih💫","🖍️")
image = image.replace(".🌌🌟e💫he💫he💫🌠","🎨")
image = image.replace(".🌌U🌠💫🌠💫🌠💫🌠", "📐")
image = image.replace(".🌌UiU💫mU*el💫🌠","📓")

try:
    f = open("image.wimmelbild", "w+", encoding="utf-8")
except IndexError:
    exit("USAGE: python3 wimmelbild2png.py <file>")

f.write(image)  
