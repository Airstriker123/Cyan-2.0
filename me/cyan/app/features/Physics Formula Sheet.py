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
# amazing acii art for banner
note = MainColor2(r"""                          
                                                                                    
                     ███                                                                          
                 ███████████                                                                       
                ██        ███                                                                      
               ██          ███                               ████████                              
              ███           ███████                     ███████     ████                           
               ██           ██    █████              █████             ███                         
               ███         ██        ████          ████                 ███                        
                ████     ███            ████    ████                     ██                        
                 █████████                 ███████                       ███                       
                 ██                         ████                          ██                       
                 ██                       ███  ███                        ██                       
                 ██                      ███     ███                      ██                       
                 ██                    ███         ██                     ██                       
                 ██                  ███            ███                  ██                        
                 ██                 ███  ███████████ ████                ██                        
                  ██      █████████████████████████████████████████      ██                        
                  █████████      ███                     ██      ██████████                        
              ███████           ███                       ███           ███████                    
          █████    ██          ██                          ███         ██     █████                
       ████         ██        ██             ███             ██       ███         ████             
    ████            ███     ███          ███████████          ██      ██             ███           
   ███               ██    ███         ███         ███         ██    ██               ██████████   
  ██                  ██  ███         ███           ██          ██  ███              ███       ███ 
 ██                    █████          ██             ██          █████              ██          ████
███                    ████           ██             ██           ███              ███           ███
███                    ████           ██            ███           ███              ███           ███
 ██                    █████           ███         ███           ██ ██              ██          ████
  ██                  ██  ███           █████   ████            ██   ██              ███       ███ 
   ███               ██    ███             ██████              ██    ███               █████████   
     ███            ███      ██                               ██      ██            ████           
       ████         ██        ██                            ███        ██        █████             
          █████    ███         ███                         ███         ███   █████                 
              ███████           ███                       ███           ███████                    
                  ███████████     ██                     ██    ████████████                        
                  ██       ███████████████████████████████████████       ██                        
                 ███                ███               ██                 ███                       
                 ██                   ███           ███                   ██                       
                 ██                    ███         ██                     ██                       
                 ██                      ███     ███                      ██                       
                 ██                        ███ ███                        ██                       
                 ███████                     ███                          ██                       
               ████   ████                 ███ ███                        ██                       
              ██         ███             ███     ████                    ██                        
             ██           ██          ████          ███                 ███                        
             ██           ██      █████               █████            ███                        
             ██           ██████████                      ██████████████                           
              ██         ██████                                 ████                               
               █████ █████                                                                         
                  █████                                                                                           
""")
Slow(note)
# to lazy to make a function zzzzzzzzzzzzz
# also to lazy to make it look better -_-
#opens chrome
webbrowser.open('https://www.geeksforgeeks.org/list-of-physics-formulas/')
