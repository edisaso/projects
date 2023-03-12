import speech_recognition as sr
from googletrans import Translator
import pyttsx3
import tkinter as tk

translator = Translator()

def translate_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        spoken_text.set("Listening...")
        translated_text.set("")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='bg-BG')
        spoken_text.set(f"You said: {text}")
        translated = translator.translate(text, src='bg', dest='en').text
        translated_text.set(f"Translation: {translated}")
        engine = pyttsx3.init()
        engine.say(translated)
        engine.runAndWait()
    except sr.UnknownValueError:
        spoken_text.set("Sorry, I didn't catch that.")
    except sr.RequestError:
        spoken_text.set("Sorry, my speech service is down.")

def on_submit():
    translate_audio()

root = tk.Tk()
root.title("Bulgarian Audio Translator into English")

spoken_text = tk.StringVar()
translated_text = tk.StringVar()

spoken_label = tk.Label(root, textvariable=spoken_text)
translated_label = tk.Label(root, textvariable=translated_text)
submit_button = tk.Button(root, text="Start Translation", command=on_submit)

spoken_label.pack()
translated_label.pack()
submit_button.pack()

root.mainloop()
