import os
import shutil
from pathlib import Path

def consolidate_images():
    # Define paths
    base_dir = Path("/Users/tobybrooks/video processor/image_data")
    output_dir = base_dir / "all_frames"
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    
    # Counter for unique filenames
    counter = 0
    
    # Walk through all subdirectories
    for root, dirs, files in os.walk(base_dir):
        # Skip the output directory itself
        if Path(root) == output_dir:
            continue
            
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                # Get the full path of the source file
                src_path = Path(root) / file
                
                # Create new filename with counter
                new_filename = f"frame_{counter:06d}{Path(file).suffix}"
                dst_path = output_dir / new_filename
                
                # Copy the file
                shutil.copy2(src_path, dst_path)
                print(f"Copied: {src_path} -> {dst_path}")
                
                counter += 1
    
    print(f"\nConsolidation complete!")
    print(f"Total images moved: {counter}")
    print(f"All images are now in: {output_dir}")

if __name__ == "__main__":
    consolidate_images() 