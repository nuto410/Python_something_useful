from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

# 加载视频
video = VideoFileClip("test.mp4")

# 加载浮水印图片并创建图像剪辑
watermark = ImageClip("1.png", duration=video.duration)
watermark = watermark.resize(height=50)  # 调整浮水印的大小

# 将浮水印剪辑叠加到视频上
video_with_watermark = CompositeVideoClip([video.set_duration(video.duration), watermark.set_duration(video.duration).set_position(("center", "bottom"))])

# 保存结果
video_with_watermark.write_videofile("output.mp4", codec="libx264")

# 关闭视频文件
video.close()
