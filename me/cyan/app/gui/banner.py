try:
 from random import randint
 from os import system
 from me.cyan.app.gui.animations.style import *
except Exception as e:
    print(e)
    print('in: banner.py')

class Fade:
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


class Banner(Fade):
    def __init__(self):
        self.banner = [
            "┃┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃┃",
            "┃┃         *     ░      ░        *       ░             ░       *              ░            ░       ░       *          ┃┃",
            "┃┃   * ░            *       ▄████▓██   ██▓▄▄▄      ███▄    █    ▄▄▄█████▓▒█████  ▒█████  ██▓           *              ┃┃",
            "┃┃       ░                 ▒██▀ ▀█▒██  ██▒████▄    ██ ▀█   █    ▓  ██▒ ▓▒██▒  ██▒██▒  ██▓██▒        ░         ░    *  ┃┃",
            "┃┃           ░    *    ░   ▒▓█    ▄▒██ ██▒██  ▀█▄ ▓██  ▀█ ██▒   ▒ ▓██░ ▒▒██░  ██▒██░  ██▒██░       *       ░          ┃┃",
            "┃┃    *        ░           ▒▓▓▄ ▄██░ ▐██▓░██▄▄▄▄██▓██▒  ▐▌██▒   ░ ▓██▓ ░▒██   ██▒██   ██▒██░         *  *      * ░    ┃┃",
            "┃┃      ░        *   ░     ▒ ▓███▀ ░ ██▒▓░▓█   ▓██▒██░   ▓██░     ▒██▒ ░░ ████▓▒░ ████▓▒░██████▒    *     ░           ┃┃",
            "┃┃       ░      ░          ░ ░▒ ▒  ░██▒▒▒ ▒▒   ▓▒█░ ▒░   ▒ ▒      ▒ ░░  ░ ▒░▒░▒░░ ▒░▒░▒░░ ▒░▓  ░       *       *  ░   ┃┃",
            "┃┃     ░                    ░  ▒ ▓██ ░▒░  ▒   ▒▒ ░ ░░   ░ ▒░    *  ░     ░ ▒ ▒░  ░ ▒ ▒░░ ░ ▒  ░     *     ░           ┃┃",
            "┃┃     ░       ░ *         ░      ▒ ▒ ░░   ░   ▒     ░   ░ ░      ░     ░ ░ ░ ▒ ░ ░ ░ ▒   ░ ░          ░     *   ░  ░ ┃┃",
            "┃┃                        ░ ░    ░ ░          ░  ░        ░   *   *        ░ ░     ░ ░     ░  ░     *    ░      *  *  ┃┃",
            "┃┃         ░               ░      ░ ░                       ░             ░    ░                 *        ░      ░    ┃┃",
            "┃┃       *            *         ░                  ░      ░       * ░        ░  ░   *              *                  ┃┃",
            "┃┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃┃"
        ]

        # Convert list to multiline string
        full_banner = "\n".join(self.banner)

        # Apply effect and print slowly
        Slow(self.greenblue(full_banner))














