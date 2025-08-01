import time
from style import *
import os
import sys
try:
    import pyautogui
except:
    pips = ["pyautogui"
            ""
            "",]
    for pip in pips:
        print(f"{yellow}Installing " + pip + f"{purple}")
        os.system(f"pip install {pip}")

class menu:
    def __init__(self
                 ):
        #banner
        print(MainColor2(f"""                                                           
                      ▄▄▄▄███▄▄▄▄      ▄████████  ▄████████    ▄████████  ▄██████▄     ▄████████ 
                    ▄██▀▀▀███▀▀▀██▄   ███    ███ ███    ███   ███    ███ ███    ███   ███    ███ 
                    ███   ███   ███   ███    ███ ███    █▀    ███    ███ ███    ███   ███    █▀  
                    ███   ███   ███   ███    ███ ███         ▄███▄▄▄▄██▀ ███    ███   ███        
                    ███   ███   ███ ▀███████████ ███        ▀▀███▀▀▀▀▀   ███    ███ ▀███████████ 
                    ███   ███   ███   ███    ███ ███    █▄  ▀███████████ ███    ███          ███ 
                    ███   ███   ███   ███    ███ ███    ███   ███    ███ ███    ███    ▄█    ███ 
                     ▀█   ███   █▀    ███    █▀  ████████▀    ███    ███  ▀██████▀   ▄████████▀  
                                                              ███    ███                                                 
        {reset}"""))
#menu
        print(MainColor2(f"""
                            {green}[1] - {red}[Auto typer] |--> {MainColor2("(auto types text from input works for docs)")} 
"""))

class Macro:
    def __init__(self):
        choice = input(MainColor2(f"""Enter macro to execute:-> """))
        if choice in ["1", "one", "01"]:
            self.AutoType()
        if choice in ["exit"]:
            sys.exit()
        else:
            print(f"{red}INVALID!")



    def AutoType(self):
        scanner_input = input(f"{purple}Enter text to type:-> {reset}")
        sleep = float(input('enter delay in ms (e.g 0.1=100ms):->'))
        text = scanner_input
        print("Switch to Google Docs and place your cursor in the document. Typing will start in 5 seconds...")
        time.sleep(5)  # 5 seconds until macro starts

        for line in text.split("\n"):
            pyautogui.write(line, interval=sleep)
            pyautogui.press("enter")
        input("Typing complete!")




#main method to call all functions (controls module)
class Main:
    def __init__(self):
        while True:
            os.system("cls||clear")
            menu()
            Macro()
Main()