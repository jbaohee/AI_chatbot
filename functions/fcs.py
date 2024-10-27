from pydub import AudioSegment

# function to convert audio file in proper format for google speech
def flac_conversion(audio_file, audio_path):
    
    # reading the audio file 
    audio_flac = AudioSegment.from_mp3(audio_file)

    # setting in mono channel with 16 kHz sampling rate
    audio_flac = audio_flac.set_channels(1)
    audio_flac = audio_flac.set_frame_rate(16000)

    # saving the audio in desired format 
    audio_flac.export(audio_path + "input_query.flac", format="flac")