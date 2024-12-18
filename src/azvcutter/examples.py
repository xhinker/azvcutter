#%%
%%time
from azvcutter_lib import merge_videos

video_files = [
    "/home/andrewzhu/storage_14t_5/record_videos/tryout_lama/2024-11-30 10-06-27.mp4"
    , "/home/andrewzhu/storage_14t_5/record_videos/tryout_lama/2024-11-30 10-23-26.mp4"
]

# output_file = "/home/andrewzhu/storage_14t_5/record_videos/tryout_lama/tryout_lama_8mbr_p3.mp4"

output_file = "/home/andrewzhu/storage_14t_5/record_videos/tryout_lama/tryout_lama_concat.mp4"
merge_videos(
    video_files     = video_files
    , output_file   = output_file
    , concate_only  = True
)