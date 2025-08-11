from utils.speech_to_text import transcribe_audio
from utils.screen_ocr import extract_screen_text
from utils.meeting_merger import merge_meeting_data
from utils.summarizer import summarize_meeting

def process_meeting(audio_file: str, screen_files: list[str]):
    transcript = transcribe_audio(audio_file)
    screen_texts = [extract_screen_text(img) for img in screen_files]
    merged = merge_meeting_data(transcript, screen_texts)
    summary = summarize_meeting(merged)
    return transcript, merged, summary
