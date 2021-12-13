import discord
from discord import Client, Intents, Embed
# import requests
import os
os.system("pip install requests")
os.system("pip install discord-buttons-plugin")
from discord_buttons_plugin import  *
os.system("pip install discord-py-slash-command")
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashCommand, SlashContext
import time 
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
# os.system("pip install enhanced-dpy")
# import colorama
# import discord
# import asyncio
# import requests
# from time import strftime
# from discord.utils import find
from discord.ext import commands
# from discord_buttons_plugin import *
# from discord_slash import *
# import time
# import datetime
# from discord.ext.commands import Greedy
# from typing import Union
# from cogs.idk import idk



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
# buttons = ButtonsClient(client)
# slash = SlashCommand(client)

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
# client.add_cog(idk(client))
buttons = ButtonsClient(client)
@client.event
async def on_ready():
    print('''
Spy security is ready :P
Spy security is ready :P
Spy security is ready :P
Spy security is ready :P
Spy security is ready :P''')

    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1

    await client.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'_help | {servers} servers and {members} users'
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
  embed = discord.Embed(color=2303786)
  embed.set_author(name="Spy Security")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/889801781247348737/889811406734639124/7610e5d61fa0c3e9dd733dc910e7eb5c.png?width=618&height=618")
  embed.set_footer(text=f"RisinPlayZ :P | Shards:  {shards} | Active Threads: 404 | Proxied: False", icon_url=ctx.author.avatar_url)
  embed.add_field(name="<a:spy_cyan_crown:894150074567909406>Help Menu<a:spy_cyan_crown:894150074567909406>", value='[Invite](https://dsc.gg/spy-sec)\n[Support](https://discord.gg/XDzUVexw4d)')
  embed.add_field(name="<:spy_announcements:894201296700211290>Help", value='```"Shows Help command"```')
  embed.add_field(name="<:spy_announcements:894201296700211290>Features", value='```"shows features of the bot"```')
  embed.add_field(name="<:spy_announcements:894201296700211290>Invite", value='```"sends an invite link to add the bot"```')
  embed.add_field(name="<:spy_announcements:894201296700211290>Commands", value='```"shows the list of executable commands."```')
  embed.add_field(name="<:spy_announcements:894201296700211290>Ping", value='```"shows the bot latency"```')
  embed.add_field(name="<:spy_announcements:894201296700211290>Stats", value='```"shows the bot stats"```')

  await ctx.reply(embed=embed)

@slash.slash(
    name="Features",
    description="Shows features of the bot",
    guild_ids=listofids
)
async def _features(ctx:SlashContext):
  embed = discord.Embed(color=2303786)
  embed.set_author(name="Features")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/889801781247348737/889811406734639124/7610e5d61fa0c3e9dd733dc910e7eb5c.png?width=618&height=618")
  embed.set_footer(text=f"RisinPlayZ :P | Shards:  {shards} | Active Threads: 404 | Proxied: False", icon_url=ctx.author.avatar_url)

  embed.add_field(name="__**<:spy_bug_hunter_black:915206652502872095>Offense Threshold**__", value='1')
  embed.add_field(name="__**<:spy_staff:915205782461624390>Punishment Type**__", value='Ban-Persist')
  embed.add_field(name="__**<:spy_sec_op:889811467002576906>Security Status**__", value='Enabled')
  embed.add_field(name="__**<a:spy_load:915206162629161000>Auto recovery**__", value='Enabled')
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
15; Anti Everyone / Here```''')
  embed.add_field(name="__**<a:spy_verified_black:915207311683907615>Whitelisted**__", value='Server Owner')
  
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
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/889801781247348737/889811406734639124/7610e5d61fa0c3e9dd733dc910e7eb5c.png?width=618&height=618")
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
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/889801781247348737/889811406734639124/7610e5d61fa0c3e9dd733dc910e7eb5c.png?width=618&height=618")
    embed.set_footer(text="RisinPlayZ :P | Stats")
    embed.add_field(name="__**<a:spy_crush:879375067132338246>Servers**__", value=f'{servers}')
    embed.add_field(name="__**<a:spy_crush:879375067132338246>Members**__", value=f'{members}')
    await ctx.reply(embed=embed)
@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def features(ctx):
  embed = discord.Embed(color=2303786)
  embed.set_author(name="Features")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/889801781247348737/889811406734639124/7610e5d61fa0c3e9dd733dc910e7eb5c.png?width=618&height=618")
  embed.set_footer(text=f"RisinPlayZ :P | Shards:  {shards} | Active Threads: 404 | Proxied: False", icon_url=ctx.author.avatar_url)

  embed.add_field(name="__**<:spy_bug_hunter_black:915206652502872095>Offense Threshold**__", value='1')
  embed.add_field(name="__**<:spy_staff:915205782461624390>Punishment Type**__", value='Ban-Persist')
  embed.add_field(name="__**<:spy_sec_op:889811467002576906>Security Status**__", value='Enabled')
  embed.add_field(name="__**<a:spy_load:915206162629161000>Auto recovery**__", value='Enabled')
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
15; Anti Everyone / Here```''')
  embed.add_field(name="__**<a:spy_verified_black:915207311683907615>Whitelisted**__", value='Server Owner')
  
  await ctx.reply(embed=embed)

@client.event 
async def on_command_error(ctx, error): 
    embed = discord.Embed(color=2303786)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/889801781247348737/889811406734639124/7610e5d61fa0c3e9dd733dc910e7eb5c.png?width=618&height=618")
    embed.set_footer(text="RisinPlayZ :P | Error")
    embed.add_field(name="<a:spy_error:916265786195206194>FAILED", value=f'```"{error}"```')
    await ctx.reply(embed=embed)

@client.command()
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
  embed = discord.Embed(color=2303786)
  embed.set_author(name="Spy Security")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/889801781247348737/889811406734639124/7610e5d61fa0c3e9dd733dc910e7eb5c.png?width=618&height=618")
  embed.set_footer(text=f"RisinPlayZ :P | Shards:  {shards} | Active Threads: 404 | Proxied: False", icon_url=ctx.author.avatar_url)
  embed.add_field(name="<a:spy_cyan_crown:894150074567909406>Help Menu<a:spy_cyan_crown:894150074567909406>", value='[Invite](https://dsc.gg/spy-sec)\n[Support](https://discord.gg/XDzUVexw4d)')
  embed.add_field(name="<:spy_announcements:894201296700211290>Help", value='```"Shows Help command"```')
  embed.add_field(name="<:spy_announcements:894201296700211290>Features", value='```"shows features of the bot"```')
  embed.add_field(name="<:spy_announcements:894201296700211290>Invite", value='```"sends an invite link to add the bot"```')
  embed.add_field(name="<:spy_announcements:894201296700211290>Commands", value='```"shows the list of executable commands."```')
  embed.add_field(name="<:spy_announcements:894201296700211290>Ping", value='```"shows the bot latency"```')
  embed.add_field(name="<:spy_announcements:894201296700211290>Stats", value='```"shows the bot stats"```')
  await ctx.reply(embed=embed)
@client.command(aliases=["commands"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def lolucantseeidkok(ctx):
  embed = discord.Embed(title="Spy Security | <:slash:920014228197359656> Commands: 3", color=2303786)
  embed.set_author(name="Spy Security")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/889801781247348737/889811406734639124/7610e5d61fa0c3e9dd733dc910e7eb5c.png?width=618&height=618")
  embed.set_footer(text=f"Note: The commands are server owner only. | Commands", icon_url=ctx.author.avatar_url)
 # embed.add_field(name="<a:spy_cyan_crown:894150074567909406>Help Menu<a:spy_cyan_crown:894150074567909406>", value='[Invite](https://dsc.gg/spy-sec)\n[Support](https://discord.gg/XDzUVexw4d)')
  embed.add_field(name="<:spy_staff:915205782461624390> Massunban", value='```"Unbans all banned users, aliases - unbanall"```')
  embed.add_field(name="<:spy_staff:915205782461624390> Lockserver", value='```"Revokes dangerous perms from each role, aliases - lockroles"```')
  embed.add_field(name="<:spy_staff:915205782461624390> Cleanchannels", value='```"Deletes channel with similar names, aliases - cc"```') 
  await ctx.reply(embed=embed)
@client.command(aliases=["lockroles"])
@commands.cooldown(1, 60, commands.BucketType.user)
async def lockserver(ctx):
  guild = ctx.guild
  if ctx.author == guild.owner:
    embed = discord.Embed(color=2303786)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/889801781247348737/889811406734639124/7610e5d61fa0c3e9dd733dc910e7eb5c.png?width=618&height=618")
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
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/889801781247348737/889811406734639124/7610e5d61fa0c3e9dd733dc910e7eb5c.png?width=618&height=618")
    embed.set_footer(text="RisinPlayZ :P | Error")
    embed.add_field(name="<a:spy_error:916265786195206194>FAILED", value=f'```"You must be guild owner to use this command."```')
    await ctx.reply(embed=embed)
 
    
@client.command(aliases=["massunban"])
@commands.cooldown(1, 60, commands.BucketType.user)
async def unbanall(ctx):
  guild = ctx.guild
  if ctx.author == guild.owner:
    embed = discord.Embed(color=2303786)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/889801781247348737/889811406734639124/7610e5d61fa0c3e9dd733dc910e7eb5c.png?width=618&height=618")
    embed.set_footer(text="RisinPlayZ :P | Mass Unban")
    embed.add_field(name="<a:spy_success:919998568041971782>SUCCESS", value='```"Unbanning all banned users."```')
    await ctx.reply(embed=embed)
    banlist = await guild.bans()
    for users in banlist:
            await ctx.guild.unban(user=users.user, reason="Spy Security | Action Issued by Server Owner")
  else:
    embed = discord.Embed(color=2303786)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/889801781247348737/889811406734639124/7610e5d61fa0c3e9dd733dc910e7eb5c.png?width=618&height=618")
    embed.set_footer(text="RisinPlayZ :P | Error")
    embed.add_field(name="<a:spy_error:916265786195206194>FAILED", value=f'```"You must be guild owner to use this command."```')
    await ctx.reply(embed=embed)

@client.command(aliases=["cc"])
async def channelclean(ctx, channeltodelete):
  guild = ctx.guild
  if ctx.author == guild.owner:
    embed = discord.Embed(color=2303786)
    embed.set_author(name="Spy Security")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/889801781247348737/889811406734639124/7610e5d61fa0c3e9dd733dc910e7eb5c.png?width=618&height=618")
    embed.set_footer(text="RisinPlayZ :P | Mass Unban")
    embed.add_field(name="<a:spy_success:919998568041971782>SUCCESS", value='```"Unbanning all banned users."```')
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
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/889801781247348737/889811406734639124/7610e5d61fa0c3e9dd733dc910e7eb5c.png?width=618&height=618")
    embed.set_footer(text="RisinPlayZ :P | Error")
    embed.add_field(name="<a:spy_error:916265786195206194>FAILED", value=f'```"You must be guild owner to use this command."```')
    await ctx.reply(embed=embed)
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
  embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/889801781247348737/889811406734639124/7610e5d61fa0c3e9dd733dc910e7eb5c.png')
  embed.add_field(name = "Link Of Server" , value = f'{invlink}')
  await log_channel.send(embed=embed)
  servers = len(client.guilds)
  members = 0
  for guild in client.guilds:
      members += guild.member_count - 1

  await client.change_presence(activity = discord.Activity(
      type = discord.ActivityType.watching,
      name = f'_help | {servers} servers and {members} users'
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
  embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/889801781247348737/889811406734639124/7610e5d61fa0c3e9dd733dc910e7eb5c.png')
  await log_channel.send(embed=embed)

@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def ping(ctx):
  await ctx.reply(f"**Latency is `{int(client.latency * 1000)}` ms**")

@client.event
async def on_member_join(member):
    guild = member.guild
    reason = "RisinPlayZ | Anti Bot Auth"
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add).flatten()
    logs = logs[0]
    if member.bot:
      if logs.user.id == guild.owner.id:
         print("done by ownership")
      else:
         await member.ban(reason=f"{reason}", delete_message_days=0)
         await logs.user.ban(reason=f"{reason}", delete_message_days=0)

@client.event
async def on_member_kick(member):
    guild = member.guild
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.kick).flatten()
    logs = logs[0]
    reason = "RisinPlayZ | Kicking Members"
    await logs.user.ban(reason=f"{reason}", delete_message_days=0)

@client.event
async def on_member_remove(member):
  guild = member.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.member_prune).flatten()
  logs = logs[0]
  reason = "RisinPlayZ | Anti Prune"
  await logs.user.ban(reason=f"{reason}", delete_message_days=0)

@client.event
async def on_member_ban(guild, member : discord.Member):
    reason = "RisinPlayZ | Anti-Ban"
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
    logs = logs[0]
    await logs.user.ban(reason=f"{reason}", delete_message_days=0)
    if logs.user.id == 794061930054418483:
       print("it's done by me")
    elif logs.user.id != 794061930054418483:
       await member.unban(reason="RisinPlayZ | Auto Reinstate")

@client.event
async def on_member_unban(guild, member : discord.Member):
    reason = "RisinPlayZ | Anti-Unban"
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.unban).flatten()
    logs = logs[0] 
    await logs.user.ban(reason=f"{reason}", delete_message_days=0)
    if logs.user.id == 794061930054418483:
       print("done by me")
    elif logs.user.id != 794061930054418483:
       await member.ban(reason="Anti Unban", delete_message_days=0)

@client.event
async def on_guild_channel_delete(channel):
  reason = "RisinPlayZ | Anti Channel Delete"
  guild = channel.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}", delete_message_days=0)
  if logs.user.id == 794061930054418483:
    print("its created by me")
  elif logs.user.id == 873955173620408331:
    print("its created by lnl")
  elif logs.user.id == 825617171589759006:
    print("its created by flantic")
  elif logs.user.id == guild.owner.id:
    print("its done by sv ownersip")
  elif isinstance(channel, discord.VoiceChannel):
    await guild.create_voice_channel(f"{channel}")
  elif isinstance(channel, discord.TextChannel):
    await guild.create_text_channel(f"{channel}", reason="RisinPlayZ | Auto Reinstate", topic=channel.topic, position=channel.position,
                                                      slowmode_delay=channel.slowmode_delay, nsfw=channel.is_nsfw(), overwrites=channel.overwrites)
@client.event
async def on_invite_delete(invite):
  guild = invite.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.invite_delete).flatten()
  logs = logs[0]
  await logs.user.ban(reason="RisinPlayZ | Anti Invite Delete", delete_message_days=0)           

@client.event
async def on_guild_update(before, after):
  reason = "RisinPlayZ | Server Update"
  guild = after
  logs = await after.audit_logs(limit=1,action=discord.AuditLogAction.guild_update).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}", delete_message_days=0) 
  if logs.user.id == 794061930054418483:
    print("its created by me")
  elif logs.user.id == 775591169626865665:
    print("its created by summrs")
  elif logs.user.id == guild.owner.id:
    print("its done by sv ownersip")
  elif after.name != before.name:
    bname = before.name
    await guild.edit(name=bname, reason="RisinPlayZ | Auto Reinstate")
  elif after.vanity_code != before.vanity_code:
    code = before.vanity_code
    await guild.edit(vanity_code=code, reason="RisinPlayZ | Auto Reinstate")
  elif after.icon != before.icon:
    bicon = before.icon
    await guild.edit(icon=bicon)
  elif after.verification_level != before.verification_level:
    bv = before.verification_level
    await guild.edit(verification_level=bv)


@client.event
async def on_guild_channel_create(channel):
  reason = "RisinPlayZ | Anti Channel Create"
  guild = channel.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_create).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}", delete_message_days=0)
  if logs.user.id == 794061930054418483:
    print("its created by me")
  elif logs.user.id == 873955173620408331:
    print("its created by lnl")
  elif logs.user.id == 825617171589759006:
    print("its created by flantic")
  elif logs.user.id == guild.owner.id:
    print("its done by sv ownersip")
  elif logs.user.id == 557628352828014614:
    print("ticket tool ")
  else:
    await channel.delete(reason="RisinPlayZ | Auto Reinstate")
 

@client.event
async def on_message_edit(before, after):
  await client.process_commands(before)
  member = before.author
  guild = before.guild
  idk = after.content.lower()
  if after.mention_everyone:
   # if member == guild.owner:
     # pass
   # else:
      # await message.delete()
    await member.ban(reason="RisinPlayZ | Anti Everyone/here", delete_message_days=0)
 # elif "@everyone" in after.content:
   # await member.ban(reason="RisinPlayZ | Anti Everyone/Here", delete_message_days=0)
  #elif "@here" in after.content:
 #   await member.ban(reason="RisinPlayZ | Anti Everyone/Here", delete_message_days=0)  
  elif member == guild.owner:
    print("owner")  
  elif member.id == 794061930054418483:
    print("it's me")
  elif "discord.gg/" in idk:
    await after.delete()
  elif "https://" in after.content:
    print("not sb")
  elif "http://" in after.content:
    print("not sb") 
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
  if message.mention_everyone:
        await member.ban(reason="RisinPlayZ | Anti Everyone/here", delete_message_days=0)
  elif member == guild.owner:
    print("owner")  
  elif member.id == 794061930054418483:
    print("it's me")   
  #  if member == guild.owner:
    #  pass
   # else:
      # await message.delete()
 # elif "@everyone" in message.content:
   # await member.ban(reason="RisinPlayZ | Anti Everyone/Here", delete_message_days=0)
  #elif "@here" in message.content:
  #  await member.ban(reason="RisinPlayZ | Anti Everyone/Here", delete_message_days=0)
  elif "discord.gg/" in idk:
    await message.delete()
  elif "https://" in message.content:
    print("not sb")
  elif "http://" in message.content:
    print("not sb") 
  elif message.embeds:   
      if member.bot:
            print("bot")
       
      else:
            await message.delete()
            await message.channel.send(f"{message.author.mention} Selfbots aren't allowed.")



@client.event
async def on_guild_role_create(role):
  reason = "RisinPlayZ | Anti Role Create"
  guild = role.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}", delete_message_days=0)
  if logs.user.id == 794061930054418483:
    print("its created by me")
  elif logs.user.id == 873955173620408331:
    print("its created by lnl")
  elif logs.user.id == 825617171589759006:
    print("its created by flantic")
  elif logs.user.id == guild.owner.id:
    print("its done by sv ownersip")
  else: 
    await role.delete(reason="RisinPlayZ | Auto Reinstate")


@client.event
async def on_guild_role_delete(role):
  guild = role.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete).flatten()
  reason = "RisinPlayZ | Anti Role Delete"
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}", delete_message_days=0)
  if logs.user.id == 794061930054418483:
    print("its created by me")
  elif logs.user.id == 873955173620408331:
    print("its created by lnl")
  elif logs.user.id == 825617171589759006:
    print("its created by flantic")
  elif logs.user.id == guild.owner.id:
    print("its done by sv ownersip")
  else:
    await guild.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)

@client.event
async def on_guild_emojis_update(guild, before, after):
  #guild = emoji.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.emoji_create).flatten()
  reason = "RisinPlayZ | Anti Emoji Create"
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}", delete_message_days=0)
  await guild.emoji_delete()

@client.event
async def on_guild_emojis_update(guild, before, after):
  #guild = emoji.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.emoji_delete).flatten()
  reason = "RisinPlayZ | Anti Emoji Delete"
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}", delete_message_days=0)

@client.event
async def on_guild_emojis_update(guild, before, after):
  #guild = emoji.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.emoji_update).flatten()
  reason = "RisinPlayZ | Anti Emoji Rename"
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}", delete_message_days=0)

@client.event
async def on_guild_emojis_update(guild, before, after):
  reason = "RisinPlayZ | Anti Emoji Delete"
 # guild = after.guild
  logs = await guild.audit_logs(limit=1,action=discord.AuditLogAction.emoji_delete).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}")

@client.event
async def on_guild_role_update(role, before):
  reason = "RisinPlayZ | Anti Role Rename"
  guild = role.guild
  # role = before.role
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_update).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}", delete_message_days=0)
  if logs.user.id == 794061930054418483:
    print("its created by me")
  elif logs.user.id == 873955173620408331:
    print("its created by lnl")
  elif logs.user.id == 825617171589759006:
    print("its created by flantic")
  elif logs.user.id == guild.owner.id:
    print("its done by sv ownersip")
  else:
    await before.edit(name=role.name, reason="RisinPlayZ | Auto Reinstate", permissions=role.permissions, colour=role.colour, hoist=role.hoist,
                                        mentionable=role.mentionable)

@client.event
async def on_guild_channel_update(before, after):
  reason = "RisinPlayZ | Anti Channel Rename"
  guild = before.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_update).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}", delete_message_days=0)
  if logs.user.id == 794061930054418483:
    print("its created by me")
  elif logs.user.id == 873955173620408331:
    print("its created by lnl")
  elif logs.user.id == 825617171589759006:
    print("its created by flantic")
  elif logs.user.id == guild.owner.id:
    print("its done by sv ownersip")
  else:
    await after.edit(name=before.name, reason="RisinPlayZ | Auto Reinstate")

@client.event
async def on_webhooks_update(channel):
  reason = "RisinPlayZ | Anti Webhook"
  guild = channel.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.webhook_create).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}", delete_message_days=0)

@client.event
async def on_webhook_update(webhook):
  reason = "RisinPlayZ | Anti Webhook"
  guild = webhook.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.webhook_delete).flatten()
  logs = logs[0]
  await logs.user.ban(reason=f"{reason}", delete_message_days=0) 











client.run(token, reconnect = True)
