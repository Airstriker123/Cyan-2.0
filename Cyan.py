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

Main()
