from skimage import io
import os
import shutil
import numpy as np
import time
import cv2
import face_recognition as fr

directories = ["./data/" + d for d in ["autumn/", "winter/", "summer/", "spring/"]]

def find_faces(directory):
    photos = []
    for f in os.listdir(directory):
        photos.append(directory+f)

    photos_with_faces = []
    print(len(photos), "total photos in", directory)
    for i, p in enumerate(photos):
        if i % 1000 == 0:
            print(i, "photos checked", len(photos_with_faces), "photos with faces found")
        im = io.imread(p)

        if len(fr.face_locations(im)):
            photos_with_faces.append(p)
    print(len(photos_with_faces), "total photos with faces found")
    return photos_with_faces

def delete_photos(photos):
    for photo in photos:
        os.remove(photo)

for directory in directories:
    delete_photos(find_faces(directory))

