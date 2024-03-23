import discord  # discord.py package
import aiohttp  # vajalik hilisemaks
import random
from debugpy.launcher import channel


# Funktsioon, mis hakkab kasutajate sõnumeid käsitlema
async def handle_response(message) -> str:
    gifs = ["https://media1.tenor.com/m/rRgs6XtH5kEAAAAd/hi-oomf-cute-anime-girl-vtuber.gif",
            "https://media1.tenor.com/m/P7hCyZlzDH4AAAAC/wink-anime.gif",
            "https://media1.tenor.com/m/NHV9r7WczWkAAAAC/oshi-no-ko-memcho.gif",
            "https://media1.tenor.com/m/Gv1cMkqev0wAAAAC/anime-confused.gif",
            "https://media1.tenor.com/m/krKJLArM5FAAAAAC/thumbs-up-thumbs-up-gif.gif"]
    laserGrid = ["https://media1.tenor.com/m/2LMV1vTX15EAAAAC/talking-ben-yes.gif",
                 "https://media1.tenor.com/m/uvcES2Nedr0AAAAd/talking-ben-no.gif"]

    # Teeme iga sõnumi väiketäheliseks, et endal oleks kergem
    message = message.lower()

    # Kui sõnum oli !abi, saadame kasutajale vastuse
    if message == "hi":
        return "Hello, mate!"
    if message == "creditcardnumber":
        return "56497537985 rsv 678 date of expiration 25/11"
    if message == "thanksmatpac":
        return "You are welcome, Matvei from Õismäe, age 21, favourite anime Code Geass, GPA 4.9"
    if message == "gif":
        return random.choice(gifs)
    if message == "lasergrid":
        return random.choice(laserGrid)
    if message == "nick":
        return "https://media1.tenor.com/m/3Zxo-oyXVSAAAAAd/yummy-mmm.gif"
    if message == "оценкивыставили":
        return "whaaaaaat😳"
    if message == "bestmusic":
        return "https://youtu.be/60ItHLz5WEA?si=TvCFf-LeuV2iaPkF"
    if message == "milk":
        return "💀"


# Sõnumi saatmine kasutajale (siin ei pea midagi muutma)
async def send_message(message, user_message):
    try:
        response = await handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

# Boti registreerimine
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)


# Tegevus, kui bot valmis laeb
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# Tegevus, kui keegi serveriga liitub
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    if channel:
        await channel.send(f"Welcome {member.mention} to the server!")


# Tegevus, kui keegi serveris sõnumi saadab
@client.event
async def on_message(message):
    # Ignoreerime boti enda sõnumeid
    if message.author == client.user:
        return

    # Võtame sõnumi detailid muutujatesse
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    # Prindime enda jaoks PyCharmis iga saadetud sõnumi
    print(f"{username} said: '{user_message}' ({channel})")

    # Kui sõnum eksisteerib ja algab !-ga, hakkame seda töötlema
    if user_message and user_message[0] == '!':
        user_message = user_message[1:]
        await send_message(message, user_message)


# Paneme boti oma tokeniga tööle
client.run('MTIyMTAxMTQ5Mjc2MjAyNjAzNA.GNSh6v.kzQ8IcRjUa5l3a5WtmVT6fMz5qxjKED-ybDvXA')  # <- siinne token enda omaga ära muuta!
