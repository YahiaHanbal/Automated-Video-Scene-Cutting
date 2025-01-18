# Question Detection from Video Frames

## Overview
This script processes a video file, detects text in specific frames, and identifies questions in the format "Question X" where `X` is a number. It logs the results in a real-time table format and generates a final table of unique detected questions along with their timestamps.

## Features
- Processes video frames at a set interval to optimize performance.
- Uses OCR (Optical Character Recognition) via `pytesseract` to extract text from video frames.
- Detects and logs questions in the format "Question X".
- Displays a real-time log table with frame details and detected questions.
- Generates a final table of unique questions and their corresponding timestamps.

## Requirements
Ensure the following dependencies are installed:
- Python 3.x
- OpenCV (`cv2`)
- Tesseract OCR (`pytesseract`)

To install the required libraries, run:
```bash
pip install opencv-python pytesseract
```

Additionally, install Tesseract OCR on your system:
- For Windows: [Tesseract Download](https://github.com/tesseract-ocr/tesseract)
- For macOS: `brew install tesseract`
- For Linux: `sudo apt-get install tesseract-ocr`

## Usage
1. Place the video file (e.g., `vid1.mp4`) in the same directory as the script.
2. Update the `video_path` variable in the script with the path to your video file:
   ```python
   video_path = "vid1.mp4"
   ```
3. Run the script:
   ```bash
   python detect_text_and_log_questions.py
   ```

## Output
### Real-Time Log Table
During processing, the script logs detected questions in a table format:
```
Frame      Time (s)        Detected Question     Question Change
------------------------------------------------------------
0          0.00            No question detected   ---------------
120        4.00            Question: 1           ---------------
240        8.00            Question: 2           ---------------
```

### Final Table of Unique Questions
At the end of the script, a table of unique detected questions and their timestamps is displayed:
```
Final Questions Detected:
Question Number  Time (s)
------------------------
1                4.00
2                8.00
```

## Code Explanation
1. **Video Initialization**:
   - Opens the video file using OpenCV and retrieves metadata like frame rate and total frame count.

2. **Frame Processing**:
   - Processes every 120th frame to optimize performance.
   - Converts each frame to grayscale for better OCR accuracy.

3. **Text Detection**:
   - Extracts text from each frame using `pytesseract`.
   - Identifies the word "Question" followed by a number.

4. **Logging**:
   - Logs detected questions and their details (frame, timestamp) in a live table.

5. **Final Table**:
   - Compiles a table of unique questions and their timestamps.

## Customization
- **Frame Interval**:
  Adjust the frame interval by changing `range(0, frame_count, 120)` in the script. For example, to process every 60th frame:
  ```python
  for frame_num in range(0, frame_count, 60):
  ```

- **Text Detection Criteria**:
  Modify the text detection logic to fit your specific requirements (e.g., different keywords or patterns).

## Troubleshooting
- **No Questions Detected**:
  Ensure the video contains text in a readable format. Poor lighting or low resolution can affect OCR accuracy.
- **Error: Tesseract Not Found**:
  Ensure Tesseract OCR is installed and added to your system’s PATH.

## License
This script is released under the MIT License.

## Acknowledgments
- [OpenCV](https://opencv.org/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

