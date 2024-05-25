import discord
from discord.ext import commands
import os  

TOKEN = "your bot's token"

bot = commands.Bot(command_prefix ="./")

@bot.event
async def on_ready():
    print("robot : Bot is online...")

for FileName in os.listdir('./cmds'):
    if FileName.endswith('.py'):
        bot.load_extension(f'cmds.{FileName[:-3]}')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded')

if  __name__ == "__main__":
    bot.run(TOKEN)
