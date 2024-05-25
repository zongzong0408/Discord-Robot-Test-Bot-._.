import discord as dc
from discord.ext import commands
from core import Cog_Extension

class trigger(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):
            
        Help = ["Help", "help", "H", "h"]
        Commands = ["./help"]

        for words in Help:
            if msg.content.find(words) >= 0 and msg.author != self.bot.user and msg.content not in Commands:

                await msg.channel.send("pls input ***./help*** to see more information.")
                
                break

def setup(bot):
    bot.add_cog(trigger(bot))