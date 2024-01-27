#bot.py
import os
import dotenv

import interactions
from dotenv import load_dotenv

from game import Game

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('GUILD_ID'))

client = interactions.Client(token=TOKEN)

game = Game()

@client.event
async def on_ready():
    print(f'Client has connected to Discord!')
@interactions.slash_command(name="getstats", description="Get your player stats",scopes=[GUILD])
async def get_stats(ctx:interactions.SlashContext):
    player = game.getPlayer(ctx.member.id)
    await ctx.send(f"""Here are your player stats!{ctx.member.user.username}, here are your player stats!
    Id: {player.id}
    Attack: {player.attack}
    HP: {player.current_hp}
    XP: {player.xp}
    """)

client.start()