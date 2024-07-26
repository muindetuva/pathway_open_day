import speech_recognition as sr
import webbrowser
import urllib.parse
import urllib.request
import re
import os
from gtts import gTTS


def speak(audio):
    tts = gTTS(text=audio, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")  # Make sure you have mpg321 installed or use another player


def take_command():
    # Implementation to take audio input and return as text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        speak("Sorry, I didn't catch that. Please repeat.")
        return None
    return query

def search_youtube(query):
    speak("Searching YouTube...")
    query_string = urllib.parse.urlencode({"search_query": query})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'watch\?v=(.{11})', html_content.read().decode())
    if search_results:
        # Open the first search result video
        webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
        speak("Here is what I found for " + query + " on YouTube.")
    else:
        speak("I couldn't find any videos for " + query)

if __name__ == '__main__':
    speak("Hello! What video would you like to watch on YouTube?")
    while True:
        command = take_command().lower()
        print(f"Command: {command}")
        if 'youtube' in command:
            command = command.replace('youtube', '').strip()
            print(command)
            search_youtube(command)
        elif 'stop' in command:
            speak("Goodbye!")
            break

