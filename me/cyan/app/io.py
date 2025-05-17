try:
    import os
    import sys
    from me.cyan.app.gui.animations.colorama.__init__ import *
    from me.cyan.app.gui.animations.style import *
    import datetime
    import time
    import requests
except Exception as e:
    print(e)
    print('in: io.py')



class Credits:
        def __init__(self):
            self.show_credits()
        # function to submit feedback.



        def show_credits(self):
            Slow(f'''
{lc}
╭────────────────────────────────╮
│ Cyan - Multi-tool for Students │
╰────────────────────────────────╯
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Developed by: {red}Airstriker{lc}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Lead Developer: {red}Airstriker{lc}
• GitHub: {cyan}github.com/Airstriker123 🚀{lc}
• Design & UX: {red}Airstriker {lc}
• Programming: {red}Airsriker {lc}
• Tested on {purple}3{lc} computers 💯
┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ {purple}Modules Used{lc}   ┃{purple} Use{lc}                                      ┃ {purple}Link{lc}                                            ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ colorama       │ Color support for console text           │ https://pypi.org/project/colorama/              │
│ pytubefix      │ Download YouTube videos (patched pytube) │ https://github.com/fent/node-ytdl-core          │
│ pydub          │ Audio processing (conversion, editing)   │ https://github.com/jiaaro/pydub                 │
│ ffmpeg         │ Multimedia processing (audio/video)      │ https://ffmpeg.org/                             │
│ imageio        │ Read/write images & videos               │ https://imageio.readthedocs.io/                 │
│ fade           │ Adds fading effects to text in CLI       │ https://pypi.org/project/fade/                  │
│ Flask          │ Web framework for Python                 │ https://flask.palletsprojects.com/              │
│ requests       │ Handles HTTP requests                    │ https://docs.python-requests.org/               │
│ rich           │ Better CLI app, tables, text formatting  │ https://github.com/Textualize/rich              │
│ PyExecJS       │ Run JavaScript from Python               │ https://pypi.org/project/PyExecJS/              │
│ datetime       │ Handles date and time operations         │ https://docs.python.org/3/library/datetime.html │
│ simplejson     │ Extended JSON handling                   │ https://pypi.org/project/simplejson/            │
│ jsons          │ Serialize/deserialize JSON data          │ https://pypi.org/project/jsons/                 │
│ pypi-json      │ Retrieve package metadata from PyPI      │ https://pypi.org/project/pypi-json/             │
│ textblob       │ NLP (Natural Language Processing)        │ https://pypi.org/project/textblob/              │
│ pyspellchecker │ Spell checking in Python                 │ https://pypi.org/project/pyspellchecker/        │
│ sympy          │ Symbolic mathematics library             │ https://www.sympy.org/                          │
└────────────────┴──────────────────────────────────────────┴─────────────────────────────────────────────────┘

{lc}Thank you for using Cyan! 
{green}Be sure to Star this project on Github!

            ''')




class AppIo(object
):
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
        except Exception as e:
            print(f'{red}error:{purple} {e}')  # Default value if the OS can't be determined
        # input from user
        choice = (input
(
            f""" {lc}┌──({purple}{username_pc}{lc}@cyan2.0{lc})─{lc}[{red}~/{os_name}/Menu-{menu_number}{lc}]
 {lc}└─{lc}> {reset}""").lower()
)
        # checks input e.g if input is c execute credits function
        try:
            if choice in ['c', 'credits', 'creds']:
                Credits()
                input(f"{BEFORE + self.current_time_hour() + AFTER} {INFO} Press enter to continue -> {reset} " + reset)
                return
            if choice in ['Gui', 'gui','swap', 'enable_gui', 'exec_gui', "g"]:
                print(f'{purple}FEATURE IS NOT OUT YET AND STILL IN DEVELOPMENT')
                input(f"{BEFORE + self.current_time_hour() + AFTER} {INFO} Press enter to continue -> {reset} " + reset)
                self.continuemain()
                return
            if choice in ['alt+f4', 'exit', 'leave', 'end', 'EXITAPP', 'exitapp']:
                sys.exit()
                return
            if choice in ['R', 'r', 'reset', 'refresh', 'clear']:
                input(f"{BEFORE + self.current_time_hour() + AFTER} {INFO} Press enter to continue -> {reset} " + reset)
                if os_name == "Windows":
                    os.system("cls")
                elif os_name == "Linux":
                    os.system("clear")
                return
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
               time.sleep(0.69)

              # error
        # Prints error message e.g a filepath is not found in code or could not find a specific module.
        except Exception as e:
            input(f"Error: {e}")
