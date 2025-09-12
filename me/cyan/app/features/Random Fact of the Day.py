import os
try:
    from style import *
    import json  # json writing
    import requests  # web requests/packets
    import time
    import webbrowser  # to open links
    import sys
except ImportError as e:
    print(f"installing modules")
    os.system(r"pip install -r packages.txt")
    from style import *
    import json  # json writing
    import requests  # web requests/packets
    import time
    import sys
    import webbrowser  # to open links


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
