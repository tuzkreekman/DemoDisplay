# Code for demo

SETUP.md has the instructions for installation needed packages


## Code setup

`svhn_extractor.py` reads the test matrix of images from the pi downloads folder
and writes the first 1000 images to imgs/svhn_.....png

The images then have to be moved to /home/pi/Downloads/imgs

Then run `bash get_random_test_images.sh` to get a subset of images

Code assumes that the app is installed in `/home/pi/Desktop/DemoDisplay`
(Change this in `app.kv` if need be)

## Basic run

`python basic_canvas.py` should pop the application up on your tablet

## Demo modification

Edit `communicator.py` to substitute in the operations

