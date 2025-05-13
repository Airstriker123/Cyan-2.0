try:
    import os
    import sys
    from me.cyan.app.gui.animations.colorama.__init__ import *
    from me.cyan.app.gui.animations.style import *
    from me.cyan.app.gui.menu import Menu
    from me.cyan.app.gui.banner import banner, Fade
    import datetime
except Exception as e:
    print(e)
    print('in: io.py')

class AppIo(object
):

    def continuemain(self):
        BEFORE = f'{red}[{white}'
        AFTER = f'{red}]'
        INFO = f'{BEFORE}!{AFTER} |'
        menu_number = '1'  # menu number
        username_pc = os.getlogin()
        ERROR = f'{BEFORE}x{AFTER} |'

        while True:
            Slow(banner)
            menu_instance = Menu(None)
            Slow(MainColor(menu_instance.menu1))
            AppIo(object)

    # Get the current time formatted as HH:MM:SS
    def current_time_hour(self):
        return datetime.datetime.now().strftime('%H:%M:%S')

    def __init__(self, choice
                 ):
        self.option_01 = "Google-Classroom"  # 1
        self.option_02 = "ChatGPT (Web-Version)"  # @
        self.option_03 = "GitHub"  ##@
        self.option_04 = "YouTube"
        self.option_05 = "Calendar"
        self.option_06 = "YouTube to MP3 or MP4"
        self.option_07 = "Alarm"
        self.option_08 = "Google Calendar"
        self.option_09 = "Dictionary & Thesaurus"  # Uses an API
        self.option_10 = "Flashcards"  # Uses an API
        self.option_11 = "AI Chatbot (Inbuilt)"  # Uses an API
        self.option_12 = "Notes"  # Uses an API
        self.option_13 = "Essay Structure Guide"
        self.option_14 = "Random Fact of the Day"  # Uses an API
        self.option_15 = "Math Solver"
        self.option_16 = "Terminal app wallpaper changer"
        self.option_17 = "Physics Formula Sheet"
        self.option_18 = "Spelling & Grammar Check"  # Uses an API
        self.option_19 = "Recommended Study Websites"

        # Additional menu options
        self.option_next = "Credits"
        self.option_site = "clear"
        self.option_info = "Help"
        self.options = \
        {
                '01': self.option_01, '02': self.option_02, '03': self.option_03, '04': self.option_04,
                '05': self.option_05, '06': self.option_06, '07': self.option_07, '08': self.option_08,
                '09': self.option_09, '10': self.option_10, '11': self.option_11, '12': self.option_12,
                '13': self.option_13, '14': self.option_14, '15': self.option_15, '16': self.option_16,
                '17': self.option_17, '18': self.option_18, '19': self.option_19,
        }
        BEFORE = f'{red}[{white}'
        AFTER = f'{red}]'
        INFO = f'{BEFORE}!{AFTER} |'
        menu_number = '1'  # menu number
        username_pc = os.getlogin()
        ERROR = f'{BEFORE}x{AFTER} |'# get pc name

        try:
            if sys.platform.startswith("win"):
                os_name = "Windows"
            elif sys.platform.startswith("linux"):
                os_name = "Linux"
            else:
                os_name = "Unknown"
        except:
            os_name = "???"  # Default value if the OS can't be determined
        # input from user
        choice = input(
            f""" {lc}┌──({purple}{username_pc}{lc}@cyan{lc})─{lc}[{red}~/{os_name}/Menu-{menu_number}{lc}]
 {lc}└─{lc}> {reset}""")
        # checks input e.g if input is c execute credits function
        try:
            if choice in ['C', 'credits', 'author', 'c', 'CREDITS', 'Credits', 'CreDIts']:
                credits()
                input(f"{BEFORE + self.current_time_hour() + AFTER} {INFO} Press enter to continue -> {reset} " + reset)
            if choice in ['Help', 'H', 'h', 'HELP', 'HeLp', '?', 'help']:
                #help()
                input(f"{BEFORE + self.current_time_hour() + AFTER} {INFO} Press enter to continue -> {reset} " + reset)
                self.continuemain()
            if choice in ['alt+f4', 'exit', 'leave', 'end', 'EXITAPP', 'exitapp']:
                sys.exit()
            if choice in ['R', 'r', 'reset', 'refresh', 'clear']:
                input(f"{BEFORE + self.current_time_hour() + AFTER} {INFO} Press enter to continue -> {reset} " + reset)
                os.system('cls')
                #self.main()
            # script path for all my modules
            script_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "features"))
            # execute option entered condition
            if choice in self.options and self.options[choice]:
                script_path = os.path.join(script_folder, f"{self.options[choice]}.py")

                if os.path.exists(script_path):
                    os.system(f"python \"{script_path}\"")
                    input(
                        f"{BEFORE + self.current_time_hour() + AFTER} {INFO} Press enter to continue -> {reset} " + reset)
                else:
                    print(f"{red}Error: {blue}{script_path} {red}not found! -_-")
                    input(f"{BEFORE + self.current_time_hour() + AFTER} {INFO} Press enter to continue -> {reset} " + reset)# if file not found

            elif '0' + choice in self.options and self.options['0' + choice]:  # if option entered starts with 0
                script_path = os.path.join(script_folder, f"{self.options['0' + choice]}.py")

                if os.path.exists(script_path):
                    os.system(f"python \"{script_path}\"")
                    input(
                        f"{BEFORE + self.current_time_hour() + AFTER} {INFO} Press enter to continue -> {reset} " + reset)
                else:
                    print(f"Error: {script_path} not found!")
                    input(f"{BEFORE + self.current_time_hour() + AFTER} {INFO} Press enter to continue -> {reset} " + reset)# if not found

            else:
                print(f"\n{BEFORE + self.current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
                time.sleep(0.5)

              # error
        # Prints error message e.g a filepath is not found in code or could not find a specific module.
        except Exception as e:
            input(f"Error: {e}")

