import discord
from config import DISCORD_TOKEN
from scheduler import start_scheduler

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    start_scheduler(client)

client.run(DISCORD_TOKEN)
