import os
import discord
from dotenv import load_dotenv
import requests
import json
import asyncio
import Naked
from shutil import rmtree

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client()
count = os.getenv('COUNT')

cd1 = "D:"
cd2 = "cd D:\\PythonProjectsSummer2021\\oh_counter\\"


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:
        print(guild)


@bot.event
async def on_message(message):
    channel = message.channel
    tiktok_header = "https://vm.tiktok.com"
    if tiktok_header in message.content:
        await channel.send("fuck you download it yourself next time ")
        # getting only the link from the message
        stripped = message.content.rsplit("/")
        link = stripped[0] + "//" + stripped[2] + "/" + stripped[3] + "/"
        # print(link)
        # setting name of folder using datetime object
        name = message.created_at
        date = str(name.month) + "." + str(name.day) + "." + str(name.year)
        time = str(name.hour) + "." + str(name.minute) + "." + str(name.second)
        # print(date + "_" + time)
        name = str(date + "_" + time)
        # actual command
        command = f'tiktok-scraper video -d {link} --filepath D:\\PythonProjectsSummer2021\\oh_counter\\{name}'
        # print(command)

        os.system(cd1)
        os.system(cd2)
        os.mkdir(name)
        os.system(command)

        # upload video
        # os.system("cd D:\\PythonProjectsSummer2021\\oh_counter\\{name}\\")
        x = os.listdir(f'D:\PythonProjectsSummer2021\oh_counter\\{name}')
        # print(x[0])
        await channel.send(file=discord.File(f'D:\\PythonProjectsSummer2021\\oh_counter\\{name}\\{x[0]}'))

        rmtree(f'D:\PythonProjectsSummer2021\oh_counter\\{name}')


bot.run(TOKEN)
