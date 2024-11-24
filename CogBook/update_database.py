from CogBook import *
import skimage.io as io
#from PIL import Image
from shutil import move

import pickle
import numpy as np
import os



# assign directory
directory = '../Images'
loadedDir = '../Loaded_Images'

# iterate over files in
# that directory
fileList = []

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    destination = os.path.join(loadedDir, filename)
    
    if os.path.isfile(filepath):
        fileList.append((filepath, filename, destination))


profileDB = load_profiles_from_file()

for fileInfo in fileList:
    print(fileInfo[1])

    name, number = fileInfo[1].split(".")[0].split("_")
    

    img_data = io.imread(str(fileInfo[0]))

    if img_data.shape[-1] == 4:
        img_data = img_data[..., :-1]
    
    # img_data = np.array(Image.open(fileInfo[0]))[:,:,:-1]
    descriptors = get_descriptors(img_data)
    
    save_vector_to_profile(profileDB, name, descriptors[0])
    
    move(fileInfo[0], fileInfo[2])
    
save_profiles_to_file(profileDB)
