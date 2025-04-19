import sys
from datetime import datetime
print(sys.executable)
import cv2
import os
from tkinter import filedialog, Tk, simpledialog
from pathlib import Path
from tkinter.simpledialog import askstring

def select_file():
    """Open a file dialog to select a video file and get a custom name for the frames."""
    root = Tk()
    root.withdraw()  # Hide the main window
    
    # First select the video file
    file_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[
            ("Video files", "*.mp4 *.avi *.mov *.mkv"),
            ("All files", "*.*")
        ]
    )
    
    if file_path:
        # Then get custom name from user
        custom_name = askstring("Input", "Enter a name for the frame files:")
        return file_path, custom_name if custom_name else None
    
    return None, None

def create_output_folder(video_path, custom_name):
    """Create an output folder based on the custom name."""
    # Use custom_name for the folder name, or 'frames' if none provided
    folder_name = custom_name if custom_name else "frames"
    output_folder = os.path.join("image_data", folder_name)
    os.makedirs(output_folder, exist_ok=True)
    print(f"Saving frames to: {output_folder}")
    return output_folder

def extract_frames(video_path, output_folder, custom_name=None):
    """Extract frames from the video and save them sequentially."""
    # Preset settings
    settings = {
        'fps': 2,             # Extract 5 frames per second
        'max_frames': 20,      # 0 means no limit
        'resize': 95,         # 50% of original size
        'quality': 95         # JPEG quality
    }
    
    current_date = datetime.now().strftime("%Y%m%d")
    video = cv2.VideoCapture(video_path)
    
    # Get video information
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    original_fps = video.get(cv2.CAP_PROP_FPS)
    
    print(f"Total frames: {total_frames}")
    print(f"Original FPS: {original_fps}")
    print(f"Settings: {settings}")
    
    # Calculate frame extraction interval
    if settings['fps'] > 0:
        frame_interval = int(original_fps / settings['fps'])
    else:
        frame_interval = 1
    
    frame_count = 0
    saved_count = 0
    
    while True:
        success, frame = video.read()
        if not success:
            break
            
        # Skip frames based on desired fps
        if frame_count % frame_interval != 0:
            frame_count += 1
            continue
            
        # Check if we've reached max frames
        if settings['max_frames'] > 0 and saved_count >= settings['max_frames']:
            break
            
        # Resize the frame if needed
        if settings['resize'] != 100:
            width = int(frame.shape[1] * settings['resize'] / 100)
            height = int(frame.shape[0] * settings['resize'] / 100)
            frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
        
        # Save the frame
        prefix = custom_name if custom_name else "frame"
        frame_path = os.path.join(output_folder, f"{prefix}_{current_date}_{saved_count:06d}.jpg")
        
        # Save with specified quality
        encode_params = [cv2.IMWRITE_JPEG_QUALITY, settings['quality']]
        cv2.imwrite(frame_path, frame, encode_params)
        
        saved_count += 1
        frame_count += 1
        
        # Update progress
        if saved_count % 10 == 0:
            progress = (frame_count / total_frames) * 100
            print(f"Progress: {progress:.1f}% (Saved frames: {saved_count})")
    
    video.release()
    print("Extraction complete!")
    print(f"Total frames saved: {saved_count}")
    print(f"Frames saved in folder: {output_folder}")

def main():
    print("Please select a video file...")
    video_path, custom_name = select_file()
    
    if not video_path:
        print("No file selected. Exiting...")
        return
        
    output_folder = create_output_folder(video_path, custom_name)
    print(f"Processing video: {video_path}")
    extract_frames(video_path, output_folder, custom_name)

if __name__ == "__main__":
    main() 