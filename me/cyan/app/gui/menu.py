import os
try:
 from me.cyan.app.gui.animations.style import *
 from me.cyan.app.gui.animations.colorama.__init__ import *
except Exception as e:
    print(e)
    print('in: menu.py')

class Menu:
    def __init__(self):
        self.menu_path = os.path.join("me", "cyan", "app", "gui", "Menu.txt")

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
        self.option_20 = "Clear temp files"
        self.option_21 = "Empty Recycle Bin"
        self.option_22 = "Smart File Organizer"
        self.option_23 = "Auto website startup"
        self.option_24 = "Auto email (template)"
        self.option_25 = "Execute custom macros"
        self.option_26 = "Hardware Monitor (CLI HUD)"
        self.option_27 = "Port Scanner (Local)"
        self.option_28 = "Launch app (installed)"
        self.option_29 = "System info"
        self.option_30 = "Wifi Troubleshooter"
        self.option_31 = "shutdown computer"
        self.option_32 = "Ai dectector (ai percentage)"
        self.option_33 = "Google docs auto complete work (ai)"
        self.option_34 = "Smart Research Summarizer"


        # Additional menu options
        self.option_next = f"{green}Next"
        self.option_site = "Credits"
        self.option_back = f"{red}back"
        self.option_settings = f"{yellow}[Settings]"

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
        self.option_20_txt = f"{cyan}[{white}20{cyan}]{white} " + self.option_20
        self.option_21_txt = f"{cyan}[{white}21{cyan}]{white} " + self.option_21
        self.option_22_txt = f"{cyan}[{white}22{cyan}]{white} " + self.option_22
        self.option_23_txt = f"{cyan}[{white}23{cyan}]{white} " + self.option_23
        self.option_24_txt = f"{cyan}[{white}24{cyan}]{white} " + self.option_24
        self.option_25_txt = f"{cyan}[{white}25{cyan}]{white} " + self.option_25
        self.option_26_txt = f"{cyan}[{white}26{cyan}]{white} " + self.option_26
        self.option_27_txt = f"{cyan}[{white}27{cyan}]{white} " + self.option_27
        self.option_28_txt = f"{cyan}[{white}28{cyan}]{white} " + self.option_28
        self.option_29_txt = f"{cyan}[{white}29{cyan}]{white} " + self.option_29
        self.option_30_txt = f"{cyan}[{white}30{cyan}]{white} " + self.option_30
        self.option_31_txt = f"{cyan}[{white}31{cyan}]{white} " + self.option_31
        self.option_32_txt = f"{cyan}[{white}32{cyan}]{white} " + self.option_32
        self.option_33_txt = f"{cyan}[{white}33{cyan}]{white} " + self.option_33
        self.option_34_txt = f"{cyan}[{white}34{cyan}]{white} " + self.option_34

        # Formatting special options
        self.option_next_txt = self.option_next + f" {cyan}[{green}N{cyan}]{white}"
        self.option_site_txt = f"{cyan}[{yellow}C{cyan}]{white} " + self.option_site
        self.option_back_txt= f"{cyan}[{red}B{cyan}]{white} " + self.option_back
        self.option_settings_txt= f"{cyan}[{yellow}S{cyan}]{white} " + self.option_settings


        # menu display

        self.ribbon = "┃┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃┃"
        self.menu1 = f""" ┌─{self.option_site_txt}                                                                                              {self.option_next_txt}─┐
 ├─{self.option_back_txt  }  ┌─────────────────┐                        ┌───────┐                           ┌───────────┐            │ 
 └─┬─────────┤ General tools   ├─────────┬──────────────┤ Study ├──────────────┬────────────┤ Utilities ├────────────┴─┃
   │         └─────────────────┘         │              └───────┘              │            └───────────┘
   ├─ {self.option_01_txt                }├─ {self.option_07_txt                }├─ {self.option_14_txt}
   ├─ {self.option_02_txt                }├─ {self.option_08_txt                }├─ {self.option_15_txt}
   ├─ {self.option_03_txt                }├─ {self.option_09_txt                }├─ {self.option_16_txt}
   ├─ {self.option_04_txt                }├─ {self.option_10_txt                }├─ {self.option_17_txt}
   ├─ {self.option_05_txt                }├─ {self.option_11_txt                }├─ {self.option_18_txt}
   └─ {self.option_06_txt                }├─ {self.option_12_txt                }└─ {self.option_19_txt}
                                         └─ {self.option_13_txt                }
{self.ribbon}                                     """

        self.menu2 = f"""█┣━{self.option_back_txt}                                                                                                  {self.option_next_txt}┣━█
┃                                                                                                                      ┃
┗━░█░───────┤{purple}[Automation]├────────░█░────────┤{red}[System tools]├─────────░█░────────┤{orange}[Ai tools]├──────────────░█░━━━━━━━━━░
   ┃                               ┃                                   ┃                                               █
   ┣━${self.option_20_txt}        ┣━{self.option_26_txt}   ┃                                               ┃
   ┣━${self.option_21_txt}       ┣━{self.option_27_txt}         ┗━━━█────────────────────────────#{self.option_settings_txt}┛
   ┣━${self.option_22_txt}    ┣━{self.option_28_txt}           ┃
   ┣━${self.option_23_txt}    ┣━{self.option_29_txt}                      ┣━{self.option_32_txt}
   ┣━${self.option_24_txt}   ┣━{self.option_30_txt}              ┣━{self.option_33_txt}
   ┣━${self.option_25_txt}   ┣━{self.option_31_txt}                ┣━{self.option_34_txt}
{self.ribbon}        
"""
        self.menu_number = self.menu1
        with open (self.menu_path, "r") as file:
           self.menu_number = file.read()
           if self.menu_number == "1":
                   self.menu_number = self.menu1
           elif self.menu_number == "2":
                   self.menu_number = self.menu2
           else:
                   self.menu_number = self.menu1



























