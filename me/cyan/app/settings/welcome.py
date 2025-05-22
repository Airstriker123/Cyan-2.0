# Import necessary modules
import os  # For interacting with the operating system
import sys
from me.cyan.app.gui.animations.style import *
from random import randint
from os import system
from me.cyan.app.gui.animations.colorama.__init__ import * # For system-specific parameters and functions

# Get the current user's login name
name = os.getlogin()

class Fade:
    def greenblue(self, text):
        system("");
        faded = ""
        blue = 100
        for line in text.splitlines():
            faded += (f"\033[38;2;0;255;{blue}m{line}\033[0m\n")
            if not blue == 255:
                blue += 15
                if blue > 255:
                    blue = 255
        return faded


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
    faded_text = Fade().greenblue(banner)  # ✅ Works
    # Apply a water-like gradient effect
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
