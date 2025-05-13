# Import necessary modules
import os  # For interacting with the operating system
import sys  # For system-specific parameters and functions
import fade  # For text color fading effects
import colorama  # For colored terminal text
import time  # For adding delays in text output
from colorama import Fore, Style  # Import specific color attributes from colorama

# Get the current user's login name
name = os.getlogin()

# Determine the operating system
try:
    if sys.platform.startswith("win"):
        os_name = "Windows"
    elif sys.platform.startswith("linux"):
        os_name = "Linux"
    else:
        os_name = "Unknown"
except:
    os_name = "None"  # If an error occurs, default to "None"

# Define color variables for colored terminal output
color = colorama.Fore
red = Fore.RED
white = Fore.WHITE
green = Fore.GREEN
reset = Fore.RESET
blue = Fore.BLUE
yellow = Fore.YELLOW
cyan = Fore.CYAN
lc = Fore.LIGHTCYAN_EX
grey = Fore.LIGHTBLACK_EX
BEFORE_CYAN = f'{cyan + white}'
purple = Fore.MAGENTA
aqua = Fore.LIGHTCYAN_EX

# Function to print text slowly for a typewriter effect
def Slow(text):
    delai = 0.03  # Delay between lines
    lignes = text.split('\n')  # Split text into lines
    for ligne in lignes:
        print(ligne)
        time.sleep(delai)  # Add delay before printing the next line

# Function to create a gradient color effect in the menu
def MainColor(menu1):
    start_color = (0, 200, 150)  # RGB start color
    end_color = (0, 255, 255)  # RGB end color
    num_steps = 15  # Number of gradient steps

    # Generate gradient color transition
    colors = []
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))

    colors += list(reversed(colors[:-1]))  # Reverse colors to create a loop effect

    # Define which characters should have a gradient effect
    gradient_chars = '┌─┬│└┐┘┴├┤▓▒░█▄▌▀'
    num_colors = len(colors)

    # Function to generate an ANSI color escape sequence
    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    # Apply gradient color to each character in the menu
    lines = menu1.split('\n')
    result = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            color_index = (i + j) % num_colors  # Cycle through colors
            color = colors[color_index]

            if char in gradient_chars:  # Apply gradient only to specified characters
                result.append(text_color(*color) + char + "\033[0m")
            else:
                result.append(char)

        if i < len(lines) - 1:
            result.append('\n')

    return ''.join(result)

# Function to simulate typing effect when printing text
def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)  # Add a small delay between printing each character
    print()  # Print a new line at the end

# Function to clear the terminal screen
def Clear():
    if os_name == "Windows":
        os.system("cls")  # Clear command for Windows
    elif os_name == "Linux":
        os.system("clear")  # Clear command for Linux

# Function to display a welcome message with styling
def welcome():
    sys.stdout.write(f"{lc}Cyan🤖: {white}")
    type_text(f"Hello {purple}{name},{white} welcome to {lc}Cyan! 😁🎉 \n", 0.04)

    sys.stdout.write(f"{lc}Cyan🤖: {white}")
    type_text("Cyan is a multi-tool designed to help students with their HSC journey! 📚👑 \n", 0.05)

# Function to display an introduction when the app is run for the first time
def first_time_run():
    # ASCII banner with a faded effect
    banner = """    
  ▄ ▄   ▄███▄   █     ▄█▄    ████▄ █▀▄▀█ ▄███▄          ▄▄▄▄▀ ████▄     ▄█▄  ▀▄    ▄ ██      ▄         ▄ 
 █   █  █▀   ▀  █     █▀ ▀▄  █   █ █ █ █ █▀   ▀      ▀▀▀ █    █   █     █▀ ▀▄  █  █  █ █      █       █  
█ ▄   █ ██▄▄    █     █   ▀  █   █ █ ▄ █ ██▄▄            █    █   █     █   ▀   ▀█   █▄▄█ ██   █     █   
█  █  █ █▄   ▄▀ ███▄  █▄  ▄▀ ▀████ █   █ █▄   ▄▀        █     ▀████     █▄  ▄▀  █    █  █ █ █  █     █   
 █ █ █  ▀███▀       ▀ ▀███▀           █  ▀███▀         ▀                ▀███▀ ▄▀        █ █  █ █         
  ▀ ▀                                ▀                                                 █  █   ██     ▀   
                                                                                      ▀                                                                        
"""

    Clear()  # Clear the screen before displaying the banner
    faded_text = fade.water(banner)  # Apply a water-like gradient effect
    Slow(f"{faded_text}\n")  # Display banner with a slow effect

    # Display a security warning
    type_text(f"{red}[{yellow}❗{red}]{yellow} ⚠️ WARNING:{red} Api keys is not included it this version!\n", 0.0009999999999)
    print(f'{purple}========================================================================================================================\n')

    # Call welcome function to greet the user
    welcome()

    # Provide an introduction on how to use the app
    sys.stdout.write(f"{lc}Cyan🤖: {white}")
    type_text(f"Cyan is a very simple and easy app to use! \n", 0.025)

    sys.stdout.write(f"{lc}Cyan🤖: {white}")
    type_text("Let's say you don't know what a word means, you can simply use the dictionary option to find it! \n", 0.025)

    sys.stdout.write(f"{lc}Cyan🤖: {white}[")
    type_text(
        f"{red}09{white}] {yellow}Dictionary & Thesaurus, where {green}09 {yellow}or{green} 9 {white}is the number you have to type to start the app. 😊 \n",
        0.025)

    sys.stdout.write(f"{lc}Cyan🤖: {white}")
    type_text(f"Begin by typing the number {yellow}9{white} and pressing {red}Enter! \n", 0.025)

    # Wait for the user to acknowledge the message
    input(f'{red}Press {lc}enter {red}if you understand how to use the app:')
