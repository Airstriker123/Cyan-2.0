import os
import sys
try:
    from style import *
    import shutil
    import tempfile
    import ctypes
    import winshell
except:
    print(f'{blue}Installing winshell')
    os.system("pip install pywin32")
    os.system("pip install winshell")

    import winshell

class EmptyRecycleBin:
    def __init__(self):
        self.choice()



    def choice(self):
        try:
            confirm = input(f'{yellow}empty bin? {lc}[Y/N]{yellow}:->{reset}').lower()
            if confirm in ['y', 'yes']:
                self.empty()
            elif confirm in ['n', 'no']:
                print(f'{green}Exiting...{reset}')
            else:
                print(f'{red}Exiting...{reset}')
        except Exception as e:
            print(f'{red}error: {purple}{e}')


    def empty(self):
        try:
            ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 1)
            Slow(f"{green}Recycle Bin emptied.")
        except:
            Slow(f"{red}Failed to empty Recycle Bin")

EmptyRecycleBin()



