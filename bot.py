import os
import discord
import openai
from discord.ext import commands

# Manually set the tokens here (Replace with actual values)
DISCORD_TOKEN = "MTM0Nzk3NzU5ODczNDY5NjYwMg.GajiLT.2RnwH3R85CPEpMflPFtZWKhsRTodG0I9krantI"
OPENAI_API_KEY = "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"

# Check if the tokens are set
if not DISCORD_TOKEN or not OPENAI_API_KEY:
    raise ValueError("ERROR: DISCORD_BOT_TOKEN or OPENAI_API_KEY is missing! Set them manually.")

# Set up OpenAI API
openai.api_key = OPENAI_API_KEY

# Enable required Discord intents
intents = discord.Intents.default()
intents.message_content = True  # REQUIRED for reading messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def chat(ctx, *, message: str):
    """Responds using OpenAI API"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a helpful AI."},
                      {"role": "user", "content": message}]
        )
        reply = response["choices"][0]["message"]["content"]
        await ctx.send(reply)
    except Exception as e:
        await ctx.send("⚠️ Error occurred while processing your request.")
        print(f"Error: {e}")

bot.run(DISCORD_TOKEN)
