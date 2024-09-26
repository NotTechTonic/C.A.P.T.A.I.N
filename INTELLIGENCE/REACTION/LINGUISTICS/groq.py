from groq import Groq
import os
from dotenv import load_dotenv; load_dotenv()

def generate_response(query: str, system_prompt: str = "You are a humorous AI, use emojis and sarcasm in your responses.") -> object:
  """
    Generates a response from the groq-llama3-70b-8192 model based on the given query.

    Parameters:
    - query (str): The input text to which the model will respond in a string format.
    - system_prompt (str, optional): The system prompt to use for the model. Defaults to "You are a humorous AI, use emojis and sarcasm in your responses.".    
   
    Returns:
    - object: response object

    This function initializes a session with the Groq client,
    and creates a chat completion with the model and user's prompt along with the system prompt. Returns the response object at last.
  """
  
  groq_client = Groq(api_key=os.environ.get('GROQ_AI'))

  response = groq_client.chat.completions.create(
    model='llama3-70b-8192',
    messages=[
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": query}
    ],
    stream=True
  )

  return response
