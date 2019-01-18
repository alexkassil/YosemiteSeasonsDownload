from skimage import io, draw
from imutils.object_detection import non_max_suppression
from matplotlib import pyplot as plt
import os
import numpy as np
import time
import cv2

directories = ["./data/" + d for d in ["autumn/", "winter/", "summer/", "spring/"]]

layerNames = [
            "feature_fusion/Conv_7/Sigmoid",
            "feature_fusion/concat_3"]

net = cv2.dnn.readNet("frozen_east_text_detection.pb")

def find_text(directory):
    photos = []
    for f in os.listdir(directory):
        photos.append(directory+f)

    def has_text(image):
        (newW, newH) = (320, 320)
        (H, W) = image.shape[:2]
        rW = W / float(newW)
        rH = H / float(newH)
        image = cv2.resize(image, (newW, newH))
        (H, W) = image.shape[:2]
        
        blob = cv2.dnn.blobFromImage(image, 1.0, (W, H),
                (123.68, 116.78, 103.94), swapRB=True, crop=False)
        net.setInput(blob)
        (scores, geometry) = net.forward(layerNames)

        scores = scores[0, 0]
        return any(scores.reshape(scores.shape[0]*scores.shape[1]) > .5)

    photos_with_text = []
    print(len(photos), "total photos in", directory)
    for i, p in enumerate(photos):
        if i % 10 == 0:
            print(i, "photos checked", len(photos_with_text), "photos with text found")
        im = io.imread(p)

        if has_text(im):
            photos_with_text.append(p)
    print(len(photos_with_text), "total photos with text found")
    return photos_with_text

def move_photos(photos, destination):
    print(destination)
    for photo in photos:
        pass
        #shutil.move(photo, destination)

for directory in directories:
    move_photos(find_text(directory), directory[:-7] + "deleted_" + directory[-7:] + "text/")
