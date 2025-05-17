try:
    from me.cyan.app.gui.banner import *
    from me.cyan.app.features import *
  #  from me.cyan.app.settings import *
    from me.cyan.app.gui.menu import Menu, Slow
    from me.cyan.app.io import AppIo
#catch module load error
except Exception as e:
    print(f'error: {e}')
    print('In: Cyan.py')

import os

#main class
class Main:
    '''
    Executes all other modules to open and display app gui (banner, menu)
    and also executes the backend of application io.py to handle input/output
    - No further use unless major changes
    - Only change code if adding something new to pre execution without user needing to input
    - If added it will execute when app is opened.
    '''
    def main(self,
):
        while True:
            os.system('cls')
            menu_instance = Menu(None)
            banner(Fade)
            Slow(MainColor(menu_instance.menu1))
            AppIo(object)

#call main function when class is called
    def __init__(self,
):
        self.main()

Main(
    #run app
)
