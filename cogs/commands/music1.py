import discord
from discord.ext import commands


class hacker111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Music commands"""
  
    def help_custom(self):
		      emoji = '<:jk_music:1050948864422707240>'
		      label = "Music"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Music__(self, ctx: commands.Context):
        """`play` , `connect` , `disconnect` , `stop` , `skip`   ,  `pause` ,  `resume` , `bassboost`  , `move` , `volume` , `nowplaying` , `shuffle` , `pull` , `queue` , `queue clear` , `seek`"""