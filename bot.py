import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot is ready. Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'🔁 Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'❌ Sync error: {e}')

@bot.tree.command(name="ping", description="Check if bot is alive")
async def ping_command(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!")

bot.run("...")  # 🔐 توکن رباتت رو اینجا بذار
