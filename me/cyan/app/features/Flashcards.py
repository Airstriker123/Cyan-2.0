import webbrowser
from colors_app import *
import sys
import requests
import json
import time
"""
if you need comments check essay structure guide this is same code
"""

# Function to display text slowly (for typewriter effect)
def Slow(text, delay=0.02):
    for line in text.split("\n"):  # Split text into lines
        print(line, flush=True)  # Print each line immediately (flush forces output)
        time.sleep(delay)  # Delay between printing each line

# Function to apply a gradient color effect to text
def MainColor2(text):
    # Define start and end colors (RGB values)
    start_color = (0, 200, 150)  # RGB color (light greenish-blue)
    end_color = (0, 255, 255)  # RGB color (cyan)

    num_steps = 16  # Number of gradient transition steps
    # Generate a gradient color transition
    colors = [
        (
            start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1),
            start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1),
            start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1),
        )
        for i in range(num_steps)
    ]
    colors += list(reversed(colors[:-1]))  # Mirror the colors to create a smooth loop effect

    # Function to convert RGB values to ANSI escape codes for terminal colors
    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    result = []
    lines = text.split("\n")  # Split text into lines
    for i, line in enumerate(lines):
        color_index = i % len(colors)  # Cycle through colors
        r, g, b = colors[color_index]
        colored_line = text_color(r, g, b) + line + "\033[0m"  # Apply color and reset at the end
        result.append(colored_line)

    return "\n".join(result)  # Join the lines back into a single strin

fc =  MainColor2(r"""

                   ███                                                                    
                ████  ████                                                                
              ███        ██                                                               
              ██          ██                                                              
              █           ██                                                              
              █        ██ ██                                                              
              █        ██ ██                                                              
              █        ██                                                                 
     ████████  ████████  ██████████████████████████████████████████                       
    ██████████ ████████  ███████████████████████████████████████████                      
    ██████████ ████████  ███████████████████████████████████████████                      
    ██████████ ████████  ███████████████████████████████████████████                      
    ██████████ ████████  ███████████████████████████████████████████                      
    ██████████ ████████  ███████████████████████████████████████████                      
    ██████████ ████████  ███████████████████████████████████████████  █████████           
             █  █     █  █                                            █████████           
    ██████████  ██████   ███████████████████████████████████████████  █████████           
    ████████████       █████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████                                                        ████                      
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████                                                        ████       ████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████                                                        ████       ████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
                                                                          █████           
               ████████████████████████████████████████████████████████████████           
               ████████████████████████████████████████████████████████████████           
               ████████████████████████████████████████████████████████████████           
               ████████████████████████████████████████████████████████████████           
               ████████████████████████████████████████████████████████████████           
                                                                                          

""")

#get keys at https://aimlapi.com
api_keys = {
    "",
    "",
    "",
    "",
    "",
    "",
}
api_url = "https://api.aimlapi.com/v1/chat/completions" #endpoint url for api keys
# Constants for defining the flashcard request format
define = "Create flashcards for the following topic:"
info = "also add info on the topic for preparing for test"

# Display the welcome ASCII art and menu options
Slow(fc)

print(f"""
{lc}=========================================================================
{purple}Current options for flashcards:
{cyan}[{white}1{cyan}]{yellow} Website {green}(recommended!)
{cyan}[{white}2{cyan}]{yellow} inbuilt A.i flashcards {red}(NOT recommended!)
{cyan}[{white}3{cyan}]{yellow} Exit app
{lc}=========================================================================
""")

# Input prompt to select an option from the menu
x = input(f'{yellow}Enter option {blue}(1,2):{red} ')

# Function to open a website in the browser
def website():
    print(f'{yellow}Opening web browser:')
    webbrowser.open("https://quizlet.com/au")  # Open the flashcard website
    print(f'{green}Success!')

# Function to send a message to the AI service and handle the response
def send_message(user_message):
    if not user_message:  # Check if no message is entered
        print("Error: No message entered.")
        return

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": f"{define}  {user_message} {info}"}
        ]
    }

    # Loop through API keys in case one fails
    for api_key in api_keys:
        try:
            response = requests.post(api_url, headers={
                "Authorization": f"Bearer {api_key}",  # Use API key for authentication
                "Content-Type": "application/json"
            }, data=json.dumps(payload))

            # Handle the response
            data = response.json()

            if data and "choices" in data:  # If the response contains a valid message
                ai_message = data["choices"][0]["message"]["content"]
                print(f"{cyan}Flashcards A.I🤖:",  f"{white}{ai_message}")
                break  # Exit the loop if request is successful
            else:
                print(f"{red}Error: Unable to retrieve response. Trying next API key.")
                print(f"{red}Switching to the next API key, please wait...")

        except requests.exceptions.RequestException as error:
            print(f"Error: Unable to connect with API key {api_key}. {error}")
            print(f"{red}Attempting to use the next available API key...")

# Function to interact with the AI to generate flashcards
def AI():
    print(f'{green}Remember to type{red} exit{green} once you have completed your prompts')
    while True:
        user_input = input(f"{yellow}\b👨‍💻Enter topic you want flashcards: ")
        if user_input.lower() == "exit":
            print(f'{red}Exiting program.')
            break
        send_message(user_input)

# Main logic to handle user input and perform actions based on the selected option
if x in ['1', 'one', 'first']:
    website()  # Open the flashcard website
elif x in ['2', 'two', 'second']:
    AI()  # Use the AI service to generate flashcards
elif x in ['3', 'three', 'ThREE', 'exit']:
    sys.exit()  # Exit the program
else:
    print(f'{red}INVALID OPTION FOR FLASHCARDS!')  # Handle invalid input
