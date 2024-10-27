import pyaudio
import wave
from pydub import AudioSegment
import os

def record(current_directory, rs):

    # Parameter list for recordings
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = rs
    WAV_OUTPUT = current_directory + "/recordings/input_query.wav"
    MP3_OUTPUT = current_directory + "/recordings/input_query.mp3"

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # printing to see what input recording device is being used
    default_input_device_index = audio.get_default_input_device_info()['index']
    input_device_index = audio.get_device_info_by_index(default_input_device_index)['index']
    print("Input device: ", audio.get_device_info_by_index(input_device_index)['name'])

    # Opening stream
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []

    # Recording audio for the specified duration
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    # Closing the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Saving the recorded audio to a WAV file
    with wave.open(WAV_OUTPUT, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))


    # Converting WAV to MP3
    audio = AudioSegment.from_wav(WAV_OUTPUT)
    audio.export(MP3_OUTPUT, format="mp3")

    os.remove(current_directory + "/recordings/input_query.wav")
    print("Audio saved as:", " input_query.mp3")
