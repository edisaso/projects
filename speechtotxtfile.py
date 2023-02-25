import speech_recognition as sr

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