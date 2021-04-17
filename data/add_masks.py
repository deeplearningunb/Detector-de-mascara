import os
from PIL import Image
parent_dir = 'nomask/'

for subdir, dirs, files in os.walk(parent_dir):
    for count, file in enumerate(files):
        image_path = os.path.join(subdir, file)
        img = Image.open(image_path)

        img2 = img.copy()
        
        mask = Image.open("mask2.png")

        img.paste(mask,(0,0),mask)
        
        img.save(f"withmask/withMask{count}.png")
        
        
