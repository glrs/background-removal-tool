# background-removal-tool
This tool removes the background of an image based on manually added markers (based on OpenCV)

I wrote this small script as an [answer](https://stackoverflow.com/a/43545744/4618605) to a StackOverflow question. However, I found myself using it quite often afterwards, thus I decided to make a repo so I can have easy access to it, and also make it accessible to other people that would like to use or shape it in their own application.

## TODOs
### Near future
* Pass the image file/path as argument
* Pass the markers as an argument
* Utility to iterate over a dataset of similar images

### Future
* Create a GUI that allow the user to place the markers visually
* Add function to the GUI for multiple images (can be exhausting for big datasets)
* Add function to the GUI to place the markers on the mean image of an image dataset
