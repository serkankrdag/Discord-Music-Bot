import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

client = commands.Bot(command_prefix="!") # Bot prefix'i ayarlayın

@client.event
async def on_ready():
    print("Bot hazır.")

@client.command()
async def play(ctx, url):
    voice_channel = ctx.author.voice.channel
    if voice_channel is None:
        await ctx.send("Bir ses kanalında değilsiniz.")
        return
    vc = await voice_channel.connect()
    vc.play(discord.FFmpegPCMAudio(url))
    while vc.is_playing():
        await asyncio.sleep(1)
    await vc.disconnect()

client.run("BOT_TOKEN") # Bot token'ınızı girin
