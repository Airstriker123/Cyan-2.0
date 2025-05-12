from me.cyan.app.gui.animations.style import *
from me.cyan.app.gui.animations.colorama.__init__ import *

class Menu:
    def __init__(self,
                 menu1
):
        option_01 = "Google-Classroom"  # 1
        option_02 = "ChatGPT (Web-Version)"  # @
        option_03 = "GitHub"  ##@
        option_04 = "YouTube"
        option_05 = "Calendar"
        option_06 = "YouTube to MP3 or MP4"
        option_07 = "Alarm"
        option_08 = "Google Calendar"
        option_09 = "Dictionary & Thesaurus"  # Uses an API
        option_10 = "Flashcards"  # Uses an API
        option_11 = "AI Chatbot (Inbuilt)"  # Uses an API
        option_12 = "Notes"  # Uses an API
        option_13 = "Essay Structure Guide"
        option_14 = "Random Fact of the Day"  # Uses an API
        option_15 = "Math Solver"
        option_16 = "Terminal app wallpaper changer"
        option_17 = "Physics Formula Sheet"
        option_18 = "Spelling & Grammar Check"  # Uses an API
        option_19 = "Recommended Study Websites"

        # Additional menu options
        option_next = "Credits"
        option_site = "clear"
        option_info = "Help"

        # Formatting the options for display in the menu
        # Using ANSI color codes (cyan and white) to style the text
        option_01_txt = f"{cyan}[{white}01{cyan}]{white} " + option_01.ljust(30)[:30].replace("-", " ")
        option_02_txt = f"{cyan}[{white}02{cyan}]{white} " + option_02.ljust(30)[:30].replace("-", " ")
        option_03_txt = f"{cyan}[{white}03{cyan}]{white} " + option_03.ljust(30)[:30].replace("-", " ")
        option_04_txt = f"{cyan}[{white}04{cyan}]{white} " + option_04.ljust(30)[:30].replace("-", " ")
        option_05_txt = f"{cyan}[{white}05{cyan}]{white} " + option_05.ljust(30)[:30].replace("-", " ")
        option_06_txt = f"{cyan}[{white}06{cyan}]{white} " + option_06.ljust(30)[:30].replace("-", " ")
        option_07_txt = f"{cyan}[{white}07{cyan}]{white} " + option_07.ljust(30)[:30].replace("-", " ")
        option_08_txt = f"{cyan}[{white}08{cyan}]{white} " + option_08.ljust(30)[:30].replace("-", " ")
        option_09_txt = f"{cyan}[{white}09{cyan}]{white} " + option_09.ljust(30)[:30].replace("-", " ")
        option_10_txt = f"{cyan}[{white}10{cyan}]{white} " + option_10.ljust(30)[:30].replace("-", " ")

        option_11_txt = f"{cyan}[{white}11{cyan}]{white} " + option_11.ljust(30)[:30].replace("-", " ")
        option_12_txt = f"{cyan}[{white}12{cyan}]{white} " + option_12.ljust(30)[:30].replace("-", " ")
        option_13_txt = f"{cyan}[{white}13{cyan}]{white} " + option_13.ljust(30)[:30].replace("-", " ")
        option_14_txt = f"{cyan}[{white}14{cyan}]{white} " + option_14.ljust(30)[:30].replace("-", " ")
        option_15_txt = f"{cyan}[{white}15{cyan}]{white} " + option_15.ljust(30)[:30].replace("-", " ")
        option_16_txt = f"{cyan}[{white}16{cyan}]{white} " + option_16.ljust(30)[:30].replace("-", " ")
        option_17_txt = f"{cyan}[{white}17{cyan}]{white} " + option_17.ljust(30)[:30].replace("-", " ")
        option_18_txt = f"{cyan}[{white}18{cyan}]{white} " + option_18.ljust(30)[:30].replace("-", " ")
        option_19_txt = f"{cyan}[{white}19{cyan}]{white} " + option_19.ljust(30)[:30].replace("-", " ")

        # Formatting special options
        option_next_txt = option_next + f" {cyan}[{white}C{cyan}]{white}"
        option_site_txt = f"{cyan}[{white}R{cyan}]{white} " + option_site
        option_info_txt = f"{cyan}[{white}H{cyan}]{white} " + option_info

        # menu display
        self.menu1 = f""" ┌─{option_site_txt}                                                                                             {option_next_txt}─┐
 ├─{option_info_txt      }  ┌─────────────────┐                        ┌───────┐                           ┌───────────┐            │
 └─┬─────────┤ General tools   ├─────────┬──────────────┤ Study ├──────────────┬────────────┤ Utilities ├────────────┴─
   │         └─────────────────┘         │              └───────┘              │            └───────────┘
   ├─ {option_01_txt                    }├─ {option_07_txt                    }├─ {option_14_txt}
   ├─ {option_02_txt                    }├─ {option_08_txt                    }├─ {option_15_txt}
   ├─ {option_03_txt                    }├─ {option_09_txt                    }├─ {option_16_txt}
   ├─ {option_04_txt                    }├─ {option_10_txt                    }├─ {option_17_txt}
   ├─ {option_05_txt                    }├─ {option_11_txt                    }├─ {option_18_txt}
   └─ {option_06_txt                    }├─ {option_12_txt                    }└─ {option_19_txt}
                                         └─ {option_13_txt                    }

            """


menu_instance = Menu(None)



