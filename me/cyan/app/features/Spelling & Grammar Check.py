import requests  # For making HTTP requests to the LanguageTool API
from spellchecker import SpellChecker  # 99% of work for spelling checking
from colors_app import *  # Assuming this is a custom module for color constants (e.g., yellow, green)
import time  # To create delays for the 'Slow' function


# Function to print the text slowly, line by line with a delay
def Slow(text, delay=0.03):
    for line in text.split("\n"):  # Split the input text into lines
        print(line, flush=True)  # Print each line
        time.sleep(delay)  # Delay between each line for slow printing


# Function to apply color to the text gradually
def MainColor2(text):
    start_color = (0, 200, 150)  # Starting RGB color for the text
    end_color = (0, 255, 255)  # Ending RGB color for the text

    num_steps = 16  # Number of steps for the color gradient
    # Generate a gradient of colors between the start and end color
    colors = [
        (
            start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1),
            start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1),
            start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1),
        )
        for i in range(num_steps)
    ]

    colors += list(reversed(colors[:-1]))  # Reverse the gradient for a fading effect

    # Function to format text with color codes
    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"  # ANSI escape code for 24-bit color

    result = []  # List to store the colored text lines
    lines = text.split("\n")  # Split the input text into lines

    # Apply the gradient colors to each line
    for i, line in enumerate(lines):
        color_index = i % len(colors)  # Loop through the colors
        r, g, b = colors[color_index]  # Get the color for the line
        colored_line = text_color(r, g, b) + line + "\033[0m"  # Apply color and reset
        result.append(colored_line)

    return "\n".join(result)  # Join the colored lines and return the result


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
