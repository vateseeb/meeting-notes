import os
from pydub import AudioSegment
import openai

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

# Function to transcribe an audio file using OpenAI
def transcribe_audio(file_path):
    # Load the audio file using PyDub
    song = AudioSegment.from_file(file_path)

    # Define the duration of each audio chunk in milliseconds
    chunk_duration = 10 * 60 * 1000

    # Split the audio file into chunks
    chunks = []
    for i in range(0, len(song), chunk_duration):
        chunk = song[i : i + chunk_duration]
        chunk.export(f"chunk_{i}.mp3", format="mp3")
        chunks.append(f"chunk_{i}.mp3")

    print(f"Split {file_path} into {len(chunks)} chunks")

    # Transcribe each audio chunk using OpenAI
    transcriptions = []
    for chunk_file in chunks:
        with open(chunk_file, "rb") as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
            transcriptions.append(transcript["text"])
        
        print(f"Transcribed chunk into {transcript}")

    # Clean up temporary audio chunk files
    for chunk_file in chunks:
        os.remove(chunk_file)

    return transcriptions

# Example usage
file_path = "./notes.m4a"
transcriptions = transcribe_audio(file_path)
for i, transcription in enumerate(transcriptions):
    # write to one file
    with open("transcript.txt", "a") as f:
        f.write(transcription)
