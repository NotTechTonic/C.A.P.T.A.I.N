# _   _       _  _____         _   _____           _      
#| \ | | ___ | ||_   _|__  ___| |_|_   _|__  _ __ (_) ___ 
#|  \| |/ _ \| __|| |/ _ \/ __| '_ \| |/ _ \| '_ \| |/ __|
#| |\  | (_) | |_ | |  __/ (__| | | | | (_) | | | | | (__ 
#|_| \_|\___/ \__||_|\___|\___|_| |_|_|\___/|_| |_|_|\___|

#  Made With 💗 By - Satyam ( NotTechTonic )
#  YouTube Channel: https://www.youtube.com/@nottechtonic

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

      - Website: https://nottechtonic.pythonanywhere.com/
      - Github: https://github.com/NotTechTonic
      - ReplIt: https://replit.com/@satyapro945

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#  ------------------------------------------------------------------------------
#  Dive into the world of coding with NotTechTonic
#  Make sure to hit that Subscribe button to stay tuned for exciting content!

#  Happy coding!
#  ----------------------------------------------------------------------------


from imports import *

def _output(response) -> Generator[str, None, None]:

  """
    This function iterates over the response to get the chunks and prints them

    Parameters:
    - response (object): Takes a Response object.
   
    Returns:
    - Generator(str, None, None): returns a generator object that can be iterated.

    This function takes a response object and iterate over it to get and print the chunks while yielding partial sentences that the Generator will return per Iteration. 
  """

  print(f"\033[1;94mC.A.P.T.A.I.N >> \033[0m", end='', flush=True)
  partial_sentence = ""
  
  for chunk in response:
    if chunk.choices[0].delta.content:
      word = chunk.choices[0].delta.content
      print(word, end='', flush=True)
      partial_sentence += word

    sentences = re.split(r'(?<!\b\w\.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', partial_sentence)
    
    for complete_sentence in sentences[:-1]:
      yield complete_sentence.strip()
      
    partial_sentence = sentences[-1]

if __name__ == "__main__":
  print("-","".join(captain_text),"by \033[35m@NotTechTonic(\033[32mSatyam\033[35m)\033[0m")

  while (user_input := input("\n\n\033[1;92mYou >> \033[0;33m")) != "Bye":
    for sentence in _output(groq.generate_response(user_input, system_prompt=CAPTAIN_INSTRUCTIONS)):
      speak(sentence)
