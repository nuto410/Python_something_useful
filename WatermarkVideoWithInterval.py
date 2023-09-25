from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

# 加载视频
video = VideoFileClip("test.mp4")

# 设置每隔3秒显示1秒浮水印的时间段
interval_duration = 3  # 每隔多少秒显示一次浮水印
watermark_duration = 1  # 浮水印显示的持续时间
video_duration = video.duration
clips = []

for start_time in range(0, int(video_duration), interval_duration):
    # 加载浮水印图片并创建图像剪辑
    watermark = ImageClip("1.png")
    watermark = watermark.resize(height=50)  # 调整浮水印的大小
    clip = watermark.set_start(start_time)
    clip = clip.set_position(("center", "bottom")).set_duration(watermark_duration)
    clips.append(clip)

# 将所有剪辑拼接起来
final_video = CompositeVideoClip([video] + clips)

# 设置 final_video 的总持续时间
final_video = final_video.set_duration(video_duration)

final_video.write_videofile("output.mp4")
