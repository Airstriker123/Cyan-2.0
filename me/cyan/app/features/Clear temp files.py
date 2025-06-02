import os
import sys
try:
    from style import *
    import shutil
    import tempfile
    import ctypes
    import winshell
except:
    pass

class CleanUp:
    def __init__(self
                 ):
        user = os.getlogin()
        self.user_temp = f"C:\\Users\\{user}\\AppData\\Local\\Temp"
        self.user_downloads = f"C:\\Users\\{user}\\Downloads\\"
        self.temp_dirs = None
        self.recycle_bin = False  # flag to optionally clear Recycle Bin
        self.banner =  MainColor2(
"""                                                                                                    
                                  ░░▒▓▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒░░                                             
                                 ░░▒▓▒▒▒▒▓▒▒▒▓▒▒▓▓█▒▒▓░                                             
                                  ░░░▓▓▓▒▒▒▒▓▒▒▒░░▓▒░░░░                                            
                                      ░▓▓▓▓▒▒▒▒▒▓▓▓░                                                
                                      ░░▓▓▒▒▒▒▓▒▓▓▒▓░                                               
                                       ░▓▓▒▒▒▒█░░░▓▒░                                               
                                      ░░▓▒░░░▒█░░░░▒▒░░                                             
                        ░░░░░░░░░░░░░░░░▓▓▓▓▓▓▒▓░ ░░░▓░░                                            
                     ░░▒▓▒▒▒▒░░░░░░░░▓░░▒▓░░░░░▓░ ░░ ░░░▒▒░░                                        
                    ░▒▓█▓▓▓▓▓▓▓▓▓▓▒░▒░░▒░▒░░░░░▒░    ░▓▓▒▓▓▒░                                       
                    ▒▒▓▒▒▓░░░░░░░░░░░░▒▒▒▒░░░░░▒▓  ░░▓▒░░▒▓▓░░░                                     
                   ░░▓▓█▓█▓▒░░▒░░░░░▒▒▓░▓▒░░░░░░░░░░▒▓▒▒░▒▓▓▓░░░                                    
                     ░░█▓▒▓▓██▓░░░░░▓▒░░▓▒░░░░░▓░░░▒▓▒░░░░▒▒▓▓░░                                    
                     ░▒░▒▒▒░░░█▓▓▒▒▓█░░▒▒▒░░░░▒▒░░░▓▒▒░░░░▒▓▒▓░░                                    
                    ░▓▒▒▒▒░░░░█▒▒░▒██▒░▓▓░░░░░░▒▒░▒▒▒░░▒▒░▒▒▓▓█▒░                                   
                  ░░░░▒▓▒ ░ ░░▓▓▒▒▒▒▓▓▒▒▒░░░░░░▒▓▒░░░░░░ ░▒▒▒▓▓█▒░░                                 
                  ░▒░▒░░    ░▓░░░▒░░▒▓▓▒▒░▒▒░░▒▒▒░░░      ░░░▒▓▓█▓░░                                
                    ░░░     ▒▒░░▒▒░░░▓▓▒░▒░   ▒▓▒░▒░       ░░▒▒▒▒▓░░░                               
                          ░░▓░░▒▒░░░░▒▓▒▒░░  ░▓▒▒▒▒▒▒▒▒▒▒▒░▒▒░░▒▒▓▓░░                               
                          ░▒▒░░▒░░░░░▒▓█░   ░░▒░▒░▒▒▒▒▒▒▒░▒░░░░░▒▒█░░                               
                          ░▓░░▒░░░░░░▒▓▓▒░░░░▒▓▒▒░░       ░░  ░░▒▒█░░                               
                          ░█░░▒░░ ░░░ ░░░▒▒░▒▓▓▓▒░░           ░░▒▒▓░                                
                          ░▓░▓░░  ░░░░░░░░░▒▓▓▒▒░░░░           ░▒▒▓░░                               
                         ░▒▒░▒░░   ░░░░░░░▒░▒▓▓░░░▒░░        ░░▒▒▒▓░                                
                         ░▒░░░░░░░░░░░░░░░▒▒░▒▓░░░▒░░        ░▒░▒▒▒░                                
                      ░░▒▒▒░░░░▒░░░░░░░░▒░░░▒▒▓░░░░░░░░  ░░░ ░░▒░▒▒░░                               
                      ░▒▓░░░░░▒░ ░▒▒▒░░░ ░▒░▒▒▓▒░▒░  ░░  ░░   ░░▒▒░░░                               
                      ░▓▒░░░▒░░ ░░░░░░░  ░░▒▒▒▓▒░▒░    ░░░░░  ░░░▓░░░                               
                      ░▒░░░▓░░░░░░░░░░░░░░░░░▓█▒░▒░    ░░░░░   ░░▓░░░                               
                     ░▒▒░░▒░▒░░░░░░░▒░░░░░░░░░█░░▒░      ░░░░░░░░▒░░░                               
                     ░▒▓▓░▒▓░░░░░░░░   ░░░░░ ░▓░░▒▒░░░░░▒▒▒▒▒▓▓▒▒▓░░         ░                      
                    ░░▒░▒▒▒▒▒▒▒░░░░░   ░░░░░ ░▓░░▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▓░░░░░░░░░▒▒░▒░                    
                  ░░▒░▒▒▒▓▒▒  ░░▒▓▒▒░░░     ░▒▓░░▒░░░░░░░░░░░░░░▒▓▒▒▒▒░░░░░░░░▓░░                   
              ░░░▒▒▓▒▓▓▓▒▒░░   ░░░░▒▒▓▒░░▒▒░▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░▒▒░░                    
              ░░▒▓▒▓▓▒▒▒░            ░░▓▒▓▓▒▓▓▓▓▒░░░░░░░░  ░░░░░░░░░░░░░▒▒▓▒░▒▒░░░                  
             ░░▓▒░█▓▒▒░░               ░░▒▓░░░░░░░░░░░░░▒░░░░░░░░░░░░░▒▓░▒▒▓▓▒▒▒▒░░░░               
          ░░░▓▓▒▓▓▒░░░░        ░░░░░░░░░░░░░▒░░░░░░    ░░▒▒░   ░░░░▒▒░░░▒░░░░░░░▒▓▓░░░░             
        ░░░░▒▒▒▓▒░░░         ░░░░░░░░░░▒▒▒░░░░▒▒░ ░░░░░░░░░▒░░░▒▒░▒▒▒▒▒▓▓▒▒░░░░░▒▒▓▓▒▒▒▒░░          
     ░░░░▒▒▒▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░▓███▓▓▒▒░░░▒░░▒▓▓▓▓▒▒░▒▒▒▒▒▒▒▒░░░░░░░░░▒░░░         
    ░░░░░░░░░▓▒░    ░░░░░     ░░░░░      ░░▒▒▓░░░▒▒▓▓▓▒░░░░░░░░░ ░░░░░░░░░░░   ░░░▒▒▒▒▓▓▒░░         
      ░░░░▒▒▒▒█▓▒░░ ░░░      ░░░           ░░░▓▓▒░░▒▓▒▒▓▓▒░░▒░░    ░░░░░░░░░░░░▒▓▓▓▓█▓▓▒░░░         
       ░░░░▒░▒▓▓█▓▒░░░░░░    ░░░ ░░░   ░░░░   ░░▒▒░░░░▒░░░░░░▒▓▓▒▒░░░░░░░░░░░░░░░░░░░▒▒░░░░░        
         ░░░░░░▒▒▓▓▓▒░░░░      ░░░▒▒░  ░░░░░░░░░ ░░▒░░░░▒▒░░     ░▒▒▓▓▓▓▓▒▒▒░░░░░░▒▒▒▓▒░░░░         
           ░░░░▒▒░▒░░▒▒▒▒▒░░░░░  ░▒░▒▒░░░░░░░░░░░░░░▒▒░░░░░▒░░░░       ░░░░░▒███████▓▓▒▒░░          
             ░░░░░░░░░▒▒▒▒▓█▓▒░░░  ░░░░░░░░░░░░   ░░░░▒▓░░░░▓▓▓▒░░░░▒▒▒░░░░░▒▒░░░▒░░░░░             
                    ░░░░░░░░░░▓▓▒░░   ░░░░░░░░░░░  ░░░░░▓▓▒▒▓▒░░  ░░░░░░░░░░▒▒▒░░▒░░░░              
                      ░░░░░░░░░░░▒▒▒░░░   ░░ ░░░░▒▒▒░░░░░▒▒▓▓▒▒▒▒▒▒▒░░░░░░░░░▒░░░░░                 
                          ░░░░░▒░░░▒▒▒▒░ ░░      ░░░░▒▒▒░░░          ░▒▒▒▒▒▒▓▒░░░░                  
                            ░░░░░▒▒░░░░▒▒▒░░░░░  ░░░░░░░▒▓▒░░░░░░░░░░░░▒▓▓▒▒▒▒░░░░                  
                                 ░░░░░░░░░░▒▓▒░░░ ░░░▒░░░░▓▓▓▓▓▒▒▒▒▒▒▓█▒░▒░░░░                      
                                       ░░░░░░░░▒▒▓▒▒▒▒▒▒▓▓▓▒░░▒▒▓▓▒▓▓▒▓▒▒░░                         
                                           ░░░░░░░░░░▒▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░                           
                                                  ░░░░░░ ░░░░░░                                                                                                                                               
""")

    def delete_options(self):
        choice = input(Slow(f"""
{red}[!] WARNING THIS IS NOT REVERSIBLE
{yellow}Choice what to cleanup:
{green}[1] Temp folder 
{red}[2] Tempfolder + Downloads folder (careful if you have important files)
{red}[3] Tempfolder + Downloads + Recylce-bin
{yellow}[4] Tempfolder + Recycle-bin  
        
{lc}Your choice:->{red}""")).lower()

        if choice in ["1", 'one']:
            self.temp_dirs = [
                tempfile.gettempdir(),
                r'C:\Windows\Temp',
                f'{self.user_temp}',
            ]
        elif choice in ["2", 'two']:
            confirm = input(f'{yellow}Are you sure? [y/n]').lower()
            if confirm in ['y', 'yes']:
                self.temp_dirs = [
                    tempfile.gettempdir(),
                    r'C:\Windows\Temp',
                    f'{self.user_temp}',
                    f'{self.user_downloads}'
                ]
            else:
                print(f'{red}Failed to delete...')
        elif choice in ["3", 'three']:
            confirm = input(f'{yellow}Are you sure? [y/n]').lower()
            if confirm in ['y', 'yes']:
                self.recycle_bin = False
                self.temp_dirs = [
                    tempfile.gettempdir(),
                    r'C:\Windows\Temp',
                    f'{self.user_temp}',
                    f'{self.user_downloads}'
                ]
            else:
                print(f'{red}Failed to delete...')
        elif choice in ["4", "four"]:
            confirm = input(f'{yellow}Are you sure? [y/n]').lower()
            if confirm in ['y', 'yes']:
                self.recycle_bin = True
                self.temp_dirs = [
                    tempfile.gettempdir(),
                    r'C:\Windows\Temp',
                    f'{self.user_temp}',
                    f'{self.user_downloads}'
                ]
            else:
                print(f'{red}Failed to delete...')


        else:
            print(f'{red}Invalid choice!')


    def delete_files_in_dir(self, folder_path):
        if not os.path.exists(folder_path):
            print(f"{yellow}Directory not found: {folder_path}")
            return

        for root, dirs, files in os.walk(folder_path):
            for name in files:
                file_path = os.path.join(root, name)
                try:
                    os.remove(file_path)
                    Slow(f"{green}Deleted file: {yellow}{file_path}{reset}")
                except Exception as e:
                    Slow(f"{red}Failed to delete {blue}{file_path}{red}: {e}")
            for name in dirs:
                dir_path = os.path.join(root, name)
                try:
                    shutil.rmtree(dir_path)
                    Slow(f"{green}Deleted folder: {dir_path}")
                except Exception as e:
                    Slow(f"{red}Failed to delete folder {dir_path}: {e}")

    def empty_recycle_bin(self):
        try:
            ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 1)
            Slow(f"{green}Recycle Bin emptied.")
        except Exception as e:
            Slow(f"{red}Failed to empty Recycle Bin: {e}")

    def cleanup(self):
        Slow(f"{purple}Starting cleanup...")

        for folder in self.temp_dirs:
            Slow(f"{yellow}Cleaning: {folder}")
            self.delete_files_in_dir(folder)

        if self.recycle_bin:
            Slow(f"{yellow}Emptying Recycle Bin...")
            self.empty_recycle_bin()

        Slow(f"{lc}Cleanup completed!")



    @staticmethod
    def main():
        Clean = CleanUp()
        Slow(CleanUp().banner)
        Clean.delete_options()
        Clean.cleanup()
        if recycling_bin:
            Slow(f'{lc}Emptying recycle bin')
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            Slow(f'{green}Done!')

CleanUp().main()

