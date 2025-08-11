meetvision-ai/
├── app.py                      # Streamlit UI to upload audio + screenshots
├── agent/
│   └── meet_agent.py           # Orchestrates transcription, OCR, and merging
├── utils/
│   ├── speech_to_text.py       # Converts meeting audio to text
│   ├── screen_ocr.py           # Extracts text from screenshots/slides
│   ├── meeting_merger.py       # Combines transcript + screen content
│   └── summarizer.py           # Summarizes and formats meeting notes
├── samples/
│   ├── meeting_audio.mp3       # Example meeting recording
│   └── screen1.png             # Example shared screen capture
└── requirements.txt
