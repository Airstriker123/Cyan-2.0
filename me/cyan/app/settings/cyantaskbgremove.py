import json
import os
import sys

'''Terminal app gif remove'''

image_path = os.path.abspath("").strip()
def change_windows_terminal_background(image_path):


        settings_path = os.path.expanduser(
            #default terminal path 
            r"~\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json")

        with open(settings_path, "r", encoding="utf-8") as file: #open file
            settings = json.load(file)


        default_profile_guid = settings.get("defaultProfile") 


        profiles_list = settings.get("profiles", {}).get("list", [])
        changed = False
        default_profile_found = False

           
        for profile in profiles_list: #change settings
            profile["backgroundImage"] = image_path
            profile["backgroundImageStretchMode"] = "uniformToFill"
            profile["backgroundImageOpacity"] = 0.8
            changed = True


            if profile.get("guid") == default_profile_guid:
                profile["backgroundImage"] = image_path
                default_profile_found = True


        if default_profile_found:
            settings["profiles"]["defaults"]["backgroundImage"] = image_path

        if changed:

            with open(settings_path, "w", encoding="utf-8") as file: # if success
                json.dump(settings, file, indent=4)

change_windows_terminal_background(image_path)
#
sys.exit()
