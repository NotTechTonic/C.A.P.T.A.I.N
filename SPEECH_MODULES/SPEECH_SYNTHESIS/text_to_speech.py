import pyttsx3
import emoji

engine = pyttsx3.init()
engine.setProperty('voice', 1)

def speak(text: str) -> None:
  engine.say(emoji.replace_emoji(text, replace=''))
  engine.runAndWait()
