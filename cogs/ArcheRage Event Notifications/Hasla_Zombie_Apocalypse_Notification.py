import pytz
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.combining import AndTrigger

from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from discord import Embed

from main import event_pings
from main import allow_ping_role

class _HaslaZombies(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.scheduler = AsyncIOScheduler(timezone=pytz.timezone('US/Eastern'))
        self.scheduler.start()
        Merchants_Day = AndTrigger(
            [CronTrigger(hour=20, minute=44, day_of_week='mon,tue,wed,thu,sun', timezone=pytz.timezone('US/Eastern'))])
        self.scheduler.add_job(self.send_message, Merchants_Day)

    async def send_message(self):
        channel = self.client.get_channel(int(event_pings))  # replace with your channel ID
        embed = Embed(title="Hasla Zombie Apocalypse", description="Starts in`15`Minutes!",
                      color=0x00FF00)
        embed.set_image(url="https://i.ibb.co/C1y4Lp4/Hasla.png")
        embed.set_thumbnail(
            url="https://1000logos.net/wp-content/uploads/2020/09/ArcheAge-logo.png")
        embed.add_field(
            name="Event Details",
            value="https://na.archerage.to/forums/threads/game-event-hasla-zombie-apocalypse.4536/")

        self.client.loop.create_task(channel.send(f"<@&{allow_ping_role}>",embed=embed))

    @commands.Cog.listener()
    async def on_ready(self):
        print("_HaslaZombies Loaded")
        self.scheduler.start()


async def setup(client):
    await client.add_cog(_HaslaZombies(client))
