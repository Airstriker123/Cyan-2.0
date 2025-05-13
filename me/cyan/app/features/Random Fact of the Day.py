import requests
import webbrowser #api!
from colors_app import *
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


fc = MainColor2(r"""
                                          ...:----:...                                              
                                     .:=#@@@@@@@@@@@@@@%*-..                                        
                                  .:#@@@@@@@%#*****#%@@@@@@@+..                                     
                               ..-@@@@@%-...... ........+@@@@@@..                                   
                               :%@@@@=..   .#@@@@@@@@#=....+@@@@*.                                  
                             .+@@@@=.      .*@@@%@@@@@@@@=...*@@@@:.                                
                            .#@@@%.                 .=@@@@@=. .@@@@-.                               
                           .=@@@#.                    .:%@@@*. -@@@%:.                              
                           .%@@@-                       .*@@*. .+@@@=.                              
                           :@@@#.                              .-@@@#.                              
                           -@@@#                                :%@@@.                              
                           :@@@#.                              .-@@@#.                              
                           .%@@@-.                             .+@@@=.                              
                           .+@@@#.                             -@@@%:.                              
                            .*@@@%.                          .:@@@@-.                               
                             .+@@@@=..                     ..*@@@@:.                                
                               :%@@@@-..                ...+@@@@*.                                  
                               ..-@@@@@%=...         ...*@@@@@@@@#.                                 
                                  .:*@@@@@@@%*++++**@@@@@@@@=:*@@@@#:.                              
                                     ..=%@@@@@@@@@@@@@@%#-.   ..*@@@@%:.                            
                                        .....:::::::....       ...+@@@@%:                           
                                                                  ..+@@@@%-.                        
                                                                    ..=@@@@%-.                      
                                                                      ..=@@@@@=.                    
                                                                         .=%@@@@=.                  
                                                                          ..-%@@@-.                 
                                                                             ....
""")
def random_fact():
    Slow(fc)
    print(f'{yellow}Fetching fact please wait...')
    try:
       
         # endpoint
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en") #get response from url
        if response.status_code == 200:
        #extract text from api
            fact = response.json()["text"]
            print(f"\n{lc}Random Fact:{white} {fact}")
        else:
            print(f"\n{red}Couldn't fetch a fact, try again later.")
    except: #error
        print(f"\n{red}Network error. Check your internet connection.")


random_fact()
