
import discord
import random
import youtube_dl
import os
from discord.ext import commands
client = commands.Bot(command_prefix='.')

players = {}
@client.event
async def on_ready():
    print('Bot initiated')
@client.event
async def on_member_join(member):
    print(f'(member) has joined the server!')
@client.event
async def on_member_remove(member):
    print(f'(member) has left the server!')
@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')
@client.command()
async def rD20(ctx):
    await ctx.send(f'You rolled a {random.randint(1,20)}!')
@client.command()
async def rD6(ctx):
    await ctx.send(f'You rolled a {random.randint(1,6)}!')
@client.command()
async def rD10(ctx):
    await ctx.send(f'You rolled a {random.randint(1,10)}!')
@client.command()
async def rD100(ctx):
    await ctx.send(f'You rolled a {random.randint(1,100)}!')
@client.command()
async def rD4(ctx):
    await ctx.send(f'You rolled a {random.randint(1,4)}!')
@client.command()
async def rD12(ctx):
    await ctx.send(f'You rolled a {random.randint(1,12)}!')
@client.command()
async def rD8(ctx):
    await ctx.send(f'You rolled a {random.randint(1,8)}!')
@client.command()
async def rClass(ctx):
    classes = ['Warlock',
                'Wizard',
                'Barbarian',
                'Druid',
                'Rogue',
                'Paladin',
                'Sorcerer',
                'Fighter',
                'Bard',
                'Cleric',
                'Monk']
    await ctx.send(f'Your class is {random.choice(classes)}!')

@client.command()
async def rRace(ctx):
    races = ['DragonBorn',
                'Human',
                'Halfling',
                'Gnome',
                'Tiefling',
                'Half-Elf',
                'Elf',
                'Genasi',
                'Asimar',
                'Aricocra',
                'Half-Orc']
    await ctx.send(f'Your race is {random.choice(races)}!')
@client.command()
async def rCharacter(ctx):
    classes = ['Warlock',
               'Wizard',
               'Barbarian',
               'Druid',
               'Rogue',
               'Paladin',
               'Sorcerer',
               'Fighter',
               'Bard',
               'Cleric',
               'Monk']
    races = ['DragonBorn',
             'Human',
             'Halfling',
             'Gnome',
             'Tiefling',
             'Half-Elf',
             'Elf',
             'Genasi',
             'Asimar',
             'Aricocra',
             'Half-Orc']
    await ctx.send(f'Your race is {random.choice(races)} and your class is {random.choice(classes)}!')

@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)



@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()


@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Song is currently playing. Please Skip first.")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()

@client.command()
async def skip(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

client.run('TOKEN')
