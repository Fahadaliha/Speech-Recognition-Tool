import speech_recognition as sr
from pydub import AudioSegment
import os
def transcribe_audio(mode='mic',file_path=None):
    recognizer = sr.Recognizer()

    try:
        if mode == "mic":
            with sr.Microphone() as source:
                print("Listening....")
                recognizer.adjust_for_ambient_noise(source)
                audio=recognizer.listen(source)
                print("Audio captured")
        elif mode == "file":
            if not file_path:
                return "Please provide valid audio file"
           
            with sr.AudioFile(file_path) as source:
                audio= recognizer.record(source)
        else:
            return"Invalid source"
        
        #for text translation we use googles API
        text= recognizer.recognize_google(audio)
        return f"Transcribed Text:{text}"
    except sr.UnknownValueError:
        return" Could not understand the audio "
    except sr.RequestError:
        return "Could not get service, check internet"
    except Exception as e:
        return f" Error:{str(e)}"