#!/bin/bash

# number of parallel tasks to run downloading photos
N=16
for i in $(seq 1 $N)
do
	python2 download_photos.py $i $N &
done

