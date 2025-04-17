import discord
from discord.ext import commands
import requests
import os
from mtgsdk import Card

BOT_TOKEN = "discord_bot_token"
CHANNEL_ID = 999
initiative = {}

bot = commands.Bot(command_prefix="~", intents=discord.Intents.all())

@bot.command()
async def mtg(ctx, *arr):
    result = ""
    for x in arr:
        result = result + " " + x
    result = '"' + result.strip() + '"'
    cards = Card.where(name=result).all()
    img_data = requests.get(cards[0].image_url).content
    with open('temp_img.jpg', 'wb') as handler:
        handler.write(img_data)
    await ctx.send(file=discord.File('temp_img.jpg'))
    os.remove("temp_img.jpg")

bot.run(BOT_TOKEN)