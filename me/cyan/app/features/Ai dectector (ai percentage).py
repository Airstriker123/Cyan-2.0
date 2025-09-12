import os
import sys

try:
    from me.cyan.app.gui.banner import *
    from me.cyan.app.features import *
    from me.cyan.app.gui.menu import *
    from me.cyan.app.io import AppIo
    from me.cyan.app.settings.welcome import *
except ImportError as e:
    print(f'error: {e}')
    print('In: Cyan.py')
    os.system(r'pip install -r me\app\settings\packages.txt')