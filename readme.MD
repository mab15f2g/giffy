# GIF Converter

GIF Converter is a Python program that allows you to convert videos to GIF format using the `moviepy` library.

## Prerequisites

Before using the GIF Converter tool, ensure that the following prerequisites are met:

- Python 3.6 or higher is installed on your system.

## Installation

1. Clone this repository to your local machine or download the ZIP file.

2. Open a terminal or command prompt and navigate to the project directory.

3. Install the required Python dependencies by running the following command:

   ```shell
   pip install moviepy
   ```


# Usage

1.    Open the terminal or command prompt and navigate to the project directory.

2.    Run the gif_converter.py script using the following command:

    
3. ``` python gif_converter.py ```
    
4.    The GIF Converter tool's user interface (UI) will open.

5.    Use the "Select Input Folder" button to choose a folder containing the videos you want to convert to GIFs.

6.    Use the "Select Output Folder" button to choose a folder where the converted GIFs will be saved.

7.    Adjust the "Quality" and "Frame Rate" sliders to set the desired quality and frame rate for the GIFs.

8.   Click the "Convert" button to start the conversion process. The tool will convert all the videos in the input folder to GIFs with the specified quality and frame rate, and save them in the output folder.

 9.   The conversion progress and status of each video will be displayed in the console or terminal window.

10.    Once the conversion is complete, the tool will display a message indicating the completion.

# Notes

    The GIF Converter tool supports video files in the formats .mp4, .avi, and .mov.

    The number of CPU cores used for conversion is automatically determined and set to 75% of the available cores.

    The UI is responsive and adjusts to a window size of 640x480 pixels.

# License

This project is licensed under the MIT License.