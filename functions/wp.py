import whisper 
import os 

def transcribe_audio(current_directory, whisper_model):
    model = whisper.load_model(whisper_model)

    current_directory = os.getcwd()
    result = model.transcribe(current_directory + "/recordings/input_query.mp3", fp16= True)
    # print(result["text"])

    return result["text"]