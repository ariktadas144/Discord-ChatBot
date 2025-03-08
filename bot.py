import discord
from discord.ext import commands

TOKEN = "Actual_Discord_Bot_Token"

# Enable necessary intents
intents = discord.Intents.default()
intents.messages = True  # Enables reading messages
intents.message_content = True  # REQUIRED for reading message content
intents.guilds = True  # Allows detecting server-related events

# Create bot instance with command prefix
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm your bot.")

bot.run(TOKEN)
