import os
from google.cloud import speech_v1p1beta1 as speech

# function to transcribe audio 
def transcribe_audio(audio_file):

    # path to google ADC key json file as an environment variable  
    current_directory = os.getcwd()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = current_directory+"/api_keys/google_speech_to_text_key.json"

    # creating a client object of Speech-to-text
    client = speech.SpeechClient()

    # opening the converted flac audio 
    with open(audio_file, 'rb') as audio_flac:
        content = audio_flac.read()

    # creating an audio recongnition object
    audio = speech.RecognitionAudio(content=content)

    # setting up the configuration parameters for the audio to be recognized
    config = speech.RecognitionConfig(
        # specifying flac encoding, mono channel, sampling frequency and language code 
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,  
        sample_rate_hertz=16000,  
        audio_channel_count=1,
        language_code='en-US',
        # language_code='fr-FR',
    )

    # performing the speech recognition. For this part, internet connection is mandatory
    response = client.recognize(config=config, audio=audio)
    
    # removing the flac file to declutter
    os.remove(audio_file)

    # The whole result contains a lot of information, some metadata. Only getting the transcripted text
    for transcript in response.results:
        transcripted_text = transcript.alternatives[0].transcript

    return transcripted_text