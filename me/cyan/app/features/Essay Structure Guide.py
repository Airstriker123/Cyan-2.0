from colors_app import *
import webbrowser
import sys
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

# this looks bad
fc = MainColor2(r"""
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
Slow(fc)
#simple ui
print(f'''
{green}Select options below:
{lc}=========================================================================||
{purple}Current options for Essay guide:                                     
{cyan}[{white}1{cyan}]{yellow} Website {green} (matrix) 
{cyan}[{white}2{cyan}]{yellow} Basic guide 
{cyan}[{white}3{cyan}]{red} Exit app                                      
{lc}=========================================================================||
''')

x = input(f'{yellow}Enter option {blue}(1,2,3):{red} ')

def web():
    webbrowser.open('https://www.matrix.edu.au/essay-writing-guide/overview/')

def base():
    print(f"""\n{lc}Essay Structure Guide:
    {green}1. Introduction:{white}
     {lc}  -{white} Hook/Attention Grabber
     {lc}  -{white} Background Information
      {lc} -{white} Thesis Statement

   {green} 2. Body Paragraphs: {white}
      {lc} - {white}Topic Sentence
     {lc}  -{white} Evidence & Explanation
      {lc} - {white}Link to Thesis

  {green}  3. Conclusion: {white}
     {lc}  -{white} Restate Thesis
      {lc} -{white} Summarize Key Points
      {lc} -{white} Closing Thought
    """)

# decides what to do when user enters input
if x in ['1', 'one', 'first']:
    web()
elif x in ['2', 'two', 'second']:
    base()
elif x in ['3', 'three', 'ThREE', 'exit']:
    sys.exit()
else:
    print(f'{red}INVALID!')
