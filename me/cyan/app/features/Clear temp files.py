import os
try:
    from style import *
except:
    pass

class CleanUp:

    def cleanup(self):
        '''function to clear temp files'''
        Slow(f'{red}cleaning up!')
        print('n/a')
    def __init__(self
                 ):
        self.banner =  MainColor2("""
        PENNIS
        """)

    @staticmethod
    def main():
        Slow(CleanUp().banner)
        CleanUp().cleanup()



CleanUp().main()

