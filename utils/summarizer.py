import openai

def summarize_meeting(merged_text: str) -> dict:
    prompt = f"""
    You are an AI assistant. Summarize the meeting into:
    1. Key points
    2. Decisions
    3. Action items

    Meeting Content:
    {merged_text}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"summary": response.choices[0].message["content"]}
