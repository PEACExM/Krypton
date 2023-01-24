import discord
from discord.ext import commands


class hacker11(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""
  
    def help_custom(self):
		      emoji = '<a:jk_general_:1050950252850593822>'
		      label = "General"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __General__(self, ctx: commands.Context):
        """`afk` , `avatar` , `banner` , `servericon` , `membercount` , `poll` , `hack` , `token` , `users` , `italicize` , `strike` , `quote` , `code` , `bold` , `censor` , `underline` , `gender` , `wizz` , `pikachu` , `shorten` , `urban` , `rickroll` , `hash` , `snipe` , `roleall`"""