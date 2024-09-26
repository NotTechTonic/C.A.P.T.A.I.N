import pyttsx3
import emoji

engine = pyttsx3.init()
engine.setProperty('voice', 1)

def speak(text: str) -> None:
  """
    This function generates speech from text at lightning speed.

    Parameters:
    - query (str): The input text to which the model will respond in a string format.
   
    Returns:
    - None: nothing

    This function simply convertes text into speech offline really fast.
  """

  engine.say(emoji.replace_emoji(text, replace=''))
  engine.runAndWait()
