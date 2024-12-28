import cv2
import pytesseract
import ffmpeg
import os

def detect_text_and_cut(video_path, output_dir):
    try:
        # Initialize video capture
        cap = cv2.VideoCapture(video_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps

        if fps == 0 or frame_count == 0:
            raise ValueError("Invalid video metadata. Check the file.")

        print(f"Video loaded: {frame_count} frames at {fps} FPS, duration: {duration:.2f}s")

        last_question_number = 0
        segments = []
        start_time = 0

        for frame_num in range(0, frame_count, 120):  # Process 1 frame every 120 frames
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
            ret, frame = cap.read()
            if not ret:
                print(f"Frame {frame_num} could not be read. Skipping.")
                continue

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            detected_text = pytesseract.image_to_string(gray_frame).strip()

            question_number = None
            words = detected_text.lower().split()
            for i, word in enumerate(words):
                if word == "question" and i + 1 < len(words) and words[i + 1].isdigit():
                    question_number = int(words[i + 1])
                    break

            if question_number:
                print(f"Frame {frame_num}, Time {frame_num / fps:.2f}s, Question: {question_number}")
            else:
                print(f"Frame {frame_num}, Time {frame_num / fps:.2f}s, No question detected")

            if question_number is not None and question_number > last_question_number:
                if last_question_number > 0:
                    segments.append((start_time, frame_num / fps))
                start_time = frame_num / fps
                last_question_number = question_number

        if start_time < duration:
            segments.append((start_time, duration))

        cap.release()

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Split the video using FFmpeg
        for i, (start, end) in enumerate(segments):
            try:
                output_file = os.path.join(output_dir, f"segment_{i + 1}.mp4")
                print(f"Creating segment {i + 1}: {start:.2f}s to {end:.2f}s")
                (
                    ffmpeg
                    .input(video_path, ss=start, to=end)
                    .output(output_file, codec='libx264', preset='slow', crf=18)
                    .run(quiet=True)
                )
                print(f"Segment {i + 1} created successfully: {output_file}")
            except ffmpeg.Error as e:
                print(f"Error creating segment {i + 1}: {e}")

        print("Processing completed successfully!")

    except Exception as e:
        print(f"Error: {e}")


# Example usage
video_path = r"D:\ELkheta\vid.mkv"
output_dir = r"D:\output"
detect_text_and_cut(video_path, output_dir)
