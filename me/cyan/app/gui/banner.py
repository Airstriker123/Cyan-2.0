try:
 from random import randint
 from os import system
 from me.cyan.app.gui.animations.style import *
except Exception as e:
    print(e)
    print('in: banner.py')
class Fade:
    def blackwhite(self, text):
        system("");
        faded = ""
        red = 0;
        green = 0;
        blue = 0
        for line in text.splitlines():
            faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
            if not red == 255 and not green == 255 and not blue == 255:
                red += 20;
                green += 20;
                blue += 20
                if red > 255 and green > 255 and blue > 255:
                    red = 255;
                    green = 255;
                    blue = 255
        return faded

    def purplepink(self, text):
        system("");
        faded = ""
        red = 40
        for line in text.splitlines():
            faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
            if not red == 255:
                red += 15
                if red > 255:
                    red = 255
        return faded

    def greenblue(self, text):
        system("");
        faded = ""
        blue = 100
        for line in text.splitlines():
            faded += (f"\033[38;2;0;255;{blue}m{line}\033[0m\n")
            if not blue == 255:
                blue += 15
                if blue > 255:
                    blue = 255
        return faded

    def pinkred(self, text):
        system("");
        faded = ""
        blue = 255
        for line in text.splitlines():
            faded += (f"\033[38;2;255;0;{blue}m{line}\033[0m\n")
            if not blue == 0:
                blue -= 20
                if blue < 0:
                    blue = 0
        return faded

    def purpleblue(self, text):
        system("");
        faded = ""
        red = 110
        for line in text.splitlines():
            faded += (f"\033[38;2;{red};0;255m{line}\033[0m\n")
            if not red == 0:
                red -= 15
                if red < 0:
                    red = 0
        return faded

    def water(self, text):
        system("");
        faded = ""
        green = 10
        for line in text.splitlines():
            faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
            if not green == 255:
                green += 15
                if green > 255:
                    green = 255
        return faded

    def fire(self, text):
        system("");
        faded = ""
        green = 250
        for line in text.splitlines():
            faded += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
            if not green == 0:
                green -= 25
                if green < 0:
                    green = 0
        return faded

    def brazil(self, text):
        system("");
        faded = ""
        red = 0
        for line in text.splitlines():
            faded += (f"\033[38;2;{red};255;0m{line}\033[0m\n")
            if not red > 200:
                red += 30
        return faded

    def random(self, text):
        system("");
        faded = ""
        for line in text.splitlines():
            for character in line:
                faded += (f"\033[38;2;{randint(0, 255)};{randint(0, 255)};{randint(0, 255)}m{character}\033[0m")
            faded += "\n"
        return faded


class banner(Fade):
    def __init__(self,
                 banner):
        self.banner = """    
                            ▄████▓██   ██▓▄▄▄      ███▄    █    ▄▄▄█████▓▒█████  ▒█████  ██▓    
                            ▒██▀ ▀█▒██  ██▒████▄    ██ ▀█   █    ▓  ██▒ ▓▒██▒  ██▒██▒  ██▓██▒    
                            ▒▓█    ▄▒██ ██▒██  ▀█▄ ▓██  ▀█ ██▒   ▒ ▓██░ ▒▒██░  ██▒██░  ██▒██░    
                            ▒▓▓▄ ▄██░ ▐██▓░██▄▄▄▄██▓██▒  ▐▌██▒   ░ ▓██▓ ░▒██   ██▒██   ██▒██░    
                            ▒ ▓███▀ ░ ██▒▓░▓█   ▓██▒██░   ▓██░     ▒██▒ ░░ ████▓▒░ ████▓▒░██████▒
                            ░ ░▒ ▒  ░██▒▒▒ ▒▒   ▓▒█░ ▒░   ▒ ▒      ▒ ░░  ░ ▒░▒░▒░░ ▒░▒░▒░░ ▒░▓  ░
                              ░  ▒ ▓██ ░▒░  ▒   ▒▒ ░ ░░   ░ ▒░       ░     ░ ▒ ▒░  ░ ▒ ▒░░ ░ ▒  ░
                            ░      ▒ ▒ ░░   ░   ▒     ░   ░ ░      ░     ░ ░ ░ ▒ ░ ░ ░ ▒   ░ ░   
                            ░ ░    ░ ░          ░  ░        ░                ░ ░     ░ ░     ░  ░
                            ░      ░ ░                                                                                                                             
    """

        Slow(self.greenblue(self.banner))



