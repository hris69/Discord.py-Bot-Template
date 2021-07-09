""""
Copyright © Hris 2021 - https://github.com/hris69
Version: 1.0
"""
import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

intents = discord.Intents.all() # enables all intents this requires the two switches ticket at https://discord.com/developers
client = commands.Bot(command_prefix="your_prefix_here", intents=intents)
client.remove_command('help') # remove the default help command if you want a custom one

@client.event
async def on_ready():
    print(f"{client.user} has been started!") # if you want you can customize this
    
    
# for filename in os.listdir('./cogs'): - if you have cogs you can use this to load all your cogs in the cogs directory
   # if filename.endswith('.py'):
    #    client.load_extension(f'cogs.{filename[:-3]}') 

    
token = os.getenv("TOKEN") # gets the token for the .env file, secure your token with the dotenv library
client.run(token) # runs the bot with the given token
