import sys
import time
from .colors import *
import sys
import time
# same a welcome.py 
def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
# same a welcome.py 
def welcome():
    sys.stdout.write(f"{lc}Cyan🤖: {white}")
    type_text("Hello, welcome to Cyan! 😁🎉", 0.04)

    sys.stdout.write(f"{lc}Cyan🤖: {white}")
    type_text("Cyan is a multi-tool designed to help students with their HSC journey 📚👑", 0.05)

# same a welcome.py 
def help():
    sys.stdout.write(f"{lc}Cyan🤖: {white}")
    type_text("Cyan is a very simple and easy app to use!", 0.025)
    sys.stdout.write(f"{lc}Cyan🤖: {white}")
    type_text("Let's say you don't know what a word means, you can simply use the dictionary option to find it.", 0.025)
    sys.stdout.write(f"{lc}Cyan🤖: {white}[")
    type_text(f"{red}09{white}] {yellow}Dictionary & Thesaurus, where {green}09 {yellow} or {green} 9 {white}is the number you have to type to start the app :)", 0.025)
    sys.stdout.write(f"{lc}Cyan🤖: {white}")
    type_text(f"Begin by typing the number {yellow}9{white} and pressing {red}Enter!", 0.025)


