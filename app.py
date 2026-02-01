from cv.frame_extractor import extract_frames
from cv.hand_analysis import analyze_frames
from audio.audio_analysis import analyze_audio
from llm.gpt_review import review_performance
from utils.video_utils import extract_audio
import os

VIDEO_PATH = "data/uploads/input_video.mp4"
AUDIO_PATH = "data/uploads/input_audio.wav"

def main():
    if not os.path.exists(AUDIO_PATH):
        extract_audio(VIDEO_PATH, AUDIO_PATH)

    frames = extract_frames(VIDEO_PATH)
    posture_issues = analyze_frames(frames)

    audio_issues = analyze_audio(AUDIO_PATH)

    feedback = review_performance(posture_issues, audio_issues)
    print("\n===== AI FEEDBACK =====\n")
    print(feedback)

if __name__ == "__main__":
    main()
