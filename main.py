import pyarmor, json, asyncio, sys, requests, os, threading, time, yaml, random
import discord
from json import dumps
from colored import fg, attr

config = yaml.safe_load(open("config.yml"))["settings"]
text = config['status']
emoji = config['emoji']
emoji_id = config['emoji_id']
################################################
tokens = []
class colors:
  green = fg('#00FF00')
  pink = fg('#FF4DE1')
  gray = fg('#E6F0F5')
  red = fg('#EE4B2B')
  redd = fg('#FF0051')
  blue = fg('#0000FF')
def clear():
  if sys.platform in ["linux", "linux2"]:
    os.system("clear")
  else:
    os.system("cls")

with open("tokens.txt", "r") as f:
  tkns = f.read().split("\n")
if len(tkns) == 0:
  print(" They're are no tokens in tokens.txt")
  sys.exit()
  
def x(Token):
  response = requests.get(f"https://discord.com/api/v9/users/@me", headers={"Authorization": Token})
  if response.status_code in [204, 200, 201]:
    print(f"{colors.pink}[{colors.gray}>{colors.pink}] {colors.green}Valid | {colors.blue}{Token}{colors.gray}")
    tokens.append(Token)
  if "need to verify" in response.text:
    print(f"{colors.red}[!] PHONE LOCKED | {Token}")
  elif response.status_code in [404, 401, 400]:
    print(f"{colors.red}[~] Invaild | {Token}")

for tkn in tkns:
  x(tkn)
payload = {"text": text,"emoji_name": emoji, "emoji_id": int(emoji_id)}
xxx = random.choice(["online","dnd","idle"])

def antix(Token):
  headers = {"Authorization":Token,"content-type":"application/json"}
  r = requests.patch("https://discord.com/api/v9/users/@me/settings",headers=headers,json={"status": xxx, "custom_status": payload})
  
time.sleep(3)
clear()
loop = asyncio.get_event_loop()
clear()
for tkn in tokens:
  client = discord.Client()
  loop.create_task(client.start(tkn))
  huh = format(tkn)
  print(f"{colors.pink}[{colors.gray}>{colors.pink}] {colors.green}Connected : {colors.red}{huh}{colors.gray}")
threading.Thread(target=loop.run_forever).start()

while True:
  for x in tokens:
    antix(x)
