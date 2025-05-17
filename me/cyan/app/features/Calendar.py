import os
from style import *
import time


def Slow(text, delay=0.03):
    for line in text.split("\n"):
        print(line, flush=True)
        time.sleep(delay)


def MainColor2(text):
    start_color = (0, 200, 150)
    end_color = (0, 255, 255)

    num_steps = 16
    colors = [
        (
            start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1),
            start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1),
            start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1),
        )
        for i in range(num_steps)
    ]

    colors += list(reversed(colors[:-1]))

    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    result = []
    lines = text.split("\n")

    for i, line in enumerate(lines):
        color_index = i % len(colors)
        r, g, b = colors[color_index]
        colored_line = text_color(r, g, b) + line + "\033[0m"
        result.append(colored_line)

    return "\n".join(result)


cal = MainColor2(r"""                                                                                                                                                                                                                              
        █████████████████████████████████████████████████████████████        
     ██████████████████████████████████████████████████████████████████      
    █████████████████████████████████████████████████████████████████████    
  ████████████████████   ███████████████████████████   ███████████████████   
  ███████████████████ █████████████████████████████ ███ ███████████████████  
  ███████████         ████                         ████         ███████████  
  ██████████          ███                           ███          ██████████  
  ██████████          ███                           ███          ██████████  
  ██████████          ███                           ███          ██████████  
  ██████████                                                     ██████████  
  ██████████                                                     ██████████  
  ██████████         █████     █████       █████      █████      ██████████  
  ██████████         █████     █████       █████      █████      ██████████  
  ██████████         █████     █████       █████      █████      ██████████  
  █████████                                                      ██████████  
  █████████          █████     █████       █████      █████      ██████████  
  █████████          █████     █████       █████      █████      ██████████  
  █████████          █████     █████       █████      █████      ██████████  
  █████████                                                      ██████████  
  █████████                                                      ██████████  
  █████████                                                      ██████████  
  █████████          █████     █████       █████      █████      ██████████  
  █████████          █████     █████       █████      █████      ██████████  
  █████████          █████     █████       █████      █████      ██████████  
  █████████                                                      ██████████  
  █████████                                                      ██████████  
  █████████          █████     █████       █████      █████      ██████████  
  █████████          █████     █████       █████      █████      ██████████  
  █████████          █████     █████       █████      █████      ██████████  
  █████████                                                      ██████████  
  █████████                                                      ██████████  
  ██████████                                                     ██████████  
  ████████████████████████████████████████████████████████████████████████   
   ██████████████████████████████████████████████████████████████████████    
     ███████████████████████████████████████████████████████████████████     
       ███████████████████████████████████████████████████████████████       
                                                                                                                                                                              
""")

Slow(cal)
#from calendar open app.py (flask app)
file_path = os.path.abspath("appdata/app_functions/Calendar/app.py")
print(f'{red}If python requests permmisions please click yes in order for the app to work. {purple}(retry this option if an error occurs)')
input(f'{yellow}press enter to launch app: ')
print(f'{green}Starting web app please wait')
os.system(f'start cmd /k python "{file_path}"')
print(f'{cyan}local server started!')



