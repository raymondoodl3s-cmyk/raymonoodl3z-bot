import os
import datetime
from twitchio.ext import commands
from database import setup, get_user
import economy
import song_requests
import ai_module

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=os.getenv("TMI_TOKEN"),
            prefix="!",
            initial_channels=[os.getenv("CHANNEL")]
        )
        self.start_time = datetime.datetime.now()

    async def event_ready(self):
        print(f"Logged in as {self.nick}")
        await setup()

    async def event_message(self, message):
        if message.echo:
            return

        await get_user(message.author.name)
        await self.handle_commands(message)

        if "raymonoodl3zbot-2.0" in message.content.lower():
            ctx = await self.get_context(message)
            await ai_module.ai_reply(ctx, message.content)

    @commands.command()
    async def points(self, ctx):
        user = await get_user(ctx.author.name)
        await ctx.send(f"{ctx.author.name} has {user[1]} coins 💰")

    @commands.command()
    async def daily(self, ctx):
        await economy.daily(ctx)

    @commands.command()
    async def gamble(self, ctx, amount: int):
        await economy.gamble(ctx, amount)

    @commands.command()
    async def steal(self, ctx, amount: int, target: str):
        await economy.steal(ctx, amount, target.replace("@",""))

    @commands.command()
    async def song(self, ctx, *, query):
        await song_requests.add_song(ctx, query=query)

    @commands.command()
    async def queue(self, ctx):
        await song_requests.show_queue(ctx)

bot = Bot()
bot.run()
