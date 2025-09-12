import os
try:
    from style import *
    import json  # json writing
    import requests  # web requests/packets
    import time
    import webbrowser  # to open links
    import sys
    from spellchecker import SpellChecker  # 99% of work for spelling checking
except ImportError as e:
    print(f"installing modules")
    os.system(r"pip install -r packages.txt")
    from style import *
    import json  # json writing
    import requests  # web requests/packets
    import time
    import sys
    import webbrowser  # to open links
    from spellchecker import SpellChecker  # 99% of work for spelling checking
import time  # To create delays for the 'Slow' function


# ASCII art with color applied using MainColor2
note = MainColor2(r"""                          
                                                                                                    
                                                                                                    
      █████████████████████████████████████████████████████████████████                             
   ████████████████████████████████████████████████████████████████████████                         
  ██████████████████████████████████████████████████████████████████████████                        
  ██████████████████████████████████████████████████████████████████████████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                        █████                                 ██████                        
  ██████                        █████                                 ██████                        
  ██████                        █████                                 ██████                        
  ██████                        █████                                 ██████                        
  ██████        ██████████████  ██████████████        ███████████     ██████                        
  ██████      ████████████████  ████████████████    █████████████     ██████                        
  ██████     ███████   ███████  ███████    ██████  ██████     ██      ██████                        
  ██████     █████       █████  ██████      █████  █████              ██████                        
  ██████     █████       █████  █████       █████ █████               ██████                  ███   
  ██████     █████       █████  █████       █████ ██████              ██████              █████████ 
  ██████     ██████    ███████  ███████    ██████  ██████     ██      ██████           ████████████ 
  ██████      ████████████████  ████████████████    █████████████     ██████         █████████████  
  ██████        ██████████████  ██████████████        ██████████      ██████       █████████████    
  ██████           ████                 ███              ████         ████       █████████████      
  ██████                                                              ██       █████████████        
  ██████                                                                     █████████████          
  ██████                                                                   ██████████████           
  ██████                                                                 ██████████████             
  ██████                                                                █████████████               
  ██████                                                              ██████████████                
  ██████                                                            ██████████████                  
  ██████                                                          ███████████████                   
  ██████                                    ███                  ███████████████                    
  ███████████████████████████████████     ███████████          ███████████████                      
  ███████████████████████████████████    ████████████████    ████████████████                       
   ██████████████████████████████████     ██████████████████████████████████                        
      ███████████████████████████████       ███████████████████████████████                         
                                              ████████████████████████████                          
                                                █████████████████████████                           
                                                 ███████████████████████                            
                                                   ███████████████████                              
                                                    ██████████████████                              
                                                     ████████████████                               
                                                      ██████████████                                
                                                        ███████████                                 
                                                         █████████                                  
                                                          ███████                                   
                                                           ██████                                   
                                                            ████                                    
                                                                                                                                                                                             
""")

# Function to check spelling and grammar
def check_spelling_grammar():
    Slow(note)  # Display ASCII art with slow text printing
    text = input(f"\n{yellow}Enter text to check: ")  # Ask user for input text
    spell = SpellChecker()  # Initialize the spell checker
    words = text.split()  # Split the input text into individual words
    misspelled = spell.unknown(words)  # Find the misspelled words

    if misspelled:
        print(f"\n🔍{lc} Spelling Suggestions:")
        for word in misspelled:
            correction = spell.correction(word)  # Get the best suggestion for each misspelled word
            print(f"{green}- {word} → {correction if correction else 'No suggestion'}")
    else:
        print(f"✅{green} No spelling errors found!")  # If no misspelled words are found

    # Call LanguageTool API for grammar checking
    api_url = "https://api.languagetool.org/v2/check"
    params = {"text": text, "language": "en-US"}
    response = requests.post(api_url, data=params)  # Send the text to LanguageTool API

    if response.status_code == 200:
        result = response.json()  # Get the result from the API
        if result["matches"]:
            print(f"\n📝{yellow} Grammar Suggestions:")
            for match in result["matches"]:
                print(f"- {match['message']}")  # Print grammar suggestions
        else:
            print(f"✅{green} No grammar errors found!")  # If no grammar issues are found
    else:
        print(f"⚠️{red} Error checking grammar!")  # If there's an error in the API request

# Run the function to check spelling and grammar
check_spelling_grammar()
