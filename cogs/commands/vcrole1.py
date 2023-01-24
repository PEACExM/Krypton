import discord
from discord.ext import commands


class hacker1111111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Voice commands"""
  
    def help_custom(self):
		      emoji = '<:jk_vc171771:1050950158566821999>'
		      label = "VcRoles"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __VcRoles__(self, ctx: commands.Context):
        """`vcrole bots add` , `vcrole bots remove` , `vcrole bots` , `vcrole config` , `vcrole humans add` , `vcrole humans remove` , `vcrole humans` , `vcrole reset` , `vcrole`"""