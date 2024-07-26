import speech_recognition as sr
import wikipedia
import webbrowser
import os
from gtts import gTTS
import urllib.parse
import urllib.request
import re

def speak(audio):
    tts = gTTS(text=audio, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: " + query + "\n")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        speak("Sorry, I didn't catch that.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("There was an error connecting to the service.")
        return None
    return query

def search_youtube(query):
    speak("Searching YouTube...")
    query_string = urllib.parse.urlencode({"search_query": query})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'watch\?v=(.{11})', html_content.read().decode())
    if search_results:
        webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
        speak("Here is what I found for " + query + " on YouTube.")
    else:
        speak("I couldn't find any videos for " + query)

if __name__ == '__main__':
    speak("Welcome to the ALX Open Day.")
    speak("Alexa Mwitu Here. How can I help you?")
    while True:
        query = take_command()
        if query is not None:
            query = query.lower()
            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "").strip()
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            elif 'youtube' in query:
                speak("What would you like to search for on YouTube?")
                video_query = take_command()
                if video_query:
                    search_youtube(video_query)
            elif 'open youtube' in query:
                speak("Opening YouTube")
                webbrowser.open("https://youtube.com")
            elif 'open google' in query:
                speak("Opening Google")
                webbrowser.open("https://google.com")
            elif 'sleep' in query:
                speak("Shutting down, goodbye!")
                break
            # Add more commands as needed
        else:
            speak("Please say something.")

