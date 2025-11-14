from frame_concat import *
from frame_cutting import *
from frame_dealing import *
from frame_scaling import *
from frame_selecting import *

def video2Image(video_path,original_frame_dir,selected_frame_dir,scaled_frame_dir,output_path,fps, total_frame_num,crop_info,rotation_angle,scaling_direction,scaling_factor):
    video_to_frames(video_path=video_path, output_dir=original_frame_dir, fps=fps)
    select_uniform_frames(original_frame_dir, selected_frame_dir, num_frames=total_frame_num)
    process_images(selected_frame_dir, selected_frame_dir, splits_config=crop_info, rotation_angle=rotation_angle)
    crop_and_resize_images(selected_frame_dir, scaled_frame_dir, scale_factor=scaling_factor, position=scaling_direction)
    #if you want to repeat the crop and resize, change the scaling direction and scaling factor and reuse the line below.
    # crop_and_resize_images(scaled_frame_dir, scaled_frame_dir, scale_factor=scaling_factor, position=scaling_direction)
    crop_and_resize_images(scaled_frame_dir, scaled_frame_dir, scale_factor=0.93, position='center-center')


    create_collage(scaled_frame_dir, output_path, direction='horizontal') 

if __name__ == "__main__":
    fps=1
    video_path="C:/Users/pengqh/Downloads/task2.mov"
    last_str='.mov'
    original_frame_dir=video_path.replace(last_str,'')+"/original_frame_dir/"
    selected_frame_dir=video_path.replace(last_str,'')+"/selected_frame_dir/"
    scaled_frame_dir=video_path.replace(last_str,'')+"/scaled_frame_dir/"
    output_path=video_path.replace(last_str,".jpg")
    crop_info=((3,3),(2,1))
    rotation_angle=0
    scaling_factor=0.95
    # scaling_factor=0.3
    # scaling_direction="bottom-center"
    # scaling_direction="top-right"
    # scaling_direction='center-center'
    scaling_direction='top-left'

    total_frame_num=8
    video2Image(video_path,original_frame_dir,selected_frame_dir,scaled_frame_dir,output_path,fps, total_frame_num,crop_info,rotation_angle,scaling_direction,scaling_factor)

