import speech_recognition as sr
import pyttsx3
# initialize the recognizer
r = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something...")
    # listen for audio and store it in audio_data variable
    audio_data = r.record(source, duration=5)

    # recognize speech using Google Speech Recognition
    text = r.recognize_google(audio_data)

# print the text
print(text)

# save the text to a file
with open("speech.txt", "w") as f:
    f.write(text)


    # initialize the text-to-speech engine
engine = pyttsx3.init()

# open the text file and read its contents
with open("speech.txt", "r") as file:
    content = file.read()

# set the rate and volume of the speech
engine.setProperty("rate", 150)
engine.setProperty("volume", 1)

# convert the text to speech
engine.say(content)
engine.runAndWait()