# Picture-Perfect
Image expansion and capturing in an enhanced way for sceintific as well as personal usage

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# Objective
This hack can be utilized in:
- [x] Images of archeological, astronomical or other scientefic importance (as well as personal pictures) often require to be clicked at optimum 3d angles, brightness, etc. in order to preserve information in best manner.

- [x] Image expansion is useful in determining the background of the image to grasp important metadata. These can be used in analysis of images from crime scenes, drone captured images for surveilance and so on.

# How to use
A simple-to-use web interface will let you analyze any captured image and output relevant suggestions.

# How it actually works?
## Optimizing image capture
- Any input image is transformed in respect to image processing vectors (here) into 24 to 96 different versions that could be achieved from given scene.
- The mentioned variants are produced by implementation of image transform vectors (here) on the input image
- These variants are then sorted on the basis of brisque score for the image (here) and the best variant is chosen as desired image with relevant optimization factor:

- ```Optimization factor = image score for best variant/ image score of original image```

## Image expansion
- Any input image is treated as a 50x50 image
- This image is fed to a KNN model that was trained on a dataset of indoor images
- The ensemble of such models produces an array of predicted pixels after image expansion

## Experimental Results
- Average image optimisation so far: 1.34
- Image expansion accuracy (R2-score): 0.56707639

# References
- [Image Transformation, MIT Media Lab](http://web.media.mit.edu/~maov/classes/comp_photo_vision08f/lect/08_image_warps.pdf)
- [Image quality assessment](https://pypi.org/project/image-quality/)
- [Image dataset](http://web.mit.edu/torralba/www/indoor.html)
