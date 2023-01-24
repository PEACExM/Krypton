import discord
from discord.ext import commands


class hacker1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Security commands"""
  
    def help_custom(self):
		      emoji = '<:jk_securitu:1050948746344681572>'
		      label = "AntiNuke"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __AntiNuke__(self, ctx: commands.Context):
        """`antinuke` , `antinuke enable` , `antinuke disable` , `antinuke show` , `antinuke punishment set` , `antinuke whitelist add` , `antinuke whitelist remove` , `antinuke whitelist show` , `antinuke whitelist reset` , `antinuke channelclean` , `antinuke roleclean` , `antinuke wl role`"""