from openai import OpenAI

client = OpenAI()

def review_performance(posture_issues, audio_issues):
    prompt = f"""
You are a professional public speaking coach.

Posture issues:
{posture_issues}

Audio analysis:
{audio_issues}

For each:
- What’s wrong
- Why it’s bad
- How to fix it
"""

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return res.choices[0].message.content
