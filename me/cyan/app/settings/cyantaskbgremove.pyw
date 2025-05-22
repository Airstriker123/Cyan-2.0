import json
import os
import sys
import subprocess
import time
import sys
try:
    import pygetwindow as gw
except:
    print('IGNORE BACKGROUND PROCESS!')
    print('This terminal will close on its own!')
    os.system('pip install pygetwindow')
    import pygetwindow as gw


'''Terminal app gif remove'''

image_path = os.path.abspath("").strip()
def change_windows_terminal_background(image_path):

        settings_path = os.path.expanduser(
            # default terminal path
            r"~\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json")

        with open(settings_path, "r", encoding="utf-8") as file:  # open file
            settings = json.load(file)

        default_profile_guid = settings.get("defaultProfile")

        profiles_list = settings.get("profiles", {}).get("list", [])
        changed = False
        default_profile_found = False

        for profile in profiles_list:  # change settings
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
            with open(settings_path, "w", encoding="utf-8") as file:  # if success
                json.dump(settings, file, indent=4)

import subprocess
import time


def is_script_running(script_name: str) -> bool:
    """Check if a specific Python script is running by inspecting command lines."""
    try:
        output = subprocess.check_output(
            'wmic process where "name=\'python.exe\'" get CommandLine',
            shell=True
        ).decode()

        return script_name.lower() in output.lower()
    except Exception as e:
        print(f"Error: {e}")
        return False


while True:
    if "Cyan2.0" in [w.title for w in gw.getWindowsWithTitle("Cyan2.0")]:
        print("The script cyan.py is running!")
    else:
        print("cyan.py is NOT running!")
        print("Cyan remove task!")
        change_windows_terminal_background(image_path)
        break

    time.sleep(3)  # Wait before checking again



sys.exit()



