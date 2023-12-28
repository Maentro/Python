#######################################
##         Made By xxxxzxxxz         ##
##     Creaton Date: 28.12.2023      ##
#######################################

import discord, json
from discord.ext import commands
from colorama import Fore, Style

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

YELLOW = Fore.YELLOW
WHITE = Style.RESET_ALL

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.CustomActivity(name=config["bot_status"]))
    print(f'{YELLOW}#######################################{WHITE}')
    print(f'{YELLOW}##        {WHITE}Made By xxxxzxxxz{YELLOW}          ##{WHITE}')
    print(f'{YELLOW}##     {WHITE}Creaton Date: 28.12.2023{YELLOW}      ##{WHITE}')
    print(f'{YELLOW}#######################################{WHITE}')
    

@bot.event
async def on_member_join(member):
    welcome_channel = bot.get_channel(config["welcome_channel_id"])
    if welcome_channel:
        embed = discord.Embed(
            title=f'Willkommen {member.display_name}!',
            description=f'Wir freuen uns, dich auf unserem Server zu haben.',
            color=discord.Colour.green()
        )
        await welcome_channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    leave_channel = bot.get_channel(config["leave_channel_id"])
    if leave_channel:
        embed = discord.Embed(
            title=f'Auf Wiedersehen {member.display_name}!',
            description=f'Schade, dass du den Server verlassen hast. Wir hoffen, dich bald wiederzusehen.',
            color=discord.Colour.red()
        )
        await leave_channel.send(embed=embed)

@bot.event
async def on_member_update(before, after):
    booster_role_id = config.get("booster_role")
    booster_channel_id = config.get("booster_channel")
    
    if booster_role_id and booster_channel_id:
        booster_role = discord.utils.get(after.roles, id=int(booster_role_id))
        booster_channel = bot.get_channel(booster_channel_id)
        
        if booster_role:
            if booster_role not in before.roles and booster_role in after.roles:
                embed = discord.Embed(
                    title=f'Server Boost',
                    description=f'Danke, dass du **{after.guild.name}** geboostet hast, {after.mention}!',
                    color=discord.Colour.pink()
                )
                await booster_channel.send(embed=embed)
                

bot.run(config["token"])
