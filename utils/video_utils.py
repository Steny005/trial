from moviepy.editor import VideoFileClip

def extract_audio(video_path, output_audio):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(output_audio)
