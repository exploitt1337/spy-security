import os
os.system("pip install dhooks")
os.system("pip install requests")
import datetime
import requests
os.system("pip install discord-buttons-plugin")
from discord_buttons_plugin import  *
os.system("pip install discord-py-slash-command")
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashCommand, SlashContext
import time 
from dhooks import Webhook, Webhook
#os.system("pip install aiohttp")
import aiohttp
os.system("pip install logging")
import logging
from discord.ext import commands
from discord.ext.commands import MissingPermissions
os.system("pip install colorama")
import colorama
os.system("pip install colored")
from colored import fg, attr
# os.system("pip install tasksio")
# import colorama
# from colorama import Fore
# import threading
# import json
# import asyncio
# import time 
# import datetime
# import random
# from discord.ext import commands, tasks 
# from tasksio import TaskPool 
# import concurrent.futures
# import os
# os.system("pip install discord_buttons_plugin")
# os.system("pip install discord.py dismusic")
# os.system("pip install discord-py-slash-command")
#os.system("pip install enhanced-dpy")
#os.system("pip install py-cord")
import discord
from discord import Client, Intents, Embed
# import colorama
# import discord
# import asyncio
# import requests
# from time import strftime
# from discord.utils import find
# from discord_buttons_plugin import *
# from discord_slash import *
# import time
# import datetime
# from discord.ext.commands import Greedy
# from typing import Union
# from cogs.idk import idk

class colors:

    main = fg('#00fefc')
    reset = attr('reset')
logging.basicConfig(
    level=logging.INFO,
    format=
    f"{colors.main}[{colors.reset}%(asctime)s{colors.main}] \033[0m%(message)s",
    datefmt="%H:%M:%S",
)
logging.info("STARTED SUCCESSFULLY")
logging.info("STARTED SUCCESSFULLY")
logging.info("STARTED SUCCESSFULLY")
logging.info("STARTED SUCCESSFULLY")
logging.info("STARTED SUCCESSFULLY")
logging.info("STARTED SUCCESSFULLY")
logging.info("STARTED SUCCESSFULLY")
logging.info("STARTED SUCCESSFULLY")

token = os.environ["noo"]
prefix = "_"
shards = 1


intents = discord.Intents.default()
intents.members = True
intents.messages = True
headers = {'Authorization': f'Bot {token}'}
client = commands.AutoShardedBot(shard_count=shards, command_prefix=commands.when_mentioned_or(prefix), case_insensitive=False, intents=intents)
client.remove_command('help')
slash = SlashCommand(client, sync_commands=True)
buttons = ButtonsClient(client)

client.lava_nodes = [

    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'idk',
        'region': 'singapore'
    }

]
@client.event
async def on_ready():
    logging.info('''
    Spy security is ready :P  
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P  
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P
    Spy security is ready :P    
 ''')

    servers = len(client.guilds)
  #  members = 0
   # for guild in client.guilds:
     #   members += guild.member_count - 1

    await client.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'_help | /help | {servers} servers'
    ))
    
listofids = []
for guild in client.guilds:
  listofids.append(guild.id)

@slash.slash(
  name="Help",
  description="Shows Help command",
  guild_ids=listofids
)
async def _help(ctx:SlashContext):
  embed = discord.Embed(title="<a:spy_cyan_crown:894150074567909406>Help Menu<a:spy_cyan_crown:894150074567909406>", description="[Invite](https://dsc.gg/spy-sec)\n[Support](https://discord.gg/XDzUVexw4d)", color=2303786)
  #embed = discord.Embed(color=2303786)
  embed.set_author(name="Spy Security")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
  embed.set_footer(text=f"RisinPlayZ :P | Shards:  {shards} | Active Threads: 404 | Proxied: False", icon_url=ctx.author.avatar_url)
 # embed.add_field(name="<a:spy_cyan_crown:894150074567909406>Help Menu<a:spy_cyan_crown:894150074567909406>", value='[Invite](https://dsc.gg/spy-sec)\n[Support](https://discord.gg/XDzUVexw4d)')
  embed.add_field(name="<:spy_announcements:894201296700211290>Help", value='```"Shows Help command"```', inline=False)
  embed.add_field(name="<:spy_announcements:894201296700211290>Features", value='```"shows features of the bot"```', inline=False)
  embed.add_field(name="<:spy_announcements:894201296700211290>Invite", value='```"sends an invite link to add the bot"```', inline=False)
  embed.add_field(name="<:spy_announcements:894201296700211290>Commands", value='```"shows the list of executable commands."```', inline=False)
  embed.add_field(name="<:spy_announcements:894201296700211290>Ping", value='```"shows the bot latency"```', inline=False)
  embed.add_field(name="<:spy_announcements:894201296700211290>Stats", value='```"shows the bot stats"```', inline=False)

  await ctx.reply(embed=embed)

@slash.slash(
    name="Features",
    description="Shows features of the bot",
    guild_ids=listofids
)
async def _features(ctx:SlashContext):
  embed = discord.Embed(color=2303786)
  embed.set_author(name="Features")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
  embed.set_footer(text=f"RisinPlayZ :P | Shards:  {shards} | Active Threads: 404 | Proxied: False", icon_url=ctx.author.avatar_url)

  embed.add_field(name="__**<:spy_bug_hunter_black:915206652502872095>Offense Threshold**__", value='1', inline=False)
  embed.add_field(name="__**<:spy_staff:915205782461624390>Punishment Type**__", value='Ban-Persist', inline=False)
  embed.add_field(name="__**<:spy_sec_op:889811467002576906>Security Status**__", value='Enabled', inline=False)
  embed.add_field(name="__**<a:spy_load:915206162629161000>Auto recovery**__", value='Enabled', inline=False)
  embed.add_field(name="<:spy_rules:894150396094865418>Features", value='''```
1; Anti Prune
2; Anti Bot Auth
3; Anti Server Update
4; Anti Member Roles Update
5; Anti Member Removal
6; Anti Unban
7; Anti Channel Create/Delete/Update
8; Anti Role Create/Delete/Update
9; Anti Emoji Delete
10; Anti Sticker Delete
11; Anti Invite Delete
12; Anti Webhook Create
13; Anti Integration
14; Anti Selfbot
15; Anti Everyone / Here```''', inline=False)
  embed.add_field(name="__**<a:spy_verified_black:915207311683907615>Whitelisted**__", value='Server Owner', inline=False)
  
  await ctx.reply(embed=embed)
@slash.slash(
    name="Commands",
    description="Shows the list of executable commands",
    guild_ids=listofids
)
async def _commands(ctx:SlashContext):
  embed = discord.Embed(title="Spy Security | <:slash:920014228197359656> Commands: 3", color=2303786)
  embed.set_author(name="Spy Security")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
  embed.set_footer(text=f"Note: The commands are server owner only.", icon_url=ctx.author.avatar_url)
 # embed.add_field(name="<a:spy_cyan_crown:894150074567909406>Help Menu<a:spy_cyan_crown:894150074567909406>", value='[Invite](https://dsc.gg/spy-sec)\n[Support](https://discord.gg/XDzUVexw4d)')
  embed.add_field(name="<:spy_staff:915205782461624390> Massunban", value='```"Unbans all banned users, aliases - unbanall"```', inline=False)
  embed.add_field(name="<:spy_staff:915205782461624390> Lockserver", value='```"Revokes dangerous perms from all roles, aliases - lockroles"```', inline=False)
  embed.add_field(name="<:spy_staff:915205782461624390> Cleanchannels", value='```"Deletes channel with similar names, aliases - cc"```', inline=False) 
  embed.add_field(name="<:spy_staff:915205782461624390> Lock", value='```"Locks the channel"```', inline=False) 
  embed.add_field(name="<:spy_staff:915205782461624390> Unlock", value='```"Unlocks the channel"```', inline=False) 
  embed.add_field(name="<:spy_staff:915205782461624390> Hide", value='```"Hides the channel"```', inline=False) 
  embed.add_field(name="<:spy_staff:915205782461624390> Unhide", value='```"Unhides the channel"```', inline=False) 
  await ctx.reply(embed=embed)

@slash.slash(
    name="Invite",
    description="sends an invite link to add the bot",
    guild_ids=listofids
)
async def _invite(ctx:SlashContext):
    embed = discord.Embed(color=2303786, description="\n[+] [Invite Spy Security](https://discord.com/oauth2/authorize?client_id=794061930054418483&permissions=8&scope=bot%20applications.commands)\n[+] [Join support server](https://discord.gg/XDzUVexw4d)\n[+] [Vote the bot on top.gg](https://top.gg/bot/794061930054418483/vote)")
    await ctx.reply(embed=embed)
    await buttons.send(
        content = None,
        embed = embed,
        channel = ctx.channel.id,
        components = [
            ActionRow([
                Button(
                    style = ButtonType().Link,
                    label = "Invite",
                    url = f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot%20applications.commands"
                )
            ])                                  
        ]
    )
@slash.slash(
    name="Ping",
    description="shows the bot latency",
    guild_ids=listofids
)
async def _ping(ctx:SlashContext):
      await ctx.reply(f"**Latency is `{int(client.latency * 1000)}` ms**")
@slash.slash(
    name="Channel Cleaner",
    description="Deletes channel with similar names",
    guild_ids=listofids
)  
async def channelclean(ctx:SlashContext, channeltodelete:SlashContext):
  guild = ctx.guild
  if ctx.author == guild.owner:
    embed = discord.Embed(color=2303786)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="RisinPlayZ :P | Channel Deleter")
    embed.add_field(name="<a:spy_success:919998568041971782>SUCCESS", value=f'```"Successfully Deleted channel with the name {channeltodelete}"```')
    await ctx.reply(embed=embed)
    for channel in ctx.message.guild.channels:
            if channel.name == channeltodelete:
                try:
                    await channel.delete()
                except:
                  pass    
  else:
    embed = discord.Embed(color=2303786)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="RisinPlayZ :P | Error")
    embed.add_field(name="<a:spy_error:916265786195206194>FAILED", value=f'```"You must be guild owner to use this command."```')
    await ctx.reply(embed=embed)    
@slash.slash(
    name="Stats",
    description="shows the bot stats",
    guild_ids=listofids
)
async def _stats(ctx:SlashContext):
    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1
    embed = discord.Embed(color=2303786)
    embed.set_author(name="STATS")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="RisinPlayZ :P | Stats")
    embed.add_field(name="__**<a:spy_crush:879375067132338246>Servers**__", value=f'{servers}')
    embed.add_field(name="__**<a:spy_crush:879375067132338246>Members**__", value=f'{members}')
    await ctx.reply(embed=embed)
    

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def stats(ctx):
    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1
    embed = discord.Embed(color=2303786)
    embed.set_author(name="STATS")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="RisinPlayZ :P | Stats")
    embed.add_field(name="__**<a:spy_crush:879375067132338246>Servers**__", value=f'{servers}')
    embed.add_field(name="__**<a:spy_crush:879375067132338246>Members**__", value=f'{members}')
    await ctx.reply(embed=embed)
@client.command(aliases=["settings"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def features(ctx):
  embed = discord.Embed(color=2303786)
  embed.set_author(name="Features")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
  embed.set_footer(text=f"RisinPlayZ :P | Shards:  {shards} | Active Threads: 404 | Proxied: False", icon_url=ctx.author.avatar_url)

  embed.add_field(name="__**<:spy_bug_hunter_black:915206652502872095>Offense Threshold**__", value='1', inline=False)
  embed.add_field(name="__**<:spy_staff:915205782461624390>Punishment Type**__", value='Ban-Persist', inline=False)
  embed.add_field(name="__**<:spy_sec_op:889811467002576906>Security Status**__", value='Enabled', inline=False)
  embed.add_field(name="__**<a:spy_load:915206162629161000>Auto recovery**__", value='Enabled', inline=False)
  embed.add_field(name="<:spy_rules:894150396094865418>Features", value='''```
1; Anti Prune
2; Anti Bot Auth
3; Anti Server Update
4; Anti Member Roles Update
5; Anti Member Removal
6; Anti Unban
7; Anti Channel Create/Delete/Update
8; Anti Role Create/Delete/Update
9; Anti Emoji Delete
10; Anti Sticker Delete
11; Anti Invite Delete
12; Anti Webhook Create
13; Anti Integration
14; Anti Selfbot
15; Anti Everyone / Here```''', inline=False)
  embed.add_field(name="__**<a:spy_verified_black:915207311683907615>Whitelisted**__", value='Server Owner', inline=False)
  
  await ctx.reply(embed=embed)

@client.event 
async def on_command_error(ctx, error): 
    embed = discord.Embed(color=2303786)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="RisinPlayZ :P | Error")
    embed.add_field(name="<a:spy_error:916265786195206194>FAILED", value=f'```"{error}"```')
    await ctx.reply(embed=embed)

@client.command(aliases=["inv", "support", "vote"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def invite(ctx):
    embed = discord.Embed(color=2303786, description="\n[+] [Invite Spy Security](https://discord.com/oauth2/authorize?client_id=794061930054418483&permissions=8&scope=bot%20applications.commands)\n[+] [Join support server](https://discord.gg/XDzUVexw4d)\n[+] [Vote the bot on top.gg](https://top.gg/bot/794061930054418483/vote)")
    await buttons.send(
        content = None,
        embed = embed,
        channel = ctx.channel.id,
        components = [
            ActionRow([
                Button(
                    style = ButtonType().Link,
                    label = "Invite",
                    url = f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot%20applications.commands"
                )
            ])                                  
        ]
    )

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def help(ctx):
  embed = discord.Embed(title="<a:spy_cyan_crown:894150074567909406>Help Menu<a:spy_cyan_crown:894150074567909406>", description="[Invite](https://dsc.gg/spy-sec)\n[Support](https://discord.gg/XDzUVexw4d)", color=2303786)
  embed.set_author(name="Spy Security")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
  embed.set_footer(text=f"RisinPlayZ :P | Shards:  {shards} | Active Threads: 404 | Proxied: False", icon_url=ctx.author.avatar_url)
 # embed.add_field(name="<a:spy_cyan_crown:894150074567909406>Help Menu<a:spy_cyan_crown:894150074567909406>", value='[Invite](https://dsc.gg/spy-sec)\n[Support](https://discord.gg/XDzUVexw4d)')
  embed.add_field(name="<:spy_announcements:894201296700211290>Help", value='```"Shows Help command"```', inline=False)
  embed.add_field(name="<:spy_announcements:894201296700211290>Features", value='```"shows features of the bot"```', inline=False)
  embed.add_field(name="<:spy_announcements:894201296700211290>Invite", value='```"sends an invite link to add the bot"```', inline=False)
  embed.add_field(name="<:spy_announcements:894201296700211290>Commands", value='```"shows the list of executable commands."```', inline=False)
  embed.add_field(name="<:spy_announcements:894201296700211290>Ping", value='```"shows the bot latency"```', inline=False)
  embed.add_field(name="<:spy_announcements:894201296700211290>Stats", value='```"shows the bot stats"```', inline=False)
  await ctx.reply(embed=embed)
@client.command(aliases=["commands"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def lolucantseeidkok(ctx):
  embed = discord.Embed(title="Spy Security | <:slash:920014228197359656> Commands: 3", color=2303786)
  embed.set_author(name="Spy Security")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
  embed.set_footer(text=f"Note: The commands are server owner only.", icon_url=ctx.author.avatar_url)
 # embed.add_field(name="<a:spy_cyan_crown:894150074567909406>Help Menu<a:spy_cyan_crown:894150074567909406>", value='[Invite](https://dsc.gg/spy-sec)\n[Support](https://discord.gg/XDzUVexw4d)')
  embed.add_field(name="<:spy_staff:915205782461624390> Massunban", value='```"Unbans all banned users, aliases - unbanall"```', inline=False)
  embed.add_field(name="<:spy_staff:915205782461624390> Lockserver", value='```"Revokes dangerous perms from all roles, aliases - lockroles"```', inline=False)
  embed.add_field(name="<:spy_staff:915205782461624390> Cleanchannels", value='```"Deletes channel with similar names, aliases - cc"```', inline=False) 
  embed.add_field(name="<:spy_staff:915205782461624390> Unlock", value='```"Unlocks the channel"```', inline=False) 
  embed.add_field(name="<:spy_staff:915205782461624390> Hide", value='```"Hides the channel"```', inline=False) 
  embed.add_field(name="<:spy_staff:915205782461624390> Unhide", value='```"Unhides the channel"```', inline=False) 
  await ctx.reply(embed=embed)
@client.command(aliases=["lockroles"])
@commands.cooldown(1, 60, commands.BucketType.user)
async def lockserver(ctx):
  guild = ctx.guild
  if ctx.author == guild.owner:
    embed = discord.Embed(color=2303786)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="RisinPlayZ :P")
    embed.add_field(name="<a:spy_success:919998568041971782>SUCCESS", value=f'```"Revoking Perms from every role..."```')
    await ctx.reply(embed=embed)
    for role in ctx.guild.roles:
        perms = discord.Permissions()
        perms.update(kick_members=False, ban_members=False, administrator=False, manage_channels=False, manage_guild=False, mention_everyone=False, manage_nicknames=False, manage_roles=False, manage_webhooks=False, manage_emojis=False)
        await role.edit(permissions=perms, reason="Spy Security | Action Issued by Server Owner")
  else:
    embed = discord.Embed(color=2303786)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="RisinPlayZ :P | Error")
    embed.add_field(name="<a:spy_error:916265786195206194>FAILED", value=f'```"You must be guild owner to use this command."```')
    await ctx.reply(embed=embed)
 
    
@client.command(aliases=["massunban"])
@commands.cooldown(1, 60, commands.BucketType.user)
async def unbanall(ctx):
  guild = ctx.guild
  banlist = await guild.bans()
  idk = 'SPY SECURITY | Unbanning {} members'.format(len(banlist))
  if ctx.author == guild.owner:
    embed = discord.Embed(color=2303786)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="RisinPlayZ :P | Mass Unban")
    embed.add_field(name="<a:spy_success:919998568041971782>SUCCESS", value=f'```"{idk}"```')
    await ctx.reply(embed=embed)
    for users in banlist:
            await ctx.guild.unban(user=users.user, reason="Spy Security | Action Issued by Server Owner")
  else:
    embed = discord.Embed(color=2303786)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="RisinPlayZ :P | Error")
    embed.add_field(name="<a:spy_error:916265786195206194>FAILED", value=f'```"You must be guild owner to use this command."```')
    await ctx.reply(embed=embed)

@client.command(aliases=["cc"])
async def channelclean(ctx, channeltodelete):
  guild = ctx.guild
  if ctx.author == guild.owner:
    embed = discord.Embed(color=2303786)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="RisinPlayZ :P | Channel Deleter")
    embed.add_field(name="<a:spy_success:919998568041971782>SUCCESS", value=f'```"Successfully Deleted channel with the name {channeltodelete}"```')
    await ctx.reply(embed=embed)
    for channel in ctx.message.guild.channels:
            if channel.name == channeltodelete:
                try:
                    await channel.delete()
                except:
                  pass    
  else:
    embed = discord.Embed(color=2303786)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png")
    embed.set_footer(text="RisinPlayZ :P | Error")
    embed.add_field(name="<a:spy_error:916265786195206194>FAILED", value=f'```"You must be guild owner to use this command."```')
    await ctx.reply(embed=embed)
@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
  if channel == None:
    channel = ctx.channel
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(f'<a:spy_success:919998568041971782> | <#{channel.id}> has been locked.')

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
  if channel == None:
    channel = ctx.channel
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(f'<a:spy_success:919998568041971782> | <#{channel.id}> has been unlocked.')
@client.command()
@commands.has_permissions(manage_channels=True)
async def hide(ctx, channel : discord.TextChannel=None):
  if channel == None:
    channel = ctx.channel
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.read_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(f'<a:spy_success:919998568041971782> | <#{channel.id}> is now hidden from the default role.')
loghook = Webhook("https://discord.com/api/webhooks/921243432381464586/d2CMJ-1DWTy11-1s9Fw2UPbUBDoiiQzL6qrKeB3NOcAFqEFW3HZ8rMEqUvvvDnz2NOd2")
@client.event
async def on_guild_join(guild):
  log_channel = client.get_channel(891982975141556244)
  channel = guild.text_channels[0]
  invlink = await channel.create_invite(unique = True)
  embed = discord.Embed(title='Spy Security', color=0x2f3136, description=f'Joined New Server!')
  embed.add_field(name='Server Name', value=f'**`{guild.name}`**')
  embed.add_field(name='Server Owner', value=f'**`{guild.owner}`**')
  embed.add_field(name='Server Members', value=f'**`{len(guild.members)}`**') 
  embed.add_field(name="Server ID", value=f"**`{guild.id}`**")
  embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png')
  embed.add_field(name = "Link Of Server" , value = f'{invlink}')
  await loghook.send(embed=embed)
  servers = len(client.guilds)
 # members = 0
 # for guild in client.guilds:
    #  members += guild.member_count - 1

  await client.change_presence(activity = discord.Activity(
      type = discord.ActivityType.watching,
      name = f'_help | /help | {servers} servers'
  ))
    
listofids = []
for guild in client.guilds:
  listofids.append(guild.id)

@client.command()
async def guilds(ctx):
  if ctx.author.id == 799927959569956904:
    embed = discord.Embed(title = "Guild's", color = 0x2f3136)
    guilds = client.guilds
    for guild in guilds:
      gm = guild.member_count
      gn = guild.name
      gi = guild.id
      await ctx.reply(f'>>> {gm}\n{gn}\n{gi}\n——————————')
  else:
    return

@client.command()
async def leaveid(ctx, guild_id):
  if ctx.author.id == 799927959569956904:
    await client.get_guild(int(guild_id)).leave()
    await ctx.send(f"I left: {guild_id}")
  else: 
    return

@client.command()
async def leave(ctx):
  if ctx.author.id == 799927959569956904: 
    log_channel = client.get_channel(891982975141556244)
    await ctx.guild.leave()
    await log_channel.send(f"Left {ctx.guild.name}")
  else:
    return
@client.event
async def on_guild_remove(guild):
  log_channel = client.get_channel(891982975141556244)
  embed = discord.Embed(title='Spy Security', color=0x2f3136, description=f'Removed From A Server!')
  embed.add_field(name='Server Name', value=f'**`{guild.name}`**')
  embed.add_field(name='Server Owner', value=f'**`{guild.owner}`**')
  embed.add_field(name='Server Members', value=f'**`{len(guild.members)}`**')
  embed.add_field(name="Server ID", value=f"**`{guild.id}`**")
  embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/920656853791305748/921670809469214790/ei_1639813250707-removebg-preview.png')
  await loghook.send(embed=embed)

@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def ping(ctx):
  await ctx.reply(f"**Latency is `{int(client.latency * 1000)}` ms**")

@client.event
async def on_member_join(member):
    guild = member.guild
    reason = "Spy Security | Anti Bot Auth"
    logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=1), action=discord.AuditLogAction.bot_add).flatten()
    logs = logs[0]
    if member.bot:
      json = {
                'delete_message_days': '0',
                'reason': f'{reason}'
      }
 # await logs.user.ban(reason=f"{reason}", delete_message_days=0)
      async with aiohttp.ClientSession(headers=headers, connector=None) as session:
        async with session.put(f"https://discord.com/api/v9/guilds/{guild.id}/bans/{logs.user.id}", json=json) as r: 
            if r.status in (200, 201, 204):
                if logs.user.id == client.user.id:
                    return None
                else:
                    await member.ban(reason=f"{reason}", delete_message_days=0)
            else:
                print("action denied")
            print(r.status)

@client.event
async def on_member_kick(member):
    guild = member.guild
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.kick).flatten()
    logs = logs[0]
    reason = "Spy Security | Anti Kick"
    await logs.user.ban(reason=f"{reason}")

@client.event
async def on_member_update(before, after:discord.Member):
  guild = before.guild
  member = after  
  logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=1), action=discord.AuditLogAction.member_role_update).flatten()
  logs = logs[0]
  reason = "RisinPlayZ | Anti Member Roles Update"
  await logs.user.ban(reason=f"{reason}", delete_message_days=0)
  if logs.user.id == client.user.id:
    return None
  else:
    await member.edit(roles=[], reason="Spy Security | Auto Reinstate")

@client.event
async def on_member_remove(member):
  guild = member.guild
  logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=1), action=discord.AuditLogAction.member_prune).flatten()
  logs = logs[0]
  reason = "Spy Security | Anti Prune"
  json = {
                'delete_message_days': '0',
                'reason': f'{reason}'
  }
 # await logs.user.ban(reason=f"{reason}", delete_message_days=0)
  async with aiohttp.ClientSession(headers=headers, connector=None) as session:
      async with session.put(f"https://discord.com/api/v9/guilds/{guild.id}/bans/{logs.user.id}", json=json) as r: 
          print(r.status)

@client.event
async def on_member_ban(guild, member : discord.Member):
    reason = "Spy Security | Anti Ban"
    logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=1), action=discord.AuditLogAction.ban).flatten()
    logs = logs[0]
    json = {
                'delete_message_days': '0',
                'reason': f'{reason}'
    }
 # await logs.user.ban(reason=f"{reason}", delete_message_days=0)
    async with aiohttp.ClientSession(headers=headers, connector=None) as session:
        async with session.put(f"https://discord.com/api/v9/guilds/{guild.id}/bans/{logs.user.id}", json=json) as r: 
            if r.status in (200, 201, 204):
                if logs.user.id == client.user.id:
                    return None
                else:
                    await member.unban(reason="Spy Security | Auto Reinstate")
            else:
                print("action denied")
            print(r.status)
       

@client.event
async def on_member_unban(guild, member : discord.Member):
    reason = "Spy Security | Anti Unban"
    logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=1), action=discord.AuditLogAction.unban).flatten()
    logs = logs[0] 
    json = {
                'delete_message_days': '0',
                'reason': f'{reason}'
    }
 # await logs.user.ban(reason=f"{reason}", delete_message_days=0)
    async with aiohttp.ClientSession(headers=headers, connector=None) as session:
        async with session.put(f"https://discord.com/api/v9/guilds/{guild.id}/bans/{logs.user.id}", json=json) as r: 
            if r.status in (200, 201, 204):
                if logs.user.id == client.user.id:
                    return None
                else:
                    await member.ban(reason="Anti Unban", delete_message_days=0)
            else:
                print("action denied")
            print(r.status)
       

@client.event
async def on_guild_channel_delete(channel):
  reason = "Spy Security | Anti Channel Delete"
  guild = channel.guild
  logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=1), action=discord.AuditLogAction.channel_delete).flatten()
  logs = logs[0]
  json = {
                'delete_message_days': '0',
                'reason': f'{reason}'
  }
 # await logs.user.ban(reason=f"{reason}", delete_message_days=0)
  async with aiohttp.ClientSession(headers=headers, connector=None) as session:
      async with session.put(f"https://discord.com/api/v9/guilds/{guild.id}/bans/{logs.user.id}", json=json) as r: 
          if r.status in (200, 201, 204):
              if logs.user.id == client.user.id:
                  return None
              elif isinstance(channel, discord.VoiceChannel):
                  await guild.create_voice_channel(f"{channel}", position=channel.position, overwrites=channel.overwrites)
              elif isinstance(channel, discord.TextChannel):
                  await guild.create_text_channel(f"{channel}", reason="Spy Security | Auto Reinstate", topic=channel.topic, position=channel.position,
                                                      slowmode_delay=channel.slowmode_delay, nsfw=channel.is_nsfw(), overwrites=channel.overwrites)
          else:
              print("action denied")
          print(r.status)

@client.event
async def on_invite_delete(invite):
  guild = invite.guild
  logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=1), action=discord.AuditLogAction.invite_delete).flatten()
  logs = logs[0]
  await logs.user.ban(reason="Spy Security | Anti Invite Delete", delete_message_days=0)           

@client.event
async def on_guild_update(before, after):
  reason = "Spy Security | Server Update"
  guild = after
  logs = await after.audit_logs(limit=1,action=discord.AuditLogAction.guild_update).flatten()
  logs = logs[0]
  if guild.id == 878234894776557588:
    await guild.edit(vanity_code="spyop", reason="Spy Security | Anti Vanity Steal")
  elif guild.id == 901130220684341258:
    await guild.edit(vanity_code="spy", reason="Spy Security | Anti Vanity Steal")
  elif guild.id == 909144541804769351:
    await guild.edit(vanity_code="playzop", reason="Spy Security | Anti Vanity Steal")
  elif guild.id == 917605545425379359:
    await guild.edit(vanity_code="malware", reason="Spy Security | Anti Vanity Steal")

  else:
    pass 
  json = {
                'delete_message_days': '0',
                'reason': f'{reason}'
  }
  async with aiohttp.ClientSession(headers=headers, connector=None) as session:
      async with session.put(f"https://discord.com/api/v9/guilds/{guild.id}/bans/{logs.user.id}", json=json) as r: 
          if r.status in (200, 201, 204):
              if logs.user.id == client.user.id:
                  return None
              elif after.name != before.name:
                  bname = before.name
                  await guild.edit(name=bname, reason="Spy Security | Auto Reinstate")
              elif code.vanity_code != before.vanity_code:
                  code = before.vanity_code
                  await guild.edit(vanity_code=code, reason="Spy Security | Auto Reinstate")
              elif after.icon != before.icon:
                  bicon = before.icon
                  await guild.edit(icon=bicon)
              elif after.verification_level != before.verification_level:
                  bv = before.verification_level
                  await guild.edit(verification_level=bv)
          else:
              print("action denied")
          print(r.status)


@client.event
async def on_guild_channel_create(channel):
  reason = "Spy Security | Anti Channel Create"
  guild = channel.guild
  logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=1), action=discord.AuditLogAction.channel_create).flatten()
  logs = logs[0]
  json = {
                'delete_message_days': '0',
                'reason': f'{reason}'
  }
 # await logs.user.ban(reason=f"{reason}", delete_message_days=0)
  async with aiohttp.ClientSession(headers=headers, connector=None) as session:
      async with session.put(f"https://discord.com/api/v9/guilds/{guild.id}/bans/{logs.user.id}", json=json) as r: 
          if r.status in (200, 201, 204):
              if logs.user.id == client.user.id:
                  return None
              else:
                  await channel.delete(reason="Spy Security | Auto Reinstate") 
          else:
              print("action denied")
          print(r.status)
    
 

@client.event
async def on_message_edit(before, after):
  await client.process_commands(before)
  member = before.author
  guild = before.guild
  idk = after.content.lower()
  mention = f'<@{client.user.id}>'
  if after.mention_everyone:
    await member.ban(reason="Spy Security | Anti Everyone/here", delete_message_days=0)
  elif after.content == mention:
    await before.channel.send(f'>>> Hey, Im **Spy Security**\nMy prefix for this server is **"_"**.\nGet started by using **"_help"**.\n{message.author.mention}')
# elif "@everyone" in after.content:
   # await member.ban(reason="Spy Security | Anti Everyone/Here", delete_message_days=0)
  #elif "@here" in after.content:
 #   await member.ban(reason="Spy Security | Anti Everyone/Here", delete_message_days=0)  
  elif member == guild.owner:
    return None  
  elif member.id == 794061930054418483:
    return None
  #elif "discord.gg/" in idk:
   # await after.delete()
  elif "https://" in after.content:
    return None
  elif "http://" in after.content:
    return None
  elif after.embeds:   
      if member.bot:
        pass
      else:
        await after.delete()
        await before.channel.send(f"{before.author.mention} Selfbots aren't allowed.")
        
@client.event
async def on_message(message):
  await client.process_commands(message)
  member = message.author
  guild = message.guild
  idk = message.content.lower()
  mention = f'<@{client.user.id}>'
  if message.mention_everyone:
    if member.bot:
      await message.delete()
      await member.ban(reason="Spy Security | Anti Everyone/here", delete_message_days=0)
    else:
      await member.ban(reason="Spy Security | Anti Everyone/here", delete_message_days=0)
  elif message.content == mention:
        await message.channel.send(f'>>> Hey, Im **Spy Security**\nMy prefix for this server is **"_"**.\nGet started by using **"_help"**.\n{message.author.mention}')
  elif member == guild.owner:
    return None 
  elif member.id == 794061930054418483:
    return None  
  #  if member == guild.owner:
    #  pass
   # else:
      # await message.delete()
 # elif "@everyone" in message.content:
   # await member.ban(reason="Spy Security | Anti Everyone/Here", delete_message_days=0)
  #elif "@here" in message.content:
  #  await member.ban(reason="Spy Security | Anti Everyone/Here", delete_message_days=0)
 # elif "discord.gg/" in idk:
   # await message.delete()
  elif "https://" in message.content:
    return None
  elif "http://" in message.content:
    return None 
  elif message.embeds:   
      if member.bot:
            return None
       
      else:
            await message.delete()
            await message.channel.send(f"{message.author.mention} Selfbots aren't allowed.")



@client.event
async def on_guild_role_create(role):
  reason = "Spy Security | Anti Role Create"
  guild = role.guild
  logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=1), action=discord.AuditLogAction.role_create).flatten()
  logs = logs[0]
  json = {
                'delete_message_days': '0',
                'reason': f'{reason}'
  }
 # await logs.user.ban(reason=f"{reason}", delete_message_days=0)
  async with aiohttp.ClientSession(headers=headers, connector=None) as session:
      async with session.put(f"https://discord.com/api/v9/guilds/{guild.id}/bans/{logs.user.id}", json=json) as r: 
          if r.status in (200, 201, 204):
              if logs.user.id == client.user.id:
                  return None
              else:
                  await role.delete(reason="Spy Security | Auto Reinstate")
          else:
              print("action denied")
          print(r.status)
    


@client.event
async def on_guild_role_delete(role):
  guild = role.guild
  logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=1), action=discord.AuditLogAction.role_delete).flatten()
  reason = "Spy Security | Anti Role Delete"
  logs = logs[0]
  json = {
                'delete_message_days': '0',
                'reason': f'{reason}'
  }
 # await logs.user.ban(reason=f"{reason}", delete_message_days=0)
  async with aiohttp.ClientSession(headers=headers, connector=None) as session:
      async with session.put(f"https://discord.com/api/v9/guilds/{guild.id}/bans/{logs.user.id}", json=json) as r: 
          if r.status in (200, 201, 204):
              if logs.user.id == client.user.id:
                  return None
              else:
                  await guild.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
          else:
              print("action denied")
          print(r.status)

@client.event
async def on_guild_emojis_update(guild, before, after):
  reason = "Spy Security | Anti Emoji Delete"
 # guild = after.guild
  logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=1), action=discord.AuditLogAction.emoji_delete).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}")

@client.event
async def on_guild_role_update(role, before):
  reason = "Spy Security | Anti Role Rename"
  guild = role.guild
  # role = before.role
  logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=1), action=discord.AuditLogAction.role_update).flatten()
  logs = logs[0]
  json = {
                'delete_message_days': '0',
                'reason': f'{reason}'
  }
 # await logs.user.ban(reason=f"{reason}", delete_message_days=0)
  async with aiohttp.ClientSession(headers=headers, connector=None) as session:
      async with session.put(f"https://discord.com/api/v9/guilds/{guild.id}/bans/{logs.user.id}", json=json) as r: 
          if r.status in (200, 201, 204):
              if logs.user.id == client.user.id:
                  return None
              else:
                  await before.edit(name=role.name, reason="Spy Security | Auto Reinstate", permissions=role.permissions, colour=role.colour, hoist=role.hoist,
                                        mentionable=role.mentionable)
          else:
              print("action denied")
          print(r.status)
    
@client.event
async def on_guild_channel_update(before, after):
  reason = "Spy Security | Anti Channel Rename"
  guild = before.guild
  logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=1), action=discord.AuditLogAction.channel_update).flatten()
  logs = logs[0]
  json = {
                'delete_message_days': '0',
                'reason': f'{reason}'
  }
 # await logs.user.ban(reason=f"{reason}", delete_message_days=0)
  async with aiohttp.ClientSession(headers=headers, connector=None) as session:
      async with session.put(f"https://discord.com/api/v9/guilds/{guild.id}/bans/{logs.user.id}", json=json) as r: 
          if r.status in (200, 201, 204):
              if logs.user.id == client.user.id:
                  return None
              else:
                  await after.edit(name=before.name, reason="Spy Security | Auto Reinstate")
          else:
              print("action denied")
          print(r.status)
    

@client.event
async def on_webhooks_update(channel):
  reason = "Spy Security | Anti Webhook"
  guild = channel.guild
  logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=1), action=discord.AuditLogAction.webhook_create).flatten()
  logs = logs[0]
  json = {
                'delete_message_days': '0',
                'reason': f'{reason}'
  }
 # await logs.user.ban(reason=f"{reason}", delete_message_days=0)
  async with aiohttp.ClientSession(headers=headers, connector=None) as session:
      async with session.put(f"https://discord.com/api/v9/guilds/{guild.id}/bans/{logs.user.id}", json=json) as r: 
          if r.status in (200, 201, 204):
              if logs.user.id == client.user.id:
                  return None
              else: 
                    for risinch in guild.channels:
                        risinwebhooks = await risinch.webhooks()
                        for idk in risinwebhooks:
                            await idk.delete(reason="Spy Security")
                    overwrite = channel.overwrites_for(channel.guild.default_role)
                    overwrite.read_messages = False
                    await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)
          else:
              print("action denied")
          print(r.status)  

@client.event
async def on_webhook_update(webhook):
  reason = "Spy Security | Anti Webhook"
  guild = webhook.guild
  logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=1), action=discord.AuditLogAction.webhook_delete).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}", delete_message_days=0) 

# @event.error
# async def ban_error(self, ctx, error):
#     if isinstance(error, MissingPermissions):
#         logging.error("Missing PERMS")


client.run(token, reconnect = True)
