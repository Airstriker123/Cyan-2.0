from .initialise import init, deinit, reinit, colorama_text, just_fix_windows_console
from .ansi import Fore, Back, Style, Cursor
from .ansitowin32 import AnsiToWin32

red = Fore.RED
white = Fore.WHITE
green = Fore.GREEN
reset = Fore.RESET
blue = Fore.BLUE
yellow = Fore.YELLOW
cyan = Fore.CYAN
lc = Fore.LIGHTCYAN_EX
grey = Fore.LIGHTBLACK_EX
BEFORE_CYAN= f'{cyan + white}'
purple = Fore.MAGENTA
orange = '\033[38;5;208m'

__version__ = '0.4.6'

