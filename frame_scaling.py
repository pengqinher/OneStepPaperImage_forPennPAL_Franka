from PIL import Image
import os
import argparse

def crop_and_resize_images(input_dir, output_dir, scale_factor=0.8, position='bottom-left'):
    """
    Crop images to keep a specific corner/position with original aspect ratio,
    then resize back to original dimensions.
    
    Args:
        input_dir: Input directory containing images
        output_dir: Output directory for processed images
        scale_factor: Scale factor for cropping (default: 0.8)
        position: Position to keep ('top-left', 'top-center', 'top-right',
                 'center-left', 'center-center', 'center-right',
                 'bottom-left', 'bottom-center', 'bottom-right')
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Validate position
    valid_positions = [
        'top-left', 'top-center', 'top-right',
        'center-left', 'center-center', 'center-right',
        'bottom-left', 'bottom-center', 'bottom-right'
    ]
    
    if position not in valid_positions:
        print(f"Error: Invalid position '{position}'. Valid options are: {', '.join(valid_positions)}")
        return
    
    # Supported image formats
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif')
    
    # Get all image files from input directory
    image_files = [f for f in os.listdir(input_dir) 
                  if f.lower().endswith(supported_formats)]
    
    if not image_files:
        print(f"No image files found in {input_dir}")
        return
    
    print(f"Found {len(image_files)} image files")
    print(f"Scale factor: {scale_factor}")
    print(f"Position: {position}")
    
    processed_count = 0
    
    for filename in image_files:
        try:
            # Open image
            input_path = os.path.join(input_dir, filename)
            with Image.open(input_path) as img:
                # Convert to RGB if necessary
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                original_width, original_height = img.size
                
                # Calculate crop dimensions maintaining aspect ratio
                crop_width = int(original_width * scale_factor)
                crop_height = int(original_height * scale_factor)
                
                # Calculate crop box based on position
                if position == 'top-left':
                    crop_box = (0, 0, crop_width, crop_height)
                elif position == 'top-center':
                    left = (original_width - crop_width) // 2
                    crop_box = (left, 0, left + crop_width, crop_height)
                elif position == 'top-right':
                    left = original_width - crop_width
                    crop_box = (left, 0, original_width, crop_height)
                elif position == 'center-left':
                    top = (original_height - crop_height) // 2
                    crop_box = (0, top, crop_width, top + crop_height)
                elif position == 'center-center':
                    left = (original_width - crop_width) // 2
                    top = (original_height - crop_height) // 2
                    crop_box = (left, top, left + crop_width, top + crop_height)
                elif position == 'center-right':
                    left = original_width - crop_width
                    top = (original_height - crop_height) // 2
                    crop_box = (left, top, original_width, top + crop_height)
                elif position == 'bottom-left':
                    top = original_height - crop_height
                    crop_box = (0, top, crop_width, original_height)
                elif position == 'bottom-center':
                    left = (original_width - crop_width) // 2
                    top = original_height - crop_height
                    crop_box = (left, top, left + crop_width, original_height)
                elif position == 'bottom-right':
                    left = original_width - crop_width
                    top = original_height - crop_height
                    crop_box = (left, top, original_width, original_height)
                
                # Crop the image
                cropped_img = img.crop(crop_box)
                
                # Resize back to original dimensions
                resized_img = cropped_img.resize((original_width, original_height), Image.LANCZOS)
                
                # Save processed image
                output_path = os.path.join(output_dir, filename)
                resized_img.save(output_path)
                
                processed_count += 1
                print(f"Processed: {filename} - Original: {original_width}x{original_height}")
                
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
    
    print(f"/nProcessing completed!")
    print(f"Successfully processed {processed_count} out of {len(image_files)} images")
    print(f"Output directory: {output_dir}")

def main():
    parser = argparse.ArgumentParser(description='Crop images to a specific position and resize back to original dimensions')
    parser.add_argument('input_dir', help='Input directory containing images')
    parser.add_argument('-o', '--output', default='processed_images', 
                       help='Output directory (default: processed_images)')
    parser.add_argument('-s', '--scale', type=float, default=0.8, 
                       help='Scale factor for cropping (default: 0.8)')
    parser.add_argument('-p', '--position', default='bottom-left', 
                       choices=['top-left', 'top-center', 'top-right',
                               'center-left', 'center-center', 'center-right',
                               'bottom-left', 'bottom-center', 'bottom-right'],
                       help='Position to keep (default: bottom-left)')
    
    args = parser.parse_args()
    
    crop_and_resize_images(args.input_dir, args.output, args.scale, args.position)

if __name__ == "__main__":
    # Example usage
    input_directory = "C:/Users/pengqh/Desktop/develop/25455306_frames_after/selected_frames/"  # Change to your input directory
    output_directory = input_directory+"scaled_frames"
    scale = 0.6
    position = "center-left"  # Options: top-left, top-center, top-right, center-left, center, center-right, bottom-left, bottom-center, bottom-right
    
    crop_and_resize_images(input_directory, output_directory, scale, position)