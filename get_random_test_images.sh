#!/bin/bash

# Clears the streetview folder then
# Gets a subset of the 1000 downloaded images
# and saves them in streetview folder


rm -r streetview
mkdir streetview

for i in {1..100} ; do
	index=$(($RANDOM % 1000))
	filename=/home/pi/Downloads/imgs/svhn_$index.png
	cp $filename streetview
done

