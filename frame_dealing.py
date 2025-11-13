from PIL import Image
import os
import argparse

def process_images(input_dir, output_dir):
    """
    Process all images in a folder: split into left/right halves, 
    keep only right half, rotate 180 degrees and save.
    
    Args:
        input_dir: Input directory containing images
        output_dir: Output directory for processed images
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Supported image formats
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif')
    
    # Get all image files from input directory
    image_files = [f for f in os.listdir(input_dir) 
                  if f.lower().endswith(supported_formats)]
    
    if not image_files:
        print(f"No image files found in {input_dir}")
        return
    
    print(f"Found {len(image_files)} image files")
    
    processed_count = 0
    
    for filename in image_files:
        try:
            # Open image
            input_path = os.path.join(input_dir, filename)
            with Image.open(input_path) as img:
                # Convert to RGB if necessary
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                width, height = img.size
                
                # Split into left and right halves
                left_half = img.crop((0, 0, width // 2, height))
                right_half = img.crop((width // 2, 0, width, height))
                
                # Keep only right half and rotate 180 degrees
                processed_img = right_half.rotate(180)
                
                # Save processed image
                output_path = os.path.join(output_dir, filename)
                processed_img.save(output_path)
                
                processed_count += 1
                print(f"Processed: {filename}")
                
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
    
    print(f"\nProcessing completed!")
    print(f"Successfully processed {processed_count} out of {len(image_files)} images")
    print(f"Output directory: {output_dir}")

# def main():
#     parser = argparse.ArgumentParser(description='Split images into halves, keep right half and rotate 180 degrees')
#     parser.add_argument('input_dir', help='Input directory containing images')
#     parser.add_argument('-o', '--output', default='processed_images', 
#                        help='Output directory (default: processed_images)')
    
#     args = parser.parse_args()
    
#     process_images(args.input_dir, args.output)

if __name__ == "__main__":
    # Example usage
    input_directory = "C:/Users/pengqh/Desktop/develop/25455306_frames"  # Change to your input directory
    output_directory = "C:/Users/pengqh/Desktop/develop/25455306_frames_after"
    
    process_images(input_directory, output_directory)