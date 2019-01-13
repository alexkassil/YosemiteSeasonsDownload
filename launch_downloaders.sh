#!/bin/bash

# number of parallel tasks to run downloading photos
N=16
for i in $(seq 1 $N)
do
	python2 download_photos.py $i $N fall &
	python2 download_photos.py $i $N winter &
	python2 download_photos.py $i $N summer &
	python2 download_photos.py $i $N spring &
	python2 download_photos.py $i $N autumn &

done

