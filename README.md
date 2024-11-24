# CogWorks 2022 Gausslien Vision Capstone

## Instructions

### Image Identification

Adding Images to Database
1. Name image(s) with \[name]\_\[identifier].\[extension]. Make sure the filename is not already taken in the Loaded_Images folder
2. Move the new image(s) to the Images folder
3. Run the update_database.py script

Clearing the Database and Resetting Images
1. Run the reset_database.py script'

Running the face detector on a new image
1. Run the main.py script and follow the prompts

### Identifying Distinct Individuals

Running the Whispers Algorithm for Identification
1. Run the test.ipynb Jupyter Notebook
      * If the images have already been organized into separate folders by a previous run, use the move_back() method from whiskers.py

Changing the Image Set
1. Add or remove images from the Whiskers_Images folder
