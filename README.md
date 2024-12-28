# Video Scene Splitter

## Description
This project automates splitting long videos into smaller clips by detecting scene changes, such as PowerPoint slide transitions. It analyzes frame differences to find significant changes and saves each segment as a separate clip, making it easier to navigate specific sections of the video.

## Features
- Automatically detects significant scene changes.
- Splits videos into smaller, organized clips.
- Outputs clips to a user-defined directory.

## Requirements
- Python 3.7 or higher
- Required Python libraries:
  - OpenCV
  - MoviePy

Install dependencies using:
```bash
pip install opencv-python moviepy
```
## How to use
- Place your video file in the same directory as the script.
- Open the script and update the video_path variable with your video file name or path.
- Run the script:

## Example Output
- output_clips/clip_1.mp4
- output_clips/clip_2.mp4
- output_clips/clip_3.mp4
