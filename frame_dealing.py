from PIL import Image
import os
import argparse

def process_images(input_dir, output_dir, splits_config=((2, 2),(1, 1)), rotation_angle=180):
    """
    Process all images in a folder: split images into multiple parts both horizontally and vertically, 
    keep one part, and rotate it by specified angle.
    
    Args:
        input_dir: Input directory containing images
        output_dir: Output directory for processed images
        splits_config: Tuple of (horizontal_splits, vertical_splits, horizontal_index, vertical_index)
                     (default: (2, 2, 1, 1) - split into 2x2, keep bottom-right part)
        rotation_angle: Rotation angle in degrees (default: 180)
    """
    # Unpack splits configuration
    horizontal_splits, horizontal_index= splits_config[0]
    vertical_splits,  vertical_index= splits_config[1]
    horizontal_index-=1
    vertical_index-=1
    # Validate parameters
    if horizontal_splits < 1 or vertical_splits < 1:
        print("Error: Both horizontal_splits and vertical_splits must be at least 1")
        return
    
    if horizontal_index < 0 or horizontal_index >= horizontal_splits:
        print(f"Error: horizontal_index must be between 0 and {horizontal_splits-1}")
        return
    
    if vertical_index < 0 or vertical_index >= vertical_splits:
        print(f"Error: vertical_index must be between 0 and {vertical_splits-1}")
        return
    
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
    print(f"Splitting each image into {horizontal_splits}x{vertical_splits} parts")
    print(f"Keeping part at position ({horizontal_index}, {vertical_index}) (0-based)")
    print(f"Rotation angle: {rotation_angle} degrees")
    
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
                
                # Calculate width and height of each split part
                part_width = width // horizontal_splits
                part_height = height // vertical_splits
                
                # Calculate the coordinates for the part to keep
                left = horizontal_index * part_width
                right = (horizontal_index + 1) * part_width if horizontal_index < horizontal_splits - 1 else width
                
                top = vertical_index * part_height
                bottom = (vertical_index + 1) * part_height if vertical_index < vertical_splits - 1 else height
                
                # Extract the specified part
                kept_part = img.crop((left, top, right, bottom))
                
                # Rotate the kept part
                processed_img = kept_part.rotate(rotation_angle)
                
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

def parse_splits_config(splits_str):
    """Parse splits configuration from string format 'h,v,hi,vi' to tuple"""
    try:
        parts = splits_str.split(',')
        if len(parts) != 4:
            raise ValueError("Splits config must have exactly 4 values")
        return tuple(int(x) for x in parts)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Invalid splits config: {e}")

def main():
    parser = argparse.ArgumentParser(description='Split images into multiple parts both horizontally and vertically, keep one part and rotate it')
    parser.add_argument('input_dir', help='Input directory containing images')
    parser.add_argument('-o', '--output', default='processed_images', 
                       help='Output directory (default: processed_images)')
    parser.add_argument('-s', '--splits', type=parse_splits_config, default=(2, 2, 1, 1),
                       help='Splits configuration as "horizontal_splits,vertical_splits,horizontal_index,vertical_index" (default: "2,2,1,1")')
    parser.add_argument('-r', '--rotation', type=float, default=180, 
                       help='Rotation angle in degrees (default: 180)')
    
    args = parser.parse_args()
    
    process_images(args.input_dir, args.output, args.splits, args.rotation)

if __name__ == "__main__":
    # Example usage
    input_directory = "C:/Users/pengqh/Desktop/develop/25455306_frames"
    output_directory = "C:/Users/pengqh/Desktop/develop/25455306_frames_after"
    
    # Various examples of splits_config:
    # (2, 1, 1, 0) - Split horizontally into 2 parts, keep right part (equivalent to original behavior)
    # (1, 2, 0, 1) - Split vertically into 2 parts, keep bottom part
    # (3, 2, 1, 0) - Split into 3 columns and 2 rows, keep middle-top part
    # (2, 2, 1, 1) - Split into 2x2 grid, keep bottom-right part
    
    splits_config = (2, 2, 1, 1)  # Split into 2x2, keep bottom-right part
    rotation_angle = 180
    
    process_images(input_directory, output_directory, splits_config, rotation_angle)