import json
from dotenv import load_dotenv
load_dotenv()
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



def extract_features(transcript):
    prompt = f"""
Extract structured information from this interview text.

Return ONLY valid JSON with exactly these keys:
mentions_kitchen, wants_storage, mentions_light, sentiment, summary

Rules:
- booleans must be true or false
- sentiment must be one of: positive, negative, neutral
- summary must be short

Interview text:
{transcript}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Return only valid JSON. No markdown, no explanations."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    content = response.choices[0].message.content.strip()
    print(json.loads(content))
    return json.loads(content)