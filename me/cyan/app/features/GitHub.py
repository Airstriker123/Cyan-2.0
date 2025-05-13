import webbrowser #to open links
from colors_app import * #colours
import time #ms delay for functions


# Function to display text slowly (for typewriter effect)
def Slow(text, delay=0.02):
    for line in text.split("\n"):  # Split text into lines
        print(line, flush=True)  # Print each line immediately (flush forces output)
        time.sleep(delay)  # Delay between printing each line

# Function to apply a gradient color effect to text
def MainColor2(text):
    # Define start and end colors (RGB values)
    start_color = (0, 200, 150)  # RGB color (light greenish-blue)
    end_color = (0, 255, 255)  # RGB color (cyan)

    num_steps = 16  # Number of gradient transition steps
    # Generate a gradient color transition
    colors = [
        (
            start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1),
            start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1),
            start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1),
        )
        for i in range(num_steps)
    ]
    colors += list(reversed(colors[:-1]))  # Mirror the colors to create a smooth loop effect

    # Function to convert RGB values to ANSI escape codes for terminal colors
    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    result = []
    lines = text.split("\n")  # Split text into lines
    for i, line in enumerate(lines):
        color_index = i % len(colors)  # Cycle through colors
        r, g, b = colors[color_index]
        colored_line = text_color(r, g, b) + line + "\033[0m"  # Apply color and reset at the end
        result.append(colored_line)

    return "\n".join(result)  # Join the lines back into a single strin


git = MainColor2(r"""

                         ███████████████████                         
                    █████████           █████████                    
                 ██████                       ██████                 
              █████                               █████              
            ████                                     █████           
          ████                                         ████          
        ███                                               ███        
      ████                                                 ████      
     ████        ███                             ███        ████     
    ███         █████████        ███        █████████         ███    
   ███          █████████████████████████████████████          ███   
  ███           █████████████████████████████████████           ███  
  ███           █████████████████████████████████████           ████ 
 ███            █████████████████████████████████████            ███ 
███            ███████████████████████████████████████            ███
███           █████████████████████████████████████████           ███
██            █████████████████████████████████████████            ██
██           ███████████████████████████████████████████           ██
██           ███████████████████████████████████████████           ██
██           ███████████████████████████████████████████           ██
██            █████████████████████████████████████████            ██
██            █████████████████████████████████████████            ██
███            ███████████████████████████████████████            ███
███             █████████████████████████████████████             ███
 ███             ███████████████████████████████████             ███ 
  ███              ███████████████████████████████              ████ 
  ███     █████        ███████████████████████                  ███  
   ███      █████          ███████████████                     ███   
    ███       ████         ████████████████                   ███    
     ████      ██████    ██████████████████                  ███     
      ████     ████████████████████████████                ████      
        ███      ██████████████████████████               ███        
          ███         ██  █████████████████             ███          
            ████          █████████████████          █████           
              █████       █████████████████       █████              
                 ██████   █████████████████   ██████                 
                    █████████████████████████████                    
                         ███████████████████                         
                     
""")
Slow(git)

print(f'{red}starting webbroswer{cyan}:{white} Github')
webbrowser.open('github.com') #open github with browser
