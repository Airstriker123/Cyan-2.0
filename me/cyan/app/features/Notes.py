from colors_app import *
import webbrowser
import subprocess
import sys
import time
'''CHECK FLASHCARDS FOR COMMENTS SAME CODE! '''

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


note = MainColor2(r"""                           
π∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞               
∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞              
∞∞√                                                                     ∞∞=÷≠≈≠∞π        
∞∞√                                                                     ≠×××÷=≠≠≠=≠√     
∞∞√                                                                    ÷××××××÷≠≠=≠≠≠≈   
∞∞√                                                                  π××××××××××÷==≠≠=≠≈ 
∞∞√                                                                ππ÷×××××××××××××÷=≠==≠
∞∞√                                                               √π√√=×××××××××××××××÷==
∞∞√      ππππππππππππππππ    πππππππππππππππ                    π∞∞√π√∞√÷××××××××××××××××
∞∞√                                                            π√√√∞∞ππ√∞√÷××××××××××××××
∞∞√                                                            ∞∞√ππ√∞√√π√√√≠×××××××××××≈
∞∞√                                                           √√√∞∞√ππ√∞√√ππ√∞√≠÷××××××√ 
∞∞√                                                         π√√√√∞∞∞∞√√∞∞∞∞∞∞√√∞∞∞√≠÷=   
∞∞√                                                        √√√√√√√∞√∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞√   
∞∞√                                                      π√√√√√√√∞√√√√∞∞∞∞∞∞∞∞∞∞∞∞∞∞√    
∞∞√                                                     π√√√√√√√∞√√√√√√√√∞∞∞∞∞∞∞∞∞∞π     
∞∞√      πππππππππππππππππππππππππ           ππππππππππ√√√√√√√∞∞√√√√√√√√≠=≠≈√√∞∞∞∞       
∞∞√                                                   √√√√√√√∞√√√√√√√√√≠=≈∞∞∞≈≈√         
∞∞√                                                 π√√√√√√√∞√√√√√√√√∞=≠∞∞∞∞∞∞π          
∞∞√                                                √√√√√√√∞∞√√√√√√√√≈=≠∞∞∞∞∞√            
∞∞√                                               √√√√√√√∞∞√√√√√√√√≈≠≈∞∞∞∞∞√             
∞∞√                                              √√√√√√√∞√√√√√√√√√≠≠∞∞∞∞∞∞√              
∞∞√       ππππππππππππππππ          πππππππ  π √√√√√√√∞∞√√√√√√√√∞=≠∞∞∞∞∞∞√∞              
∞∞√                                           √√√√√√√∞∞√√√√√√√√≈=≈∞∞∞∞∞√∞∞∞              
∞∞√                                          √√√√√√√≈√√√√√√√√√≠≠≈∞∞∞∞∞π ∞∞∞              
∞∞√                                        π√√√√√√√∞√√√√√√√√√=≠∞∞∞∞∞√π  ∞∞∞              
∞∞√                                       √√√√√√√∞∞√√√√√√√√≈=≈∞∞∞∞∞√    ∞∞∞              
∞∞√                                      √√√√√√√∞∞√√√√√√√√≠=∞∞∞∞∞∞√     ∞∞∞              
∞∞√                ππππ√πππππππππππππππ√√√√√√√√∞√√√√√√√√∞≠≠∞∞∞∞∞√π      ∞∞∞              
∞∞√      π      π                     √√√√√√√√∞√√√√√√√√∞=≈∞∞∞∞∞√        ∞∞∞              
∞∞√                                  √√√√√√√∞√√√√√√√√√≈=≈∞∞∞∞∞√         ∞∞∞              
∞∞√                                 √√√√√√√∞√√√√√√√√√=≠∞∞∞∞∞√√          ∞∞∞              
∞∞√                                √√√√√√∞∞√√√√√√√√≈=≠∞∞∞∞∞√            ∞∞∞              
∞∞√                                √√√√√∞∞√√√√√√√√≈≠≈∞∞∞√∞√             ∞∞∞              
∞∞√        πππππ      πππππ        π√√√√√√√√√√√√√≠≠≈∞∞∞∞∞√√∞∞√√√√       ∞∞∞              
∞∞√      π       ππππ             πππππ√√√√√√√√∞=≠∞∞∞∞∞√π     π         ∞∞∞              
∞∞√                               ππππππ√√√√√√≈=≈∞∞∞∞∞√                 ∞∞∞              
∞∞√                               ππππππ ππ√√√√∞∞∞∞∞∞√                  ∞∞∞              
∞∞√                               ππππππππππππ π√√√√π                   ∞∞∞              
∞∞√                             √∞πππππππππππππππ                       ∞∞∞              
∞∞√                             ≠×∞ππππππππππ                           ∞∞∞              
∞∞√                             ÷×××≈πππππ                              ∞∞∞              
∞∞√                            √×××××××≠π                               ∞∞∞              
∞∞√     ππ    πππππππ   πππππππ≠××××≠π                                  ∞∞∞              
∞∞√                                                                     ∞∞∞              
∞∞√                                                                     ∞∞∞              
∞∞√                                                                     ∞∞∞              
∞∞√                                                                     ∞∞∞              
∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞                       
""")
Slow(note)
print(f'''
{green}Select options below:
{lc}=========================================================================||
{purple}Current options for flashcards:                                     
{cyan}[{white}1{cyan}]{yellow} Website {green} (notion) 
{cyan}[{white}2{cyan}]{yellow} inbuilt  {yellow}(notepad/windows only)
{cyan}[{white}3{cyan}]{red} Exit app                                      
{lc}=========================================================================||

''')

x = input(f'{yellow}Enter option {blue}(1,2,3):{red} ')
def website():
    print(f'{yellow}Opening web browser:')
    webbrowser.open("https://www.notion.com/")
    print(f'{green}Success!')

def inbuilt():
    print(f'{yellow}Starting notepad.exe!')
    subprocess.Popen(["notepad.exe"])


if x in ['1', 'one', 'first']:
    website()
elif x in ['2', 'two', 'second']:
    inbuilt()
elif x in ['3', 'three', 'ThREE', 'exit']:
    sys.exit()
else:
  print(f'{red}INVALID OPTION FOR FLASHCARDS!')
