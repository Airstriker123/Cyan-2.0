try:
    from me.cyan.app.gui.banner import *
    from me.cyan.app.features import *
    from me.cyan.app.settings import *
    from me.cyan.app.gui.menu import Slow, MainColor, menu_instance

except: print('error: failed to import modules')

class Main:
    def __init__(self,

):
        #construct app
        banner(Fade)
        Slow(MainColor(menu_instance.menu1))
        input('')





    def main(self,
): #burner fucntion no purpose
        pass


Main()
