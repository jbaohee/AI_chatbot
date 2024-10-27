import os
from functions import aqs, fcs, gstt, recorder, wp

# Setting necessary path for recordings 
current_directory = os.getcwd()
audio_path = current_directory+ "/recordings/"

# calling the recorder function to record audio for 5 seconds
print("###################   AI TUTOR   ###################")
print("--Press A to ask question\n--Press Q to exit")


while (True):
    master_choice = input("Enter choice : ")

    if master_choice == 'a':
        # second parameter is how long I want to record in seconds
        recorder.record(current_directory, 6)

        # defining the path to recoreded audio
        audio_file = audio_path + "input_query.mp3"

        # prompting for transcription model to be used
        choice = input("Enter 1 for google, 2 for Whisper: ")

        if choice == '1' :
            print("--Using google speech to text--")
            # converting to flac 
            fcs.flac_conversion(audio_file, audio_path)
            audio_file = audio_path + "input_query.flac"

            # getting text from speech (the question)
            transcript = gstt.transcribe_audio(audio_file)

        elif choice == '2' :
            print("--Using whisper--")
            transcript = wp.transcribe_audio(current_directory, "base")

        else:
            print("Invalid choice. Terminated")

        print("Your Question: " + transcript)

        os.remove(current_directory + "/recordings/input_query.mp3")
        # calling groq with the transcription
        ai_answer = aqs.ai_query(transcript)

        print(ai_answer)
        print("\n\n")
    
    elif master_choice == 'q':
        break

    else:
        print("Invalid choice\n--Press A to ask question\n--Press Q to exit ")
