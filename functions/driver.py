# import os
# import time
# from functions import aqs, fcs, gstt, recorder, wp

# # Setting necessary path for recordings 
# current_directory = os.getcwd()
# audio_path = current_directory+ "/recordings/"

# # calling the recorder function to record audio for 4 seconds
# recorder.record(current_directory, 4)

# # defining the path to recoreded audio
# audio_file = audio_path + "input_query.mp3"

# # # Start measuring time
# # start_time = time.time() #in seconds
# # start_time_clocks = time.process_time() #in cpu clocks
# choice = input("Enter a for google, b for Whisper: ")

# if input == 'a':

#     print("--Using google speech to text--")
#     # converting to flac 
#     fcs.flac_conversion(audio_file, audio_path)
#     audio_file = audio_path + "input_query.flac"

#     # getting text from speech (the question)
#     transcript = gstt.transcribe_audio(audio_file)

# if input == 'b':
#     print("--Using whisper--")
#     # getting text from speech (the question)
#     transcript = wp.transcribe_audio(current_directory, "tiny")
#     os.remove(current_directory + "/recordings/input_query.mp3")


# print("Your Question: " + transcript)


# # elapsed_time_seconds = time.time() - start_time
# # elapsed_time_clocks = time.process_time() - start_time_clocks

# # getting answer from ai 
# ai_answer = aqs.ai_query(transcript)
# print(ai_answer)


# # print("\nExecution time in seconds:", elapsed_time_seconds)
# # print("\nExecution time in CPU clocks:", elapsed_time_clocks)