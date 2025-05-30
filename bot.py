import os
import discord
import requests
import json
from dotenv import load_dotenv

load_dotenv()  # Muat variabel dari file .env
TOKEN = os.getenv("DISCORD_TOKEN")

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
print("Semua environment:")
for k, v in os.environ.items():
    print(f"{k} = {v}")

client.run(TOKEN)
