# Import necessary modules
from style import *  # Importing custom colors module
import os
import time  # For adding delays in text output
try:
    import sympy as sp  # For symbolic mathematical computations
except:
    print(f'{lc}please wait installing package...')
    os.system('pip install sympy') #check
    import sympy as sp
import re  # For regular expressions (used to modify input expressions)
import math  # For mathematical functions like factorial

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
