import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands.Hands(static_image_mode=True)

def analyze_frames(frames):
    issues = set()

    for frame in frames:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = mp_hands.process(rgb)

        if not result.multi_hand_landmarks:
            issues.add("No visible hand gestures")
            continue

        for hand in result.multi_hand_landmarks:
            y_vals = [lm.y for lm in hand.landmark]
            avg_y = sum(y_vals) / len(y_vals)

            if avg_y > 0.75:
                issues.add("Hands too low")

            spread = abs(hand.landmark[8].x - hand.landmark[4].x)
            if spread > 0.15:
                issues.add("Over-dramatic finger spread")

    return list(issues)
