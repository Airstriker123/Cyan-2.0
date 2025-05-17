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
    '''Brings app together prints frontend (banner, menu)
    and also executes io script to manage input/output from user.

   - No further use
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
