from discord.ext import tasks
import datetime
from spotify_service import get_random_song
from config import CHANNEL_ID

def start_scheduler(client):

    @tasks.loop(time=datetime.time(hour=9, minute=0))
    async def daily_song():
        channel = client.get_channel(CHANNEL_ID)
        if channel:
            song = get_random_song()
            await channel.send(song)

    daily_song.start()
