def merge_meeting_data(transcript: str, screen_texts: list[str]) -> str:
    screen_notes = "\n\n".join([f"Screen {i+1}: {txt}" for i, txt in enumerate(screen_texts)])
    merged = f"--- MEETING TRANSCRIPT ---\n{transcript}\n\n--- SCREEN NOTES ---\n{screen_notes}"
    return merged
