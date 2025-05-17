import os
from pytubefix import YouTube #pytube for downloading videos
from pytubefix.cli import on_progress #pytube for downloading videos
from pydub import AudioSegment #pydub for mp3 videos
from style import *
import requests
import time


def Slow(text, delay=0.03):
    for line in text.split("\n"):
        print(line, flush=True)
        time.sleep(delay)


def MainColor2(text):
    start_color = (0, 200, 150)
    end_color = (0, 255, 255)

    num_steps = 16
    colors = [
        (
            start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1),
            start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1),
            start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1),
        )
        for i in range(num_steps)
    ]

    colors += list(reversed(colors[:-1]))

    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    result = []
    lines = text.split("\n")

    for i, line in enumerate(lines):
        color_index = i % len(colors)
        r, g, b = colors[color_index]
        colored_line = text_color(r, g, b) + line + "\033[0m"
        result.append(colored_line)

    return "\n".join(result)


yt = MainColor2(r"""                                                                                                      
                            ██████████████████████████████████████████████████                            
                          ██████████████████████████████████████████████████████                          
                         ████████████████████████████████████████████████████████                         
                        ██████████████████████████████████████████████████████████                        
                        ███████████████████████████████████████████████████████████                       
                       ████████████████████████████████████████████████████████████                       
                       ████████████████████████  ██████████████████████████████████                       
                       ████████████████████████     ███████████████████████████████                       
                       ████████████████████████         ███████████████████████████                       
                       ████████████████████████            ████████████████████████                       
                       ████████████████████████                ████████████████████                       
                       ████████████████████████             ███████████████████████                       
                       ████████████████████████          ██████████████████████████                       
                       ████████████████████████      ██████████████████████████████                       
                       ████████████████████████   █████████████████████████████████                       
                       ████████████████████████████████████████████████████████████                       
                       ████████████████████████████████████████████████████████████                       
                        ███████████████████████████████████████████████████████████                       
                        ██████████████████████████████████████████████████████████                        
                         █████████████████████████████████████████████████████████                        
                          ██████████████████████████████████████████████████████                          
                            ██████████████████████████████████████████████████                            

""")

# Create a folder for storing downloaded content if it doesn't exist
download_folder = "downloaded content"
os.makedirs(download_folder, exist_ok=True)

# Display the title or some introductory message
Slow(yt)

# Prompt the user to choose the type of content (mp3 or mp4) they wish to download
file_type = input(f'{yellow}What type of video do you wish to download (mp3/mp4): {white}')
url = input(f'{cyan}Enter URL of the video you want to download: {white}')

# Function to download the video in mp4 format
def mp4():
    try:
        # Initialize YouTube object and set up progress callback for download
        yt = YouTube(url, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True)
        print(f"Downloading: {yt.title}")
        ys = yt.streams.get_highest_resolution()  # Get the highest resolution stream
        ys.download(download_folder)  # Download the video to the 'downloaded content' folder
    except Exception as e:
        # If an error occurs during download, print the error message
        print(f"{red}Error: {e}")

# Function to download the audio as mp3 format
def mp3():
    try:
        # Initialize YouTube object and set up progress callback for download
        yt = YouTube(url, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True)
        print(f"Downloading Audio: {yt.title}")
        
        # Get the audio stream
        stream = yt.streams.filter(only_audio=True).first()

        if not stream:
            print(f"{red}No audio stream available.")  # If no audio stream found, notify user
            return

        # Download the audio stream temporarily
        temp_file = stream.download(download_folder)
        
        # Rename the downloaded file to have a '.mp3' extension
        mp3_file = os.path.join(download_folder, os.path.splitext(os.path.basename(temp_file))[0] + ".mp3")

        try:
            # Convert the audio file to mp3 using pydub
            audio = AudioSegment.from_file(temp_file, format="m4a")
            audio.export(mp3_file, format="mp3")
            os.remove(temp_file)  # Remove the temporary file
            print(f"{green}MP3/M4A downloaded! Check the {red}'downloaded content' folder.")
        except Exception as e:
            # Handle errors related to audio conversion
            print(f'{lc}ignore errors!')
    except Exception as e:
        # If an error occurs during download, print the error message
        print(f"{red}Error: {e}")

# Define headers for the HTTP request to make it look like a request from a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Make a request to the URL and check if it is accessible
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"{red}Error: Unable to access the URL. Please check the URL and try again.")  # URL is inaccessible
else:
    # If URL is accessible, proceed to download based on the user's choice
    if file_type.lower() in ['mp4', '2', 'mpfour', '4']:
        mp4()  # Call mp4 function to download the video
        print(f'\n{green}Video downloaded! Check the {lc}"downloaded content"{red} folder.')
    elif file_type.lower() in ['mp3', '1', 'mpthree', '3']:
        mp3()  # Call mp3 function to download the audio
        print(f'\n{green}MP3 downloaded! Check the {lc}"downloaded content"{red} folder.')
    else:
        print(f'An error occurred, most likely a network issue. Try using a different network.')

