from skimage import io
import os
import numpy as np
import time


directories = ["./data/" + d for d in ["autumn/", "winter/", "summer/", "spring/"]]

def find_black_white(directory):
    photos = []
    for f in os.listdir(directory):
        photos.append(directory+f)

    bw = []
    print(len(photos), "total photos in", directory)
    for i, p in enumerate(photos):
        if i % 500 == 0:
            print(i, "photos checked", len(bw), "black/white photos found")
        # Convert from uint8 to int32 to avoid overflow when subtracting and allow to add up
        im = io.imread(p).astype(np.int32)
        # Photos that don't have color channel are black and white
        if len(im.shape) != 3:
            bw.append(p)
        # Check for photos who are almost the same color in all 3 color channels
        # 5 * height * width is used for cutoff because after testing that seemed to be the cutoff that
        # caught black and white photos whose color channels weren't perfectly off and didn't catch
        # very white/grey photos like snow or rocks that are in color
        elif np.sum(np.abs(im[:, :, 0] - im[:, :, 1]) + np.abs(im[:, :, 1] - im[:, :, 2]) + np.abs(im[:, :, 2] - im[:, :, 0])) <= 5*im.shape[0]*im.shape[1]:
            bw.append(p)

    print(len(bw), "total bw photos found")
    return bw

def delete_photos(photos):
    for photo in photos:
        os.remove(photo)


for directory in directories:
    delete_photos(find_black_white(directory))
