import discord
from bot_logic import gen_pass
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))


@bot.command()
async def coin(ctx):
    result = random.choice(["HEADS", "TAILS"])
    await ctx.send(f'🪙 Coinflip result: **{result}**')

@bot.command()
async def dice(ctx):
    number = random.randint(1, 6)
    await ctx.send(f'🎲 You rolled: **{number}**')

@bot.command()
async def emoji(ctx):
    emojis = ["😀", "🔥", "🐱", "🌙", "🍀", "🚀", "⭐", "😎"]
    await ctx.send(random.choice(emojis))


bot.run("MTQzNjMzNDcwNzcwMzkzOTE0Mw.GvsV_c.4yFMYHImIzhLJH_6K5_oHp2c3GptVJYj1bjU1A")
