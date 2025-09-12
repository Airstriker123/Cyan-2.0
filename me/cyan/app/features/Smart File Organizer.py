import os
try:
    from style import *
    import json  # json writing
    import requests  # web requests/packets
    import time
    import webbrowser  # to open links
    import sys
except ImportError as e:
    print(f"installing modules")
    os.system(r"pip install -r packages.txt")
    from style import *
    import json  # json writing
    import requests  # web requests/packets
    import time
    import sys
    import webbrowser  # to open links


class SmartFileOrganizer:
    """Sort folders and other files in order"""
    def __init__(self):

        pass

    def task_1(self):

        pass

    def task_2(self):

        pass


    def task_3(self):

        pass


#call class
SmartFileOrganizer()