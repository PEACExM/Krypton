import discord
from discord.ext import commands


class hacker11111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Extra commands"""
  
    def help_custom(self):
		      emoji = '<:jk_utility:1050949989771264011>'
		      label = "Utility"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Utility__(self, ctx: commands.Context):
        """`stats` , `invite` , `serverinfo` , `userinfo` , `roleinfo` , `botinfo` , `status` , `emoji` , `user` , `role` , `channel` , `boosts`, `emoji-add` , `removeemoji` , `unbanall` ,  `joined-at` , `ping` , `github` , `vcinfo` , `channelinfo` , `note` , `notes` , `trashnotes` , `badges` , `list boosters` , `list inrole` , `list emojis` , `list bots` , `list admins` , `list invoice` , `list mods` , `list early` , `list activedeveloper` , `list createpos` , `list roles` , `ignore` , `ignore channel` , `ignore channel add` , `ignore channel remove` , `banner user` , `banner server`"""