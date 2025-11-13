from frame_concat import *
from frame_cutting import *
from frame_dealing import *
from frame_scaling import *
from frame_selecting import *

def video2Image(video_path,original_frame_dir,selected_frame_dir,scaled_frame_dir,output_path,fps, total_frame_num,franka,scaling_direction,scaling_factor):
    video_to_frames(video_path=video_path, output_dir=original_frame_dir, fps=fps)
    select_uniform_frames(original_frame_dir, selected_frame_dir, num_frames=total_frame_num)
    if franka:
        process_images(selected_frame_dir, selected_frame_dir)
    crop_and_resize_images(selected_frame_dir, scaled_frame_dir, scale_factor=scaling_factor, position=scaling_direction)
    #if you want to repeat the crop and resize, change the scaling direction and scaling factor and reuse the line below.
    # crop_and_resize_images(scaled_frame_dir, scaled_frame_dir, scale_factor=scaling_factor, position=scaling_direction)

    create_collage(scaled_frame_dir, output_path, direction='horizontal') 

if __name__ == "__main__":
    fps=6
    # video_path="C:/Users/pengqh/Downloads/Archive/MP4/25455306.mp4"
    # video_path="C:/Users/pengqh/Downloads/Archive/MP4/14436910.mp4"
    # video_path="C:/Users/pengqh/Downloads/Archive/Sat_Sep_27_12_17_14_2025/recordings/MP4/25455306.mp4"
    # video_path="C:/Users/pengqh/Downloads/Archive/Sat_Nov__1_18_30_57_2025/recordings/MP4/26368109.mp4"
    # video_path="C:/Users/pengqh/Downloads/Archive/Sat_Nov__1_18_30_57_2025/recordings/MP4/14436910.mp4"
    # video_path="C:/Users/pengqh/Downloads/Archive/pineapple/15512737.mp4"
    # video_path="C:/Users/pengqh/Downloads/Archive/pineapple/27085680.mp4"
    video_path="C:/Users/pengqh/Downloads/Archive/pineapple/26368109.mp4"
    # video_path=""
    # original_frame_dir=""
    original_frame_dir=video_path.replace(".mp4",'')+"/original_frame_dir/"
    # selected_frame_dir=""
    selected_frame_dir=video_path.replace(".mp4",'')+"/selected_frame_dir/"
    scaled_frame_dir=video_path.replace(".mp4",'')+"/scaled_frame_dir/"
    output_path=video_path.replace(".mp4",".jpg")
    scaling_factor=0.6
    # scaling_direction="top-right"
    scaling_direction="bottom-center"

    franka=True
    total_frame_num=8
    video2Image(video_path,original_frame_dir,selected_frame_dir,scaled_frame_dir,output_path,fps, total_frame_num,franka,scaling_direction,scaling_factor)

