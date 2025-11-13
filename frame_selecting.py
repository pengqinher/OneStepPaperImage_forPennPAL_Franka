import os
import shutil
import argparse
from PIL import Image

def select_uniform_frames(input_dir, output_dir, num_frames=8):
    """
    Select a specified number of frames uniformly from all images in a folder.
    
    Args:
        input_dir: Input directory containing images
        output_dir: Output directory for selected frames
        num_frames: Number of frames to select (default: 8)
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Supported image formats
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.webp')
    
    # Get all image files from input directory and sort them
    image_files = [f for f in os.listdir(input_dir) 
                  if f.lower().endswith(supported_formats)]
    
    if not image_files:
        print(f"No image files found in {input_dir}")
        return
    
    # Sort image files to ensure consistent ordering
    image_files.sort()
    
    total_images = len(image_files)
    
    print(f"Found {total_images} image files")
    print(f"Selecting {num_frames} frames uniformly")
    
    # If we have fewer images than requested frames, adjust the number
    if total_images < num_frames:
        print(f"Warning: Only {total_images} images available, selecting all")
        num_frames = total_images
    
    # Calculate the indices for uniform selection
    if num_frames == 1:
        # If only selecting one frame, choose the middle one
        indices = [total_images // 2]
    else:
        # Calculate step size for uniform selection
        step = (total_images - 1) / (num_frames - 1)
        indices = [int(round(i * step)) for i in range(num_frames)]
    
    # Select and copy the frames
    selected_count = 0
    for i, idx in enumerate(indices):
        if idx < total_images:  # Ensure index is within bounds
            src_path = os.path.join(input_dir, image_files[idx])
            dst_path = os.path.join(output_dir, f"frame_{i+1:03d}_{image_files[idx]}")
            
            # Copy the image file
            shutil.copy2(src_path, dst_path)
            selected_count += 1
            print(f"Selected: {image_files[idx]} -> frame_{i+1:03d}_{image_files[idx]}")
    
    print(f"/nSelection completed!")
    print(f"Successfully selected {selected_count} frames")
    print(f"Output directory: {output_dir}")

def main():
    parser = argparse.ArgumentParser(description='Select uniform frames from a folder of images')
    parser.add_argument('input_dir', help='Input directory containing images')
    parser.add_argument('-o', '--output', default='selected_frames', 
                       help='Output directory (default: selected_frames)')
    parser.add_argument('-n', '--number', type=int, default=8, 
                       help='Number of frames to select (default: 8)')
    
    args = parser.parse_args()
    
    select_uniform_frames(args.input_dir, args.output, args.number)

if __name__ == "__main__":
    # Example usage
    input_directory = "C:/Users/pengqh/Desktop/develop/25455306_frames_after/"  # Change to your input directory
    output_directory = input_directory+"selected_frames"
    number_of_frames = 8
    
    select_uniform_frames(input_directory, output_directory, number_of_frames)