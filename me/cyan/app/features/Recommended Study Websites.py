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

#animation
# is that a minion studying?
#app banner
study = MainColor2(r"""                          
                                         ::::::::::::::::::::                                        
                                   ::::::::::::::::::::::::::::-:                                   
                               :::::::::::::::::::::::::::::::::::---                               
                            ::::::::::::::::::::::::::::::::::::::::---:                            
                          ::::::::::::::::::::::::::::::::::::::::::::----                          
                        :::::::::::::::::::::::::::::::::::::::::::::::::---                        
                      :::::---------::::::::::::::::::::::::::::---------:----                      
                     :::-=+**********+=-::::::::::::::::::::-=+**********+=----                     
                    ::=******************=::::::::::::::::=+*****************=--                    
                   :-+******        ******+-:::::---::::-+******        ******+--                   
                 ::-******            ******=+********+=*****+            ******=--                 
                 :-*****                ********************                *****=-                 
              *********                  *****=------=*****                  *********              
             **********      ++++++      ****+-::::::-+****      ++++++      **********             
               =-=+****     ++++++++     ****+-::::::-+****     ++++++++     *****===               
              --:-+****     ++++++++     ****+-::::::-+****     ++++++++     ****+----              
              -:::=*****    ++++++++    *****=::::::::=*****    ++++++++    *****=----              
              --::-+*****    ++++++    *****+-::::::::-+*****    ++++++    +****+-----              
             ---:::-+******          ******+-::::::::::-+******          ******+-------             
             ---:::::=********+  +********=::::::::::::::=********+  +********=-:------             
             ---:::::::=****************=::::::::::::::::::=****************=::::------             
             ---:::::::::-=++******++=-::::::::::::::::::::::-=++******++=-::::::------             
         ....:---:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::------:....         
         ......::::::::::::::::::::::::::-++++++++++++++++-:::::::::::::::::::::----:......         
        ...........:::::::::::::::::::::::=**************=:::::::::::::::::::::::...........        
    === ...............:::::::::::::::::::-=************+-:::::::::::::::::::............... ===    
    ======--:..............:::::::::::::::::-+********+-:::::::::::::::::..............:--======    
    =============::.............:::::::::::::::--==--:::::::::::::::.............::=============    
     =================-:::.........::::::::::::::::::::::::::::::.........:::-=================     
     =======================--:........::::::::::::::::::::::........:--=======================     
     =============================--:......::::::::::::::......:--=============================     
      ==================================-::.....:::::....::-==================================      
      ========================================--++++--=======================================-:     
     ::::::::-================================++++++++==================================-::::::--   
    -::::::::::-==============================++++++++================================-::::::::---  
    --::::::::::-=============================++++++++===============================-:::::::::---  
    ---::::::::::-============================++++++++==============================-:::::::::----  
     ---::::::::::-===========================++++++++=============================-:::::::::----   
     ----:::::::::-===========================++++++++=============================:::::::::----    
      ----::::-----===========================++++++++============================-:::::::::----    
       -----------============================++++++++=============================--:::::-----     
        --------==============================++++++++===============================---------      
           ===================================++++++++===================================           
           ===================================++++++++===================================           
            ==================================++++++++==================================            
             =================================++++++++=================================             
                  ============================++++++++============================                  
                      ========================++++++++========================                      
                           ===================++++++++===================                           
                                 =============++++++++=============                                 
                                     =========++++++++=========                                     
                                          ====++++++++====                                          
                                              ++++++++                                              
                                               ++++++                                               
                                                                                                         
""")
#links of sites 
try:
    links = {
        "Physics": {
            "Khan Academy": "https://www.khanacademy.org/science/physics",
            "HyperPhysics": "http://hyperphysics.phy-astr.gsu.edu/",
            "Physics Classroom": "https://www.physicsclassroom.com/",
            "MIT OpenCourseWare": "https://ocw.mit.edu/courses/physics/",
            "PhET Interactive Simulations": "https://phet.colorado.edu/"
        },
        "Mathematics": {
            "Khan Academy": "https://www.khanacademy.org/math",
            "Paul's Online Math Notes": "http://tutorial.math.lamar.edu/",
            "Desmos": "https://www.desmos.com/",
            "Wolfram Alpha": "https://www.wolframalpha.com/",
            "PatrickJMT": "https://www.youtube.com/user/patrickJMT",
            "Art of Problem Solving": "https://artofproblemsolving.com/",
            "Project Euler": "https://projecteuler.net/",
            "The Math Learning Center": "https://www.mathlearningcenter.org/"
        },
        "English": {
            "Grammarly": "https://www.grammarly.com/",
            "Purdue OWL": "https://owl.purdue.edu/",
            "BBC Bitesize": "https://www.bbc.co.uk/bitesize/subjects/zckwqty",
            "SparkNotes": "https://www.sparknotes.com/",
            "TED-Ed": "https://ed.ted.com/"
        },
        "Software Engineering": {
            "W3Schools": "https://www.w3schools.com/",
            "GeeksforGeeks": "https://www.geeksforgeeks.org/",
            "FreeCodeCamp": "https://www.freecodecamp.org/",
            "MDN Web Docs": "https://developer.mozilla.org/en-US/",
            "Codecademy": "https://www.codecademy.com/",
            "GitHub": "https://github.com/"
        },
        "Enterprise Computing": {
            "IBM SkillsBuild": "https://www.ibm.com/training/skillsbuild",
            "Oracle Academy": "https://academy.oracle.com/",
            "Microsoft Learn": "https://learn.microsoft.com/en-us/",
            "AWS Educate": "https://aws.amazon.com/education/awseducate/"
        },
        "Other Useful Resources": {
            "EdX": "https://www.edx.org/",
            "Coursera": "https://www.coursera.org/",
            "OpenStax": "https://openstax.org/",
            "CrashCourse (YouTube)": "https://www.youtube.com/user/crashcourse",
            "YouTube EDU": "https://www.youtube.com/education",
            "TED Talks": "https://www.ted.com/talks",
            "Library Genesis": "https://libgen.is/",
            "Google Scholar": "https://scholar.google.com/",
            "Academic Earth": "https://academicearth.org/",
            "Study.com": "https://www.study.com/",
            "Skillshare": "https://www.skillshare.com/",
            "LinkedIn Learning": "https://www.linkedin.com/learning/",
            "Memrise": "https://www.memrise.com/",
            "Socratic": "https://www.socratic.org/",
            "Open Culture": "https://www.openculture.com/",
            "ChatGPT": "https://chatgpt.com/"
        }
    }

 
    def format_links(links):
        display_link = "" #empty string for formated links
       # loop to print all items in links
        for category, sites in links.items():
            display_link += "\n" + MainColor2(category) + "\n"
               
            def add_sites(prefix, sites_dict):
                nonlocal display_link  # Allows modification of the display_link variable from the outer scope
                for i, (site, url) in enumerate(sites_dict.items()): 
                    if isinstance(url, dict):  # Check if the URL is another dictionary (nested structure)
                        display_link += f"{prefix}├─ {red + site}\n" 
                        add_sites(prefix + "│   ", url)
                    else:
                        if i == len(sites_dict) - 1:  # If it's the last site in the list, use '└─' (final branch)
                            display_link += f"{prefix}└─ {red + site}: {white + url}" + "\n"
                        else:
                            display_link += f"{prefix}├─ {red + site}: {white + url}" + "\n"  # Otherwise, use '├─' to indicate more items follow

            add_sites("", sites) 

        return display_link


    formatted_links = format_links(links)
    Slow(study + MainColor2(formatted_links)) #call function 
except Exception as e:
    print(f'{red}error: {purple}{e}') #error catching
