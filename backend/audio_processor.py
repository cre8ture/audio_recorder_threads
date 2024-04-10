import asyncio
import threading
import sounddevice as sd
import numpy as np
import speech_recognition as sr
from scipy.io.wavfile import write
import tempfile
import os
from tempfile import mkstemp

# Function to capture audio, modified to use sounddevice for actual audio capture
def capture_audio(duration=5, fs=44100):
    print("Capturing audio...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()  # Wait for the recording to finish
    return recording, fs
def transcribe_audio(recording, fs):
    recognizer = sr.Recognizer()
    fd, tmp_filename = mkstemp(suffix=".wav")
    os.close(fd)

    try:
        write(tmp_filename, fs, recording)  # Save the recording to a temporary file.
        with sr.AudioFile(tmp_filename) as source:
            audio_data = recognizer.record(source)
            # Use Sphinx for offline speech recognition
            text = recognizer.recognize_sphinx(audio_data)
            print("Transcription: ", text)
            return text
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Sphinx; {e}")
    finally:
        os.remove(tmp_filename)  # Clean up the temporary file.

async def audio_processing_loop(websocket):
    while True:
        try:
            print("audio listening")
            recording, fs = capture_audio(duration=5)
            print("recording, fs" , recording, fs)
            transcription = transcribe_audio(recording, fs)
            print("trascription", transcription)
            if transcription:
                await websocket.send_text(transcription)
        except Exception as e:
            print(f"An error occurred: {e}")
            # Optionally, break the loop or continue based on the type of error
            break  # or `continue` to skip to the next iteration


# Function to start the audio processing in a new thread with its own asyncio event loop
def start_audio_processing_thread(websocket):
    print("Starting audio processing thread...")
    def run_loop():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(audio_processing_loop(websocket))
        loop.close()
    thread = threading.Thread(target=run_loop)
    thread.start()
