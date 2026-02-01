from openai import OpenAI

client = OpenAI()

def review_performance(posture_issues, audio_issues):
    prompt = f"""
You are a professional public speaking coach.

Posture issues:
{posture_issues}

Audio analysis:
{audio_issues}

For each problem:
1. Explain why it is bad
2. Explain how to fix it clearly
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content
