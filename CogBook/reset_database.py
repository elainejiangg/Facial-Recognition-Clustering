from shutil import move
import pickle
import os

emptyDict = {}
with open("profiles.pkl", 'wb') as f:
    pickle.dump(emptyDict, f)

directory = '../Images'
loadedDir = '../Loaded_Images'

for filename in os.listdir(loadedDir):
    filepath = os.path.join(loadedDir, filename)
    destination = os.path.join(directory, filename)
    
    if os.path.isfile(filepath):
        move(filepath, destination)
