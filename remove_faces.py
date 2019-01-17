from skimage import io, draw
from matplotlib import pyplot as plt
import os
import shutil
import numpy as np
import time
import cv2

directories = ["./data/" + d for d in ["autumn/", "winter/", "summer/", "spring/"]]

def find_faces(directory):
    photos = []
    for f in os.listdir(directory):
        photos.append(directory+f)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    def has_faces(img):
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.175,
            minNeighbors=5,
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        return len(faces) != 0

    photos_with_faces = []
    print(len(photos), "total photos in", directory)
    for i, p in enumerate(photos):
        if i % 1000 == 0:
            print(i, "photos checked", len(photos_with_faces), "photos with faces found")
        im = io.imread(p)

        if has_faces(im):
            photos_with_faces.append(p)
    print(len(photos_with_faces), "total photos with faces found")
    return photos_with_faces

def move_photos(photos, destination):
    for photo in photos:
        shutil.move(photo, destination)

for directory in directories:
    move_photos(find_faces(directory), directory[:-7] + "deleted_" + directory[-7:])
