#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Mohamed Gamal AbdElKhalek
# DATE CREATED: 2/5/2020                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
#
def creat_label_from_name(file_name):
    """
    Return pet label equivelent to file name
    (ex. filename = 'Boston_terrier_02259.jpg' ==> Pet label = 'boston terrier')
    Parameters:
     file_name  (string)
    Returns:
      label (string)
    """    
    file_name_components = file_name.lower().split("_")
    # Create pet_label starting as empty string
    label = ""
    for component in file_name_components:
        # Loops to check if word in pet name is only
        # alphabetic characters - if true append word
        # to pet_label separated by trailing space 
        if component.isalpha():
            label += component + " "

    # Strip off starting/trailing whitespace characters 
    label = label.strip()
    
    return label

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    
    # Retrieve the filenames from folder pet_images/
    filename_list = listdir(image_dir)
    filename_list.sort()                # Group pets by name by sorting

    pet_key=[]                          # Use list container for labels
    pet_value=[[]]                      # Use list of lists for file names
    for file_name in filename_list:
        label = creat_label_from_name(file_name)
        if(len(pet_key) == 0):
            # Added to handle out of index exception
            # The first file name will automatically be added to first element of list
            pet_key.append(label)
            pet_value.append([file_name])
        elif (label == pet_key[-1]):
            # If label already exists just add this file name to equivlelent file names list
            # We need only to check the last label as the list is already listed
            pet_value[-1].append(file_name)
        else:
            # If label doesn't exist, Add new entry as label and file name list
            pet_key.append(label)
            pet_value.append([file_name])
    
    # Use the lists to return dictionary and the lists will be distroyed 
    return zip(pet_key,pet_value)