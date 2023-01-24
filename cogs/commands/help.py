import discord
from discord.ext import commands
from difflib import get_close_matches
from contextlib import suppress
from core import Context
from core.Astroz import Astroz
from core.Cog import Cog
from utils.Tools import getConfig
from itertools import chain
from utils import *
import json
from utils import help as vhelp
from utils import Paginator, DescriptionEmbedPaginator, FieldPagePaginator, TextPaginator

client = Astroz()


class HelpCommand(commands.HelpCommand):

    async def on_help_command_error(self, ctx, error):
        damn = [
            commands.CommandOnCooldown, commands.CommandNotFound,
            discord.HTTPException, commands.CommandInvokeError
        ]
        if not type(error) in damn:
            await self.context.reply(
                f"Unknown Error Occurred\n{error.original}",
                mention_author=False)
        else:
            if type(error) == commands.CommandOnCooldown:
                return

                return await super().on_help_command_error(ctx, error)

    async def command_not_found(self, string: str) -> None:
        with open('blacklist.json', 'r') as f:
            data = json.load(f)
        if str(self.context.author.id) in data["ids"]:
            embed = discord.Embed(
                title="<:error_ok:946729104126922802> Blacklisted",
                description=
                "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/D78YMq279a)",
                color=0x2f3136)
            await self.context.reply(embed=embed, mention_author=False)
        else:

            if string in ("security", "anti","antinuke"):
                cog = self.context.bot.get_cog("Antinuke")
                with suppress(discord.HTTPException):
                    await self.send_cog_help(cog)
            else:
                msg = f"Command `{string}` is not found...\n"
                hacker = await self.context.bot.fetch_user(143853929531179008)
                cmds = (str(cmd) for cmd in self.context.bot.walk_commands())
                mtchs = get_close_matches(string, cmds)
                if mtchs:
                    for okaay, okay in enumerate(mtchs, start=1):
                        msg += f"Did You Mean: \n`[{okaay}]`. `{okay}`\n"
                embed1 = discord.Embed(
                    color=0x2f3136,
                    title=f"Command `{string}` is not found...\n",
                    description=f"Did You Mean: \n`[{okaay}]`. `{okay}`\n")
                embed1.set_footer(text=f"Made By {hacker}",
                                  icon_url=hacker.display_avatar.url)
                return None

    async def send_bot_help(self, mapping):
        await self.context.typing()
        with open('ignore.json', 'r') as heck:
            randi = json.load(heck)
        with open('blacklist.json', 'r') as f:
            bled = json.load(f)
        if str(self.context.author.id) in bled["ids"]:
            embed = discord.Embed(
                title="<:error_ok:1002376341959757884> Blacklisted",
                description=
                "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/D78YMq279a)",
                color=0x2f3136)
            return await self.context.reply(embed=embed, mention_author=False)
        elif str(self.context.channel.id) in randi["ids"]:
            return None
        data = getConfig(self.context.guild.id)
        prefix = data["prefix"]
        perms = discord.Permissions.none()
        perms.read_messages = True
        perms.external_emojis = True
        perms.send_messages = True
        perms.manage_roles = True
        perms.manage_channels = True
        perms.ban_members = True
        perms.kick_members = True
        perms.manage_messages = True
        perms.embed_links = True
        perms.read_message_history = True
        perms.attach_files = True
        perms.add_reactions = True
        perms.administrator = True
        inv = discord.utils.oauth_url(self.context.bot.user.id,
                                      permissions=perms)
        filtered = await self.filter_commands(self.context.bot.walk_commands(),
                                              sort=True)
        hacker = await self.context.bot.fetch_user(143853929531179008)
        embed = discord.Embed(
            title="Help Command Overview :",
            description=
            f"• Prefix for this server is `{prefix}`\n• Total Commands: {len(set(self.context.bot.walk_commands()))} | Usable by you (here): {len(set(filtered))}\n• Type `{prefix}help <command | module>` for more info.\n• [Invite Krypton]({inv}) | [Support Server](https://discord.gg/D78YMq279a) | [Vote me](https://top.gg/bot/1012627088232165376/vote)",
            color=0x2f3136)
        embed.set_thumbnail(url=self.context.bot.user.display_avatar.url)

        embed.set_footer(text=f"Made By {hacker}",
                         icon_url=hacker.display_avatar.url)
        embed.add_field(
            name="__Main__",
            value=
            """<:jk_securitu:1050948746344681572> AntiNuke\n<a:jk_general_:1050950252850593822> General\n<:jk_music:1050948864422707240> Music\n<:jk_automod:1050949024443809852> Automod\n<a:jk_wlc:1025242738679103549> Welcomer""",
            inline=False)
        embed.add_field(
            name="__Extras__",
            value=
            """<:jk_canal_nsfw:1053691647294185543> Nsfw\n<:PartneredServerOwner:1033787680032575508> Server\n<:jk_mod:1050949488811978933> Moderation\n:cricket_game: Games\n<:jk_utility:1050949989771264011> Utility\n<:jk_voice:1050949645678940210> Voice\n<:jk_vc171771:1050950158566821999> VcRoles""",
            inline=False)
        embed.set_author(name=self.context.author.name,
                         icon_url=self.context.author.display_avatar.url)
        embed.timestamp = discord.utils.utcnow()

        view = vhelp.View(mapping=mapping,
                          ctx=self.context,
                          homeembed=embed,
                          ui=2)
        await self.context.reply(embed=embed, mention_author=False, view=view)

    async def send_command_help(self, command):
        with open('ignore.json', 'r') as heck:
            randi = json.load(heck)
        with open('blacklist.json', 'r') as f:
            data = json.load(f)
        if str(self.context.author.id) in data["ids"]:
            embed = discord.Embed(
                title="<:error_ok:1002376341959757884> Blacklisted",
                description=
                "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/D78YMq279a)",
                color=0x2f3136)
            await self.context.reply(embed=embed, mention_author=False)
        elif str(self.context.channel.id) in randi["ids"]:
            return None
        else:
            hacker = f">>> {command.help}" if command.help else '>>> No Help Provided...'
            embed = discord.Embed(
                description=
                f"""```yaml\n- [] = optional argument\n- <> = required argument\n- Do NOT Type These When Using Commands !```\n{hacker}""",
                color=0x2f3136)
            alias = ' | '.join(command.aliases)

            embed.add_field(
                name="**Aliases**",
                value=f"{alias}" if command.aliases else "No Aliases",
                inline=False)
            embed.add_field(
                name="**Usage**",
                value=f"`{self.context.prefix}{command.signature}`\n")
            embed.set_author(name=f"{command.cog.qualified_name.title()}",
                             icon_url=self.context.bot.user.display_avatar.url)
            await self.context.reply(embed=embed, mention_author=False)

    def get_command_signature(self, command: commands.Command) -> str:
        parent = command.full_parent_name
        if len(command.aliases) > 0:
            aliases = ' | '.join(command.aliases)
            fmt = f'[{command.name} | {aliases}]'
            if parent:
                fmt = f'{parent}'
            alias = f'[{command.name} | {aliases}]'
        else:
            alias = command.name if not parent else f'{parent} {command.name}'
        return f'{alias} {command.signature}'

    def common_command_formatting(self, embed_like, command):
        embed_like.title = self.get_command_signature(command)
        if command.description:
            embed_like.description = f'{command.description}\n\n{command.help}'
        else:
            embed_like.description = command.help or 'No help found...'


    async def send_group_help(self, group):
        with open('blacklist.json', 'r') as f:
            idk = json.load(f)
        with open('ignore.json', 'r') as heck:
            randi = json.load(heck)
        if str(self.context.author.id) in idk["ids"]:
            embed = discord.Embed(
                title="<:error_ok:1002376341959757884> Blacklisted",
                description=
                "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/D78YMq279a)",
                color=0x2f3136)
            await self.context.reply(embed=embed, mention_author=False)
        elif str(self.context.channel.id) in randi["ids"]:
            return None
        else:
            entries = [(
            f"`{self.context.prefix}{cmd.qualified_name}`",
            f"{cmd.short_doc if cmd.short_doc else 'No Description Provided...'}\n\n"
        ) for cmd in group.commands]
        paginator = Paginator(source=FieldPagePaginator(
            entries=entries,
            title=f"{group.qualified_name} Commands",
            description="<...> Duty | [...] Optional\n\n",
            color=0x2f3136,
            per_page=10),
                              ctx=self.context)
        await paginator.paginate()

        
    
    async def send_cog_help(self, cog):
        with open('blacklist.json', 'r') as f:
            data = json.load(f)
        with open('ignore.json', 'r') as heck:
            randi = json.load(heck)
        if str(self.context.author.id) in data["ids"]:
            embed = discord.Embed(
                title="<:error_ok:1002376341959757884> Blacklisted",
                description=
                "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/D78YMq279a)",
                color=0x2f3136)
            return await self.context.reply(embed=embed, mention_author=False)
        elif str(self.context.channel.id) in randi["ids"]:
            return None
        #await self.context.typing()
        entries = [(
            f"`{self.context.prefix}{cmd.qualified_name}`",
            f"{cmd.short_doc if cmd.short_doc else 'No Description Provided...'}\n\n"
        ) for cmd in cog.get_commands()]
        paginator = Paginator(source=FieldPagePaginator(
            entries=entries,
            title=f"{cog.qualified_name.title()} ({len(cog.get_commands())})",
            description="<...> Duty | [...] Optional\n\n",
            color=0x2f3136,
            per_page=10),
                              ctx=self.context)
        await paginator.paginate()


class Help(Cog, name="help"):

    def __init__(self, client: Astroz):
        self._original_help_command = client.help_command
        attributes = {
            'name':
            "help",
            'aliases': ['h'],
            'cooldown':
            commands.CooldownMapping.from_cooldown(1, 5,
                                                   commands.BucketType.user),
            'help':
            'Shows help about bot, a command or a category'
        }
        client.help_command = HelpCommand(command_attrs=attributes)
        client.help_command.cog = self

    async def cog_unload(self):
        self.help_command = self._original_help_command

    #def help_custom(self):
    # emoji = '<a:jk_general_:1050950252850593822>'
    # label = "Home"
    # description = ""
    # return emoji, label, description
