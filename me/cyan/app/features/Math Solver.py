# Import necessary modules
from colors_app import *  # Importing custom colors module
import time  # For adding delays in text output
import sympy as sp  # For symbolic mathematical computations
import re  # For regular expressions (used to modify input expressions)
import math  # For mathematical functions like factorial

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

    return "\n".join(result)  # Join the lines back into a single string

# Function to safely evaluate mathematical expressions
def safe_eval(expression):
    # Replace '^' with '**' for exponentiation (Python syntax)
    expression = expression.replace('^', '**')
    # Replace factorial notation (e.g., "5!") with math.factorial(5)
    expression = re.sub(r'(\d+)!', r'math.factorial(\1)', expression)

    # Define allowed mathematical functions
    allowed_funcs = {
        "sin": sp.sin,
        "cos": sp.cos,
        "tan": sp.tan,
        "sqrt": sp.sqrt,
        "log": sp.log,  # log() defaults to base 10
        "ln": lambda x: sp.log(x, sp.E),  # Natural logarithm (ln)
        "exp": sp.exp,  # Exponential function e^x
        "pi": sp.pi,  # π constant
        "e": sp.E,  # Euler's number
        "factorial": math.factorial,  # Factorial function
        "abs": abs,  # Absolute value
        "round": round  # Round function
    }

    try:
        # Evaluate the mathematical expression safely using sympy
        result = sp.sympify(expression, locals=allowed_funcs).evalf()
        # Return rounded result if it's a number, else return as is
        return round(result, 10) if isinstance(result, (int, float)) else result
    except Exception:
        return "Invalid Expression"  # Handle any errors gracefully

# Function to run the Math Solver
def math_solver():
    # ASCII art with gradient effect
    cal = MainColor2("""
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████
 █████                           █████
 █████                           █████
 █████                           █████
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████
 ███████      ██      ██      ████████
 ███████      ██      ██      ████████
 ███████      ██      ██      ████████
 █████████████████████████████████████
 ███████      ██      ██      ████████
 ███████      ██      ██      ████████
 ████████    ████    ████    █████████
 █████████████████████████████████████
 ███████      ██      ██      ████████
 ███████      ██      ██      ████████
 █████████████████████████████████████
 ███████      ██      ██      ████████
 ███████      ██      ██      ████████
 ███████      ██      ██      ████████
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████
 █████████████████████████████████████

""")
    Slow(cal)  # Print ASCII banner with slow effect
    print(f"{yellow}Type {red}'exit' {yellow}to leave app!{reset}")
    print(f"{purple}Supports:{cyan} +, -, *, /, ^, !, sin(), cos(), tan(), sqrt(), log(), ln(), exp(), pi, e, abs(), round()")

    # Loop to continuously take user input
    while True:
        expression = input(f"\n{yellow}Enter a math expression {lc}(e.g., 5+3*2, 4!): {white}")

        # Exit the app if user types 'exit'
        if expression.lower() == "exit":
            print(f"{red}Exiting Math Solver...{reset}")
            break

        # Evaluate the mathematical expression
        result = safe_eval(expression)
        print(f"{lc}Result:{white} {result}")  # Display result

# Run the Math Solver function
math_solver()
