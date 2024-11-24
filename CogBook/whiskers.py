import numpy as np
import random
from pathlib import Path
from connected_components import connected_components
from propagate_label import propagate_label
import os

""" The full whiskers algorithm

Parameters:
    iterations (int): number of iterations
    nodes (list): list of all nodes
    adj_matrix (np.array): the adjacency matrix

Returns: None, but prints grouping history as a list and organizes the images based on their groupings
"""
def whiskers(iterations: int, nodes: list, adj_matrix: np.array):
    
    # the algorithm
    num_grouping_history = []
    for i in range(0, iterations):
        node = nodes[random.randint(0, len(nodes)-1)]
        neighbors = [nodes[i] for i in node.neighbors]
        propagate_label(node, neighbors, adj_matrix)
        groupings = connected_components(nodes)
        num_grouping_history.append(len(groupings))
    print(num_grouping_history)
    
    # moves the images into folders based on their groupings
    cwd = Path.cwd()
    # makes a folder to hold all the images in this group
        
            
#         # moves the images in this group
    count = 0

    for key in groupings.keys():
        person_id = 'Person' + str(count+1)
        new_folder_path = cwd.parents[0] / person_id
        
        if not Path.exists(new_folder_path):
            new_folder_path.mkdir()
        for node in groupings[key]:
            file_path = str(Path(node.file_path).resolve())
            file_name = Path(file_path).name

            
            new_file_path = new_folder_path / file_name
            Path(file_path).rename(new_file_path)
        count+=1
            

"""
Tests to check if a single file can be moved properly
"""
def file_move_test(file_path: str, group_num: int):
    cwd = Path.cwd()
    person_id = 'Person' + str(group_num+1)
    new_folder_path = cwd.parents[0] / person_id
    
    if not Path.exists(new_folder_path):
        new_folder_path.mkdir()
    
    file_name = Path(file_path).name

    new_file_path = new_folder_path / file_name
    Path(file_path).rename(new_file_path)

"""
Moves the images back to the original folder
Parameters:
    num_folders (int): the number of folders created by the last run of the whispers algorithms,
                       needs to be from Folder 1 to Folder num_folders
"""
def move_back(num_folders: int):
    cwd = Path.cwd()
    for group_num in range(1, num_folders+1):
        person_id = 'Person' + str(group_num)
        folder_path = cwd.parents[0] / person_id
            
        files = []
        for filename in os.listdir(folder_path):
            f = os.path.join(folder_path, filename)
            if os.path.isfile(f):
                files.append(f)

        for file in files:
            file_name = Path(file).name
            new_file_path = cwd.parents[0]/ 'Whiskers_Images' / file_name
            Path(file).rename(new_file_path)
