import os
import subprocess
import sys
try:
    from me.cyan.app.gui.banner import *
    from me.cyan.app.features import *
    from me.cyan.app.gui.menu import Menu, Slow
    from me.cyan.app.io import AppIo
    from me.cyan.app.settings.welcome import *
except Exception as e:
    print(f'error: {e}')
    print('In: Cyan.py')

#background tasks
os.system(r'python me\cyan\app\settings\cyantaskbg.pyw')
os.system(r'python me\cyan\app\settings\cyantaskbgremove.pyw')
isrunning = True
if isrunning == True:
    os.system(r'python me\cyan\app\settings\cyantaskbg.pyw')


welcome_flag_path = os.path.join("me", "cyan", "app", "settings", "Welcome_complete.txt")
sys.stdout.reconfigure(encoding='utf-8') #better encoding for printing text


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
# if welcome_complete does not exist in path welcome user to app
if not os.path.exists(welcome_flag_path):
    first_time_run()
    with open(welcome_flag_path, "w") as file:
        file.write("Completed=True")
Main()
