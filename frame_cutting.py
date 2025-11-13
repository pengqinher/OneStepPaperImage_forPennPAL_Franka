import cv2
import os
import argparse

def video_to_frames(video_path, output_dir, fps=6):
    """
    Extract frames from video at specified frame rate
    
    Args:
        video_path: path to video file
        output_dir: output directory for frames
        fps: target frame rate (default: 6fps)
    """
    # Create output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Open video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Cannot open video file {video_path}")
        return
    
    # Get video information
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / original_fps
    
    print(f"Video Info:")
    print(f"  Original FPS: {original_fps:.2f}")
    print(f"  Total frames: {total_frames}")
    print(f"  Duration: {duration:.2f} seconds")
    print(f"  Target FPS: {fps}")
    
    # Calculate frame interval
    frame_interval = int(original_fps / fps)
    
    frame_count = 0
    saved_count = 0
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Save frame at specified interval
        if frame_count % frame_interval == 0:
            # Generate output filename
            output_filename = f"frame_{saved_count:06d}.jpg"
            output_path = os.path.join(output_dir, output_filename)
            
            # Save frame
            cv2.imwrite(output_path, frame)
            saved_count += 1
            
            if saved_count % 50 == 0:
                print(f"Saved {saved_count} frames...")
        
        frame_count += 1
    
    # Release resources
    cap.release()
    
    print(f"\nConversion completed!")
    print(f"Total frames saved: {saved_count}")
    print(f"Output directory: {output_dir}")

# # if __name__ == "__main__":
# #     parser = argparse.ArgumentParser(description='Extract frames from video at 6fps')
# #     parser.add_argument('video_path', default='C:/Users/pengqh/Downloads/Archive/MP4/25455306.mp4')
# #     parser.add_argument('-o', '--output', default='./', 
# #                        help='Output directory (default: output_frames)')
# #     parser.add_argument('--fps', type=int, default=6, 
# #                        help='Target frame rate (default: 6)')
    
# #     args = parser.parse_args()
    
#     video_to_frames(args.video_path, args.output, args.fps)

if __name__ == "__main__":
    # Example usage
    video_path = "C:/Users/pengqh/Downloads/Archive/MP4/25455306.mp4"
    output_dir = "./"
    fps = 6
    
    video_to_frames(video_path, output_dir, fps)