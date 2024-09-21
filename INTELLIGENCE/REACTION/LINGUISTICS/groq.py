from groq import Groq
import os
from dotenv import load_dotenv; load_dotenv()

def generate_response(query: str, system_prompt: str = "You are a humorous AI, use emojis and sarcasm in your responses.") -> object:
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
