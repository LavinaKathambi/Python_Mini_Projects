'''
1. Get a list of the file names
2. Extract the place names from the file names
3. Make a directory for each place name
4. Move files into the right directories
'''

import os
# FUNCTION 1: This function makes folders for each destination

def make_place_directories(places): 
    for place in places:
        os.mkdir(place)

# FUNCTION 2: This function extracts the destination names from the long name extension

def extract_place(filename):
    return filename.split('_')[1]

# FUNCTION 3: This is the main function, navigates to the folder we want to organize 

def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = [] # a list variable to store all the destinations
    for filename in originals:
        place = extract_place(filename) # extract the destination name
        if place not in places: 
            places.append(place) # add to the destinations list

    # call this function to create a folder for each destination
    make_place_directories(places)

    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename)) # move the pics to a new folder

organize_photos("Photos")