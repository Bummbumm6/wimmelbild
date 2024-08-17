from PIL import Image
from time import time
import numpy as np
import ast, sys
import json
import re

decompress = str.maketrans(
    'NOPQRSTfVWXYZonpqrstuvxwyzABEDCFGHIJKLMac1234567890dmUghijkleb.,*/|-_',
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz1234567890)(,][_-')

timer = time()
try:
    f = open(sys.argv[1], "r+", encoding="utf-8")
except IndexError:
    exit("USAGE: wimmelbildviewer <file>")
print("Open File: "+str(time()-timer))

timer = time()
image = f.read()
image = re.sub("📓",".🌌UiU💫mU*el💫🌠",image)
image = re.sub("📐",".🌌U🌠💫🌠💫🌠💫🌠",image)
image = re.sub("🎨",".🌌🌟e💫he💫he💫🌠",image)
image = re.sub("🖍️", ".🌌Uih💫ih💫ih💫",image)
image = re.sub("⭐","🧤🧤🧤🧤🧤🧤",image)
image = re.sub("🧤","🌨️🪐🌨️🪐🌨️🪐",image)
image = re.sub("🌨️","🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌",image)
image = re.sub("🌦️","🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐🌌🪐",image)
image = re.sub("🧣","/*|,",image)
image = re.sub("🌕","🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐🪐",image)
image = re.sub("🪐","🌟l💫🧶💫🧶💫🌠.",image)
image = re.sub("✨","Ui,",image)
image = re.sub("🌌","*,",image)
image = re.sub("🧶","hl",image)
image = re.sub("🌠","ii",image)
image = re.sub("🌟","Uh",image)
image = re.sub("💫","*U",image)
image = re.sub('WIMMELBILDFILE__OWO','',image)
image = re.sub('OwO__WIMMELBILDFILE','',image) 
print("Replace: "+str(time()-timer))
timer = time()
image = image.translate(decompress)
print("Decompress: "+str(time()-timer))
timer = time()
image = json.loads(image)
print("Evaluate: "+str(time()-timer))
timer = time()
image = np.asarray(image)
print("Load: "+str(time()-timer))
timer = time()
im = Image.fromarray(image.astype(np.uint8))
print("Convert: "+str(time()-timer))
timer = time()
im.show()
print("View: "+str(time()-timer))
