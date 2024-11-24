from CogBook import label_faces
from PIL import Image
from camera import take_picture
import numpy as np
import skimage.io as io

while True:
    choice = input("Upload (u) or take a photo (c)? ")
    
    if choice=="u":
        filepath = input("Filepath: ")
        # pic = np.array(Image.open(filepath))[:,:,:3]
        # shape-(Height, Width, Color)
        pic = io.imread(str(filepath))
        if pic.shape[-1] == 4:
            # Image is RGBA, where A is alpha -> transparency
            # Must make image RGB.
            pic = pic[..., :-1]  # png -> RGB
        label_faces(pic)
        break
    elif choice=="c":
        pic = take_picture()
        label_faces(pic)
        break
    else:
        print("Invalid input. Try again. ")
