import os, ctypes
from time import sleep
import json
try:
    import requests
    import colorama
    from colorama import Fore
except (ModuleNotFoundError):
    os.system('pip install colorama, requests')


clear = lambda: os.system('cls')
colorama.init(autoreset=True)

clear()
ctypes.windll.kernel32.SetConsoleTitleW("WebhookLyrics 1.1")
lyrics = open('lyrics.txt').read().split('\n')

with open('config.json') as config_file:
    cfg = json.load(config_file)

print(f'{Fore.CYAN}Input your webhook url')
url = input('> ')


for line in lyrics:
    payload = {
        'username': cfg['username'],
        'avatar_url': cfg['avatar_url'],
        'content': line,
        'tts': False
    }
    req = requests.post(url, data=payload)
    if req.status_code == 204:
        print('Sent a new message')
        sleep(0.6)
clear()
print(f'{Fore.CYAN}Finished spamming')