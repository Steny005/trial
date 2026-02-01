import librosa

def analyze_audio(audio_path):
    y, sr = librosa.load(audio_path)

    rms = librosa.feature.rms(y=y)[0]
    avg_volume = float(rms.mean())
    silence_frames = rms < 0.01
    silence_ratio = float(silence_frames.sum() / len(rms))

    return {
        "average_volume": round(avg_volume, 3),
        "silence_ratio": round(silence_ratio, 3)
    }
