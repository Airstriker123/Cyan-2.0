import json
import requests
from style import *
import time

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
#get at aimlapi.com
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
