# background-removal-tool
This tool removes the background of an image based on manually added markers (based on OpenCV)

I wrote this small script as an [answer](https://stackoverflow.com/a/43545744/4618605) to a StackOverflow question. However, I found myself using it quite often afterwards, thus I decided to make a repo so I can have easy access to it, and also make it available for other people that would like to use or shape it in their own application.

The script is based on OpenCV (cv2) library. The first step is to select several points/markers (pixel coordinates) to dictate the object you want to keep. This essentially means that this code actually keeps what you want from an image, and dumps the rest (rather than just removing the background). After you get the points, they are projected on an integer array of zeros to be used as a mask (the points should be a non-zero number [1, 255]). Then the watershed algorithm is used, taking the image and the mask as input. The resulting image is dilated by a small kernel (currently set to 3x3 pixels), to avoid losing information on the perimeter of the desired object. Finally, the dilated image is used as a mask to the original image (using the cv2.bitwise_and()). Then saves the image in a preset name.

## TODOs
### Near future
* Pass the image file/path as argument
* Pass the markers as an argument
* Pass the output filename as an argument
* Utility to iterate over a dataset of similar images

### Future
* Create a GUI that allow the user to place the markers visually
* Add function to the GUI for multiple images (can be exhausting for big datasets)
* Add function to the GUI to place the markers on the mean image of an image dataset
* Make it a proper tool and give it a proper name
