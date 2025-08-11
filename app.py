import streamlit as st
from agent.meet_agent import process_meeting

st.title("MeetVision AI – Meeting Reconstruction Agent")

audio_file = st.file_uploader("Upload Meeting Audio", type=["mp3", "wav"])
screen_files = st.file_uploader("Upload Shared Screen Captures", type=["png", "jpg"], accept_multiple_files=True)

if st.button("Process Meeting") and audio_file:
    with open("temp_audio.mp3", "wb") as f:
        f.write(audio_file.getbuffer())

    screen_paths = []
    for file in screen_files:
        path = f"temp_{file.name}"
        with open(path, "wb") as f:
            f.write(file.getbuffer())
        screen_paths.append(path)

    transcript, merged, summary = process_meeting("temp_audio.mp3", screen_paths)

    st.subheader("Full Transcript")
    st.write(transcript)

    st.subheader("Merged Meeting Data")
    st.write(merged)

    st.subheader("Summary")
    st.write(summary["summary"])
