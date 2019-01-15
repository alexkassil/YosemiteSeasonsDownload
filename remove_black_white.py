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
        elif np.sum(np.abs(im[:, :, 0] - im[:, :, 1]) + np.abs(im[:, :, 1] - im[:, :, 2]) + np.abs(im[:, :, 2] - im[:, :, 0])) <= 5*im.shape[0]*im.shape[1]:
            bw.append(p)

    print(len(bw), "total bw photos found")
    return bw

def delete_photos(photos):
    pass


for directory in directories:
    find_black_white(directory)
