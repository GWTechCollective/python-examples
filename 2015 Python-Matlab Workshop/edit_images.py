##
#   Python Image Manipulation Example
#   Mark Tentindo - markten@gwu.edu
#   2015 GWTC Python-MatLab Workshop
##

import os
import glob
from PIL import Image
import matplotlib.pyplot as plt

## Define a function to open a file, detect edges, and save the result
def image_to_grayscale(inputFile, outputFolder):
    imageData = Image.open(inputFile)
    imageData = imageData.convert('LA')
    plt.imshow(imageData)
    outputPath = os.path.join(outputFolder, os.path.basename(inputFile))

    plt.savefig(outputPath)
    return

## Config Variables
# I like to set up a few directories that I can just drop files into and
# have the code do its thing.I usually leave the folder name at the top of
# the script so its easy to edit.
INPUT_DIR = os.path.join(os.getcwd(), 'raw_images')
OUTPUT_DIR = os.path.join(os.getcwd(), 'proc_images')

## Iterate the Analysis over the Images

# we use the glob module with the wildcard "*" operator to select any file with the JPG extension
inputPath = os.path.join(INPUT_DIR, '*.jpg')
images = glob.glob(inputPath)

# Check that we actually have something to process
if not images:
    print('!!! No images found in input directory !!!')

else:
    # iterate through all the images performing processing and saving the
    # results in the output folder
    print('Analyzing Files...')

    for image in images:
        print('\t{0}'.format(os.path.basename(image)))
        image_to_grayscale(image, OUTPUT_DIR)

print('Analysis Complete.')
