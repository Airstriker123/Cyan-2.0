try:
 from me.cyan.app.gui.animations.style import *
 from me.cyan.app.gui.animations.colorama.__init__ import *
except Exception as e:
    print(e)
    print('in: menu.py')

class Menu:
    def __init__(self,
                 menu1
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

        # Formatting the options for display in the menu
        # Using ANSI color codes (cyan and white) to style the text
        self.option_01_txt = f"{cyan}[{white}01{cyan}]{white} " + self.option_01.ljust(30)[:30].replace("-", " ")
        self.option_02_txt = f"{cyan}[{white}02{cyan}]{white} " + self.option_02.ljust(30)[:30].replace("-", " ")
        self.option_03_txt = f"{cyan}[{white}03{cyan}]{white} " + self.option_03.ljust(30)[:30].replace("-", " ")
        self.option_04_txt = f"{cyan}[{white}04{cyan}]{white} " + self.option_04.ljust(30)[:30].replace("-", " ")
        self.option_05_txt = f"{cyan}[{white}05{cyan}]{white} " + self.option_05.ljust(30)[:30].replace("-", " ")
        self.option_06_txt = f"{cyan}[{white}06{cyan}]{white} " + self.option_06.ljust(30)[:30].replace("-", " ")
        self.option_07_txt = f"{cyan}[{white}07{cyan}]{white} " + self.option_07.ljust(30)[:30].replace("-", " ")
        self.option_08_txt = f"{cyan}[{white}08{cyan}]{white} " + self.option_08.ljust(30)[:30].replace("-", " ")
        self.option_09_txt = f"{cyan}[{white}09{cyan}]{white} " + self.option_09.ljust(30)[:30].replace("-", " ")
        self.option_10_txt = f"{cyan}[{white}10{cyan}]{white} " + self.option_10.ljust(30)[:30].replace("-", " ")

        self.option_11_txt = f"{cyan}[{white}11{cyan}]{white} " + self.option_11.ljust(30)[:30].replace("-", " ")
        self.option_12_txt = f"{cyan}[{white}12{cyan}]{white} " + self.option_12.ljust(30)[:30].replace("-", " ")
        self.option_13_txt = f"{cyan}[{white}13{cyan}]{white} " + self.option_13.ljust(30)[:30].replace("-", " ")
        self.option_14_txt = f"{cyan}[{white}14{cyan}]{white} " + self.option_14.ljust(30)[:30].replace("-", " ")
        self.option_15_txt = f"{cyan}[{white}15{cyan}]{white} " + self.option_15.ljust(30)[:30].replace("-", " ")
        self.option_16_txt = f"{cyan}[{white}16{cyan}]{white} " + self.option_16.ljust(30)[:30].replace("-", " ")
        self.option_17_txt = f"{cyan}[{white}17{cyan}]{white} " + self.option_17.ljust(30)[:30].replace("-", " ")
        self.option_18_txt = f"{cyan}[{white}18{cyan}]{white} " + self.option_18.ljust(30)[:30].replace("-", " ")
        self.option_19_txt = f"{cyan}[{white}19{cyan}]{white} " + self.option_19.ljust(30)[:30].replace("-", " ")

        # Formatting special options
        self.option_next_txt = self.option_next + f" {cyan}[{white}C{cyan}]{white}"
        self.option_site_txt = f"{cyan}[{white}R{cyan}]{white} " + self.option_site
        self.option_info_txt = f"{cyan}[{white}H{cyan}]{white} " + self.option_info

        # menu display
        self.menu1 = f""" ┌─{self.option_site_txt}                                                                                             {self.option_next_txt}─┐
 ├─{self.option_info_txt  }  ┌─────────────────┐                        ┌───────┐                           ┌───────────┐            │
 └─┬─────────┤ General tools   ├─────────┬──────────────┤ Study ├──────────────┬────────────┤ Utilities ├────────────┴─
   │         └─────────────────┘         │              └───────┘              │            └───────────┘
   ├─ {self.option_01_txt                }├─ {self.option_07_txt                }├─ {self.option_14_txt}
   ├─ {self.option_02_txt                }├─ {self.option_08_txt                }├─ {self.option_15_txt}
   ├─ {self.option_03_txt                }├─ {self.option_09_txt                }├─ {self.option_16_txt}
   ├─ {self.option_04_txt                }├─ {self.option_10_txt                }├─ {self.option_17_txt}
   ├─ {self.option_05_txt                }├─ {self.option_11_txt                }├─ {self.option_18_txt}
   └─ {self.option_06_txt                }├─ {self.option_12_txt                }└─ {self.option_19_txt}
                                         └─ {self.option_13_txt                }
"""








