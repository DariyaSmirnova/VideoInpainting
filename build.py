# Сборка из 4 изображений
from moviepy.editor import VideoFileClip, clips_array, vfx
clip1 = VideoFileClip("steak.mp4")
clip2 = VideoFileClip("steak.mp4")
clip3 = VideoFileClip("steak.mp4")
clip4 = VideoFileClip("steak.mp4")
final_clip = clips_array([[clip1, clip2], [clip3, clip4]])
final_clip.resize(width = 480).write_videofile("dich.mp4")