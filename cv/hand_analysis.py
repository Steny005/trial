import cv2

def analyze_frames(frames):
    """
    Simple fallback posture analyzer.
    This version just checks if frames are not empty
    and returns simple posture issues.
    """
    issues = set()

    if not frames:
        issues.add("No frames detected")
        return list(issues)

    # We take the first frame as a simple test
    first = frames[0]
    height, width = first.shape[:2]

    # If more than half the image is dark, maybe posture low
    gray = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
    avg_brightness = gray.mean()

    if avg_brightness < 80:
        issues.add("Frame too dark - possible camera angle problem")

    issues.add("Posture detection skipped (fallback)")

    return list(issues)
