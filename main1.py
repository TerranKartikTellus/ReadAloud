import win32com.client as wincl
import os


def text_to_speech(text_file):
    print("ReadAloud")
    with open(text_file, 'r') as f:
        text = f.read()

    # Initialize the speech synthesizer
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Rate = 4
    voices = speak.GetVoices()
    for voice in voices:
        print(voice.GetDescription())
    speak.Voice = voices.Item(1)
    speak.Speak(text)


text_to_speech("text.txt")


# https://github.com/TerranKartikTellus
