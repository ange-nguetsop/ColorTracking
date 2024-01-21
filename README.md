 Color Tracking using OpenCV

## Overview
This Python script utilizes the OpenCV library to perform real-time color tracking. It captures video from the default camera device and tracks three colors: red, green, and blue. The script displays the result in a window where only the tracked colors are visible, and it saves this output to an MP4 file.

## Requirements
- Python 3.x
- OpenCV-Python package

## Installation
Before running the script, ensure that you have Python and OpenCV installed. You can install OpenCV using pip:
pip install opencv-python

## Example
![Example](https://github.com/ange-nguetsop/ColorTracking/blob/master/Example.gif)

## How it Works
The script performs the following steps:

- Captures video from the default camera (webcam).
- Converts each video frame from BGR to HSV color space.
- Defines the range of colors to track (red, green, and blue) in HSV.
- Creates masks for each color and combines them.
- Applies the mask to the original frame, resulting in an image showing only the tracked colors.
- Writes the resultant image to an MP4 file.
- Displays the output in a window.

## Stopping the Script
To stop the script, focus on the output window and press the 'ESC' key.

## Customization
You can customize the script by changing the color ranges in the HSV color space to track different colors.

## Output
The script will create an MP4 file named 'Color_Tracking.mp4' in the directory where the script is located. This file contains the video output with only the tracked colors visible.

