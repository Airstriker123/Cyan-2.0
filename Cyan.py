import os
import ctypes
import atexit
import signal
import sys
try:
    from me.cyan.app.gui.banner import *
    from me.cyan.app.features import *
    from me.cyan.app.gui.menu import Menu, Slow
    from me.cyan.app.io import AppIo
except Exception as e:
    print(f'error: {e}')
    print('In: Cyan.py')

# Launch background task
os.system(r'python me\cyan\app\settings\cyantaskbg.py')


def cleanup():
    print("Cyan delete task...")
    os.system(r'start me\cyan\app\settings\cyantaskbgremove.py')


# Register normal exit
atexit.register(cleanup)

# Register signal handlers
def signal_handler(sig, frame):
    cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Register Windows close (X) event
CTRL_EVENTS = (0, 1, 2, 5, 6)

def console_ctrl_handler(ctrl_type):
    if ctrl_type in CTRL_EVENTS:
        cleanup()
        return True
    return False

ctypes.windll.kernel32.SetConsoleCtrlHandler(
    ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_uint)(console_ctrl_handler),
    True
)


# Main application class
class Main:
    def __init__(self):
        self.running = True
        self.main()

    def main(self):
        while self.running:
            os.system('cls')
            menu_instance = Menu(None)
            Banner()
            Slow(MainColor(menu_instance.menu1))
            AppIo(object)


# Run the app once — cleanup will handle any exits
try:
    Main()
except KeyboardInterrupt:
    cleanup()
except Exception as e:
    print(f'Unexpected error: {e}')
    cleanup()
