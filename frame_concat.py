# from PIL import Image
# import os
# import argparse

# def create_horizontal_collage(input_dir, output_path, image_count=8):
#     """
#     Create a horizontal collage by arranging specified number of images side by side.
    
#     Args:
#         input_dir: Input directory containing images
#         output_path: Output path for the collage image
#         image_count: Number of images to include in the collage (default: 8)
#     """
#     # Get all image files from input directory
#     supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif')
#     image_files = [f for f in os.listdir(input_dir) 
#                   if f.lower().endswith(supported_formats)]
    
#     # Sort image files to ensure consistent ordering
#     image_files.sort()
    
#     if len(image_files) < image_count:
#         print(f"Warning: Only found {len(image_files)} images, but requested {image_count}")
#         image_count = len(image_files)
    
#     # Select the first 'image_count' images
#     selected_images = image_files[:image_count]
    
#     if not selected_images:
#         print("No images found to create collage")
#         return
    
#     print(f"Creating collage with {len(selected_images)} images:")
#     for img in selected_images:
#         print(f"  - {img}")
    
#     # Open all images and collect their dimensions
#     images = []
#     widths = []
#     heights = []
    
#     for filename in selected_images:
#         img_path = os.path.join(input_dir, filename)
#         img = Image.open(img_path)
#         images.append(img)
#         widths.append(img.width)
#         heights.append(img.height)
    
#     # Calculate total width and determine max height
#     total_width = sum(widths)
#     max_height = max(heights)
    
#     # Create a new blank image with the calculated dimensions
#     collage = Image.new('RGB', (total_width, max_height))
    
#     # Paste each image into the collage
#     x_offset = 0
#     for i, img in enumerate(images):
#         # If image height is less than max height, center it vertically
#         if img.height < max_height:
#             y_offset = (max_height - img.height) // 2
#             collage.paste(img, (x_offset, y_offset))
#         else:
#             collage.paste(img, (x_offset, 0))
        
#         x_offset += img.width
    
#     # Save the collage
#     collage.save(output_path)
#     print(f"Collage saved to: {output_path}")
#     print(f"Final dimensions: {total_width} x {max_height}")

# # def main():
# #     parser = argparse.ArgumentParser(description='Create a horizontal collage from images in a folder')
# #     parser.add_argument('input_dir', help='Input directory containing images')
# #     parser.add_argument('-o', '--output', default='collage.jpg', 
# #                        help='Output path for collage image (default: collage.jpg)')
# #     parser.add_argument('-n', '--number', type=int, default=8, 
# #                        help='Number of images to include in collage (default: 8)')
    
# #     args = parser.parse_args()
    
# #     create_horizontal_collage(args.input_dir, args.output, args.number)

# if __name__ == "__main__":
#     # Example usage
#     input_directory = "C:/Users/pengqh/Desktop/develop/25455306_frames_after/selected_frames/scaled_frames/"  # Change to your input directory
#     output_path = input_directory+"horizontal_collage.jpg"
#     number_of_images = 8
    
#     create_horizontal_collage(input_directory, output_path, number_of_images)


from PIL import Image
import os
import argparse

def create_collage(input_dir, output_path, direction='horizontal'):
    """
    Create a collage by arranging all images from a folder either horizontally or vertically.
    
    Args:
        input_dir: Input directory containing images
        output_path: Output path for the collage image
        direction: Arrangement direction - 'horizontal' or 'vertical' (default: 'horizontal')
    """
    # Get all image files from input directory
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif')
    image_files = [f for f in os.listdir(input_dir) 
                  if f.lower().endswith(supported_formats)]
    
    # Sort image files to ensure consistent ordering
    image_files.sort()
    
    if not image_files:
        print("No images found to create collage")
        return
    
    print(f"Creating {direction} collage with {len(image_files)} images:")
    for img in image_files:
        print(f"  - {img}")
    
    # Open all images and collect their dimensions
    images = []
    widths = []
    heights = []
    
    for filename in image_files:
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path)
        images.append(img)
        widths.append(img.width)
        heights.append(img.height)
    
    if direction == 'horizontal':
        # Calculate total width and determine max height
        total_width = sum(widths)
        max_height = max(heights)
        
        # Create a new blank image with the calculated dimensions
        collage = Image.new('RGB', (total_width, max_height))
        
        # Paste each image into the collage
        x_offset = 0
        for i, img in enumerate(images):
            # If image height is less than max height, center it vertically
            if img.height < max_height:
                y_offset = (max_height - img.height) // 2
                collage.paste(img, (x_offset, y_offset))
            else:
                collage.paste(img, (x_offset, 0))
            
            x_offset += img.width
            
    else:  # vertical direction
        # Calculate total height and determine max width
        total_height = sum(heights)
        max_width = max(widths)
        
        # Create a new blank image with the calculated dimensions
        collage = Image.new('RGB', (max_width, total_height))
        
        # Paste each image into the collage
        y_offset = 0
        for i, img in enumerate(images):
            # If image width is less than max width, center it horizontally
            if img.width < max_width:
                x_offset = (max_width - img.width) // 2
                collage.paste(img, (x_offset, y_offset))
            else:
                collage.paste(img, (0, y_offset))
            
            y_offset += img.height
    
    # Save the collage
    collage.save(output_path)
    print(f"Collage saved to: {output_path}")
    
    if direction == 'horizontal':
        print(f"Final dimensions: {collage.width} x {collage.height}")
    else:
        print(f"Final dimensions: {collage.width} x {collage.height}")

def main():
    parser = argparse.ArgumentParser(description='Create a horizontal or vertical collage from all images in a folder')
    parser.add_argument('input_dir', help='Input directory containing images')
    parser.add_argument('-o', '--output', default='collage.jpg', 
                       help='Output path for collage image (default: collage.jpg)')
    parser.add_argument('-d', '--direction', choices=['horizontal', 'vertical'], default='horizontal',
                       help='Arrangement direction (default: horizontal)')
    
    args = parser.parse_args()
    
    create_collage(args.input_dir, args.output, args.direction)

if __name__ == "__main__":
    # Example usage
    input_directory = "input_images"  # Change to your input directory
    output_path = "collage.jpg"
    direction = "horizontal"  # Options: 'horizontal' or 'vertical'
    
    create_collage(input_directory, output_path, direction)