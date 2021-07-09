""""
Copyright © Hris 2021 - https://github.com/hris69
Version: 1.0
"""
import discord
from discord.ext import commands


class class_name_here(commands.Cog, name="name here"): # create a class for the cog
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command() # IMPORTANT: indent your command right under the init otherwise it doesn't work
    async def test(self, ctx): # always do a self in a class or cog
          await ctx.send("cog is working")


def setup(bot):
    bot.add_cog(class_name_here(bot)) # add the cog to your bot
    print("Example Cog has been loaded!") # if you want you can print something when the cog is loaded
