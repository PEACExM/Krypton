import discord
from discord.ext import commands


class hacker111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Moderation commands"""
  
    def help_custom(self):
		      emoji = '<:jk_mod:1050949488811978933>'
		      label = "Moderation"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Moderation__(self, ctx: commands.Context):
        """`softban` , `purge` , `purge contains` , `purge startswith` , `purge invites` , `purge user` , `mute` , `unmute` , `kick` , `warn` , `ban` , `unban` , `clone` , `nick` , `slowmode` ,  `unslowmode` , `clear` , `clear all` , `clear bots` , `clear embeds` , `clear files` , `clear mentions` , `clear images` , `clear contains` , `clear reactions` , `nuke` , `lock` , `unlock` , `hide` , `unhide` , `hideall` , `unhideall` , `audit` , `sticker` , `emojisearch` , `stickersearch` , `role` , `role temp` , `role remove` , `role delete` , `role create` , `role rename`"""