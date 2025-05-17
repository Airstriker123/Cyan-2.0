import os
import subprocess
try:
    from me.cyan.app.gui.banner import *
    from me.cyan.app.features import *
    from me.cyan.app.gui.menu import Menu, Slow
    from me.cyan.app.io import AppIo
except Exception as e:
    print(f'error: {e}')
    print('In: Cyan.py')

#background tasks
os.system(r'python me\cyan\app\settings\cyantaskbg.pyw')
os.system(r'start me\cyan\app\settings\cyantaskbgremove.pyw')

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
