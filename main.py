import cv2
import pytesseract


# Function to detect questions from the video and log in a table format
def detect_text_and_log_questions(video_path):
    try:
        # Initialize video capture to read the video file
        cap = cv2.VideoCapture(video_path)

        # Get the video properties: frames per second (FPS) and total frame count
        fps = int(cap.get(cv2.CAP_PROP_FPS))  # Frames per second
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Total frames
        duration = frame_count / fps  # Total duration of the video in seconds

        # If the video doesn't have proper FPS or frames, raise an error
        if fps == 0 or frame_count == 0:
            raise ValueError("Invalid video metadata. Check the file.")

        # Print basic video info
        print(f"Video loaded: {frame_count} frames at {fps} FPS, duration: {duration:.2f}s")

        last_question_number = 0  # Variable to store the last detected question number
        start_time = 0  # Start time for detecting question change

        # List to store unique questions and their timings
        detected_questions = []

        # Print header for the log table
        print(f"{'Frame':<10} {'Time (s)':<15} {'Detected Question':<20} {'Question Change'}")
        print("-" * 60)

        # Process the video frame by frame (every 120th frame)
        for frame_num in range(0, frame_count, 120):  # Process 1 frame every 120 frames
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)  # Set the frame to process
            ret, frame = cap.read()  # Read the frame
            if not ret:
                print(f"Frame {frame_num} could not be read. Skipping.")
                continue  # Skip if the frame couldn't be read

            # Convert the frame to grayscale for better text detection
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Use pytesseract to extract text from the grayscale frame
            detected_text = pytesseract.image_to_string(gray_frame).strip()

            # Initialize question_number to None
            question_number = None

            # Split the detected text into words and check for the word "question"
            words = detected_text.lower().split()  # Convert to lowercase and split into words
            for i, word in enumerate(words):
                if word == "question" and i + 1 < len(words) and words[i + 1].isdigit():
                    question_number = int(words[i + 1])  # Extract the number after "question"
                    break  # Stop searching once a question is found

            # Check if a question was detected and log it in a table format
            if question_number:
                print(f"{frame_num:<10} {frame_num / fps:<15.2f} {f'Question: {question_number}':<20} {'-' * 15}")
            else:
                print(f"{frame_num:<10} {frame_num / fps:<15.2f} {'No question detected':<20} {'-' * 15}")

            # Check if the question number has changed and log the change
            if question_number is not None and question_number > last_question_number:
                if last_question_number > 0:
                    print(
                        f"Question changed from {last_question_number} to {question_number} at {frame_num / fps:.2f}s")
                start_time = frame_num / fps  # Update the start time of the question
                last_question_number = question_number  # Update the last question number

                # Add unique questions and their corresponding times to the list
                if all(q[0] != question_number for q in detected_questions):
                    detected_questions.append((question_number, frame_num / fps))

        # Release the video capture object after processing
        cap.release()

        # Print the final table with unique detected questions and their timings
        print("\nFinal Questions Detected:")
        print(f"{'Question Number':<15} {'Time (s)'}")
        print("-" * 30)
        for question_number, time in detected_questions:
            print(f"{question_number:<15} {time:.2f}")

        print("Processing completed successfully!")

    except Exception as e:
        print(f"Error: {e}")  # Print error message if any exception occurs


# Example usage
video_path = "vid2.mp4"  # Path to the video file
detect_text_and_log_questions(video_path)
