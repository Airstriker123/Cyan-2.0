import json
import requests
from colors_app import *
import time

# API KEYS CONTAINED
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


dic = MainColor2(r"""
             ████████                                         █████████            
             ███████████████                           ████████████████            
             ███████████████████                   ████████████████████            
          █  ██████████████████████              ██████████████████████  █         
       █  █  ████████████████████████         █████████████████████████  █  █      
       █  █  ████       ███████████████     █████████████████       ███  █  █      
       █  █  █████████        ███████████  ███████████    ███  ████████  █  █      
       █  █  ████████████████     ███████  ████████     ███████████████  █  █      
       █  █  ████        ███████    █████  █████    ████████        ███  █  █      
       █  █  ████████         █████  ████  ████  █████         ████████  █  █      
       █  █  ████████████████    ████████  ████████     ███████████████  █  █      
       █  █  ████     ███████████   █████  █████    ██████████     ████  █  █      
       █  █  ████████████    ██████   ███  ████  ██████       █████████  █  █      
       █  █  ████████████████    ████████  ████████     ███████████████  █  █      
       █  █  ████         ██████    █████  █████    ███████         ███  █  █      
       █  █  ██████████        ████  ████  ████  ████         █████████  █  █      
       █  █  ████████████████     ███████  ███████     ████████████████  █  █      
       █  █  ████           █████    ████  █████   ██████           ███  █  █      
       █  █  █████████████      ████ ████  ████  ████     █████████████  █  █      
       █  █  ██████████████████    ██████  ███████ ██ █████████████████  █  █      
       █  █  █████████████████████   ████  █████  █████████████████████  █  █      
       █  █  ████████████████████████████  ████████████████████████████  █  █      
       █  █  ████████████████████████████  ████████████████████████████  █  █      
       █  █                ██████████████  ██████████████                █  █      
       █  ███████████████      ██████████  ██████████      ███████████████  █      
       █                  ████    ███████  ██████     ███                   █      
       █    ███████████              ████  ████              ██████████    ██      
       █████████████████████████       ██  ██       █████████████████████████      
       █████████████████████████████           ██████████████████████████████      
       ████████████████████████████████     █████████████████████████████████      
                                        █ ██                                       
                                                                                   
                                                                                   


""")
# do not show these keys!
api_keys = {
    "",
    "",
    "",
    "",
    "",
    "",
}

api_url = "https://api.aimlapi.com/v1/chat/completions"
#define sends prompt to ai asking what it means
# fastest and best way to create this
define = "What does this word mean?"
thesaurus = "Also what give a thesaurus of the word"
def send_message(user_message):
    if not user_message:
        print("Error: No message entered.")
        return

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": f"{define}  {user_message} {thesaurus}"} #prompt
        ]
    }
# cycles through keys
    for api_key in api_keys:
        try:
            response = requests.post(api_url, headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }, data=json.dumps(payload))

            #error handle
            data = response.json()

            if data and "choices" in data:
                ai_message = data["choices"][0]["message"]["content"]
                print(f"{cyan}Personal Dictionary🤖:",  f"{white}{ai_message}")
                break  # Exit loop if the request is successful
            else:
                print(f"{red}Error: Unable to retrieve response. Trying next API key. (you used all tokens)")
                print(f"{red}Switching to the next API key, please wait... (you used all tokens)")

        except requests.exceptions.RequestException as error:
            print(f"Error: Unable to connect with API key {api_key}. {error}")
            print( f"{red}Attempting to use the next available API key...")


# rest
#main function
def Personal_Dictionary():
    Slow(dic)
    print(
        f'{green}Remember to type{red} exit{green} once you have completed your prompts')
    while True:
        user_input = input(f"{yellow}\b👨‍💻Enter the word you want to search: ")
        if user_input.lower() == "exit":
            print(f'{red}Exiting program.')
            break
        send_message(user_input)


Personal_Dictionary()
