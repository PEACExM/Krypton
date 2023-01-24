from __future__ import annotations
from discord.ext import commands
from utils.Tools import *
from discord import *
from utils.config import OWNER_IDS, No_Prefix
import json, discord
import typing
from utils import Paginator, DescriptionEmbedPaginator, FieldPagePaginator, TextPaginator

from typing import Optional

#Cyg90MAh7a0
class Owner(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="slist")
    @commands.is_owner()
    async def _slist(self, ctx):
        hasanop = ([hasan for hasan in self.client.guilds])
        hasanop = sorted(hasanop,
                         key=lambda hasan: hasan.member_count,
                         reverse=True)
        entries = [
            f"`[{i}]` | [{g.name}](https://discord.com/channels/{g.id}) - {g.member_count}"
            for i, g in enumerate(hasanop, start=1)
        ]
        paginator = Paginator(source=DescriptionEmbedPaginator(
            entries=entries,
            description="",
            title=f"Server List of Krypton - {len(self.client.guilds)}",
            color=0x2f3136,
            per_page=10),
                              ctx=ctx)
        await paginator.paginate()



    @commands.command(name="restart", help="Restarts the client.")
    @commands.is_owner()
    async def _restart(self, ctx: Context):
        await ctx.reply("Restarting!")
        restart_program()

    @commands.command(name="sync", help="Syncs all database.")
    @commands.is_owner()
    async def _sync(self, ctx):
        await ctx.reply("Syncing...", mention_author=False)
        with open('anti.json', 'r') as f:
            data = json.load(f)
        for guild in self.client.guilds:
            if str(guild.id) not in data['guild']:
                data['guilds'][str(guild.id)] = 'on'
                with open('anti.json', 'w') as f:
                    json.dump(data, f, indent=4)
            else:
                pass
        with open('config.json', 'r') as f:
            data = json.load(f)
        for op in data["guilds"]:
            g = self.client.get_guild(int(op))
            if not g:
                data["guilds"].pop(str(op))
                with open('config.json', 'w') as f:
                    json.dump(data, f, indent=4)

    @commands.group(name="blacklist",
                    help="let's you add someone in blacklist",
                    aliases=["bl"])
    @commands.is_owner()
    async def blacklist(self, ctx):
        if ctx.invoked_subcommand is None:
            with open("blacklist.json") as file:
                blacklist = json.load(file)
                entries = [
                    f"`[{no}]` | <@!{mem}> (ID: {mem})"
                    for no, mem in enumerate(blacklist['ids'], start=1)
                ]
                paginator = Paginator(source=DescriptionEmbedPaginator(
                    entries=entries,
                    title=
                    f"List of Blacklisted users of Krypton - {len(blacklist['ids'])}",
                    description="",
                    per_page=10,
                    color=0x2f3136),
                                      ctx=ctx)
                await paginator.paginate()

    @blacklist.command(name="add")
    @commands.is_owner()
    async def blacklist_add(self, ctx: Context, member: discord.Member):
        try:
            with open('blacklist.json', 'r') as bl:
                blacklist = json.load(bl)
                if str(member.id) in blacklist["ids"]:
                    embed = discord.Embed(
                        title="Error!",
                        description=f"{member.name} is already blacklisted",
                        color=discord.Colour(0x2f3136))
                    await ctx.reply(embed=embed, mention_author=False)
                else:
                    add_user_to_blacklist(member.id)
                    embed = discord.Embed(
                        title="Blacklisted",
                        description=f"Successfully Blacklisted {member.name}",
                        color=discord.Colour(0x2f3136))
                    with open("blacklist.json") as file:
                        blacklist = json.load(file)
                        embed.set_footer(
                            text=
                            f"There are now {len(blacklist['ids'])} users in the blacklist"
                        )
                        await ctx.reply(embed=embed, mention_author=False)
        except:
            embed = discord.Embed(title="Error!",
                                  description=f"An Error Occurred",
                                  color=discord.Colour(0x2f3136))
            await ctx.reply(embed=embed, mention_author=False)

    @blacklist.command(name="remove")
    @commands.is_owner()
    async def blacklist_remove(self, ctx, member: discord.Member = None):
        try:
            remove_user_from_blacklist(member.id)
            embed = discord.Embed(
                title="User removed from blacklist",
                description=
                f"<:GreenTick:1029990379623292938> | **{member.name}** has been successfully removed from the blacklist",
                color=0x2f3136)
            with open("blacklist.json") as file:
                blacklist = json.load(file)
                embed.set_footer(
                    text=
                    f"There are now {len(blacklist['ids'])} users in the blacklist"
                )
                await ctx.reply(embed=embed, mention_author=False)
        except:
            embed = discord.Embed(
                title="Error!",
                description=f"**{member.name}** is not in the blacklist.",
                color=0x2f3136)
            embed.set_thumbnail(url=f"{self.client.user.display_avatar.url}")
            await ctx.reply(embed=embed, mention_author=False)

    @commands.group(
        name="np",
        help="Allows you to add someone in no prefix list (owner only command)"
    )
    @commands.is_owner()
    async def _np(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)

    @_np.command(name="list")
    @commands.is_owner()
    async def np_list(self, ctx):
        with open("info.json") as f:
            np = json.load(f)
            nplist = np["np"]
            npl = ([await self.client.fetch_user(nplu) for nplu in nplist])
            npl = sorted(npl, key=lambda nop: nop.created_at)
            entries = [
                f"`[{no}]` | [{mem}](https://discord.com/users/{mem.id}) (ID: {mem.id})"
                for no, mem in enumerate(npl, start=1)
            ]
            paginator = Paginator(source=DescriptionEmbedPaginator(
                entries=entries,
                title=f"No Prefix of Krypton - {len(nplist)}",
                description="",
                per_page=10,
                color=0x2f3136),
                                  ctx=ctx)
            await paginator.paginate()

    @_np.command(name="add", help="Add user to no prefix")
    @commands.is_owner()
    async def np_add(self, ctx, user: discord.User):
        with open('info.json', 'r') as idk:
            data = json.load(idk)
        np = data["np"]
        if user.id in np:
            embed = discord.Embed(
                description=
                f"**The User You Provided Already In My No Prefix**",
                color=0x2f3136)
            await ctx.reply(embed=embed)
            return
        else:
            data["np"].append(user.id)
        with open('info.json', 'w') as idk:
            json.dump(data, idk, indent=4)
            embed1 = discord.Embed(
                description=
                f"<:GreenTick:1029990379623292938> | Added no prefix to {user} for all",
                color=0x2f3136)
           # embed1.set_thumbnail(url=f"{self.client.user.display_avatar.url}")
            await ctx.reply(embed=embed1)

    @_np.command(name="remove", help="Remove user from no prefix")
    @commands.is_owner()
    async def np_remove(self, ctx, user: discord.User):
        with open('info.json', 'r') as idk:
            data = json.load(idk)
        np = data["np"]
        if user.id not in np:
            embed = discord.Embed(
                description="**{} is not in no prefix!**".format(user),
                color=0x2f3136)
            await ctx.reply(embed=embed)
            return
        else:
            data["np"].remove(user.id)
        with open('info.json', 'w') as idk:
            json.dump(data, idk, indent=4)
            embed2 = discord.Embed(
                description=
                f"<:GreenTick:1029990379623292938> | Removed no prefix from {user} for all",
                color=0x2f3136)

            await ctx.reply(embed=embed2)

    @commands.group(name="bdg", help="Allows owner to add badges for a user")
    @commands.is_owner()
    async def _badge(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)

    @_badge.command(name="add",
                    aliases=["give"],
                    help="Add some badges to a user.")
    @commands.is_owner()
    async def badge_add(self, ctx, member: discord.Member, *, badge: str):
        ok = getbadges(member.id)
        if badge.lower() in ["own", "owner", "king"]:
            idk = "*<:RC_OWNER:1025209930719969382> Owner*"
            ok.append(idk)
            makebadges(member.id, ok)
            embed2 = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Added `Owner` Badge To {member}**",
                color=0x2f3136)
            await ctx.reply(embed=embed2)
        elif badge.lower() in ["staff", "support staff"]:
            idk = "*<:jr_staff:1025210867987521557> Staff*"
            ok.append(idk)
            makebadges(member.id, ok)
            embed3 = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Added `Staff` Badge To {member}**",
                color=0x2f3136)
            await ctx.reply(embed=embed3)
        elif badge.lower() in ["partner"]:
            idk = "*<a:_partner:1025211207566753914> Partner*"
            ok.append(idk)
            makebadges(member.id, ok)
            embed4 = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Added `Partner` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed4)
        elif badge.lower() in ["sponsor"]:
            idk = "*<:Krypton_spo:1025212082532122685> Sponsor*"
            ok.append(idk)
            makebadges(member.id, ok)
            embed5 = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Added `Sponsor` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed5)
        elif badge.lower() in [
                "friend", "friends", "homies", "owner's friend"
        ]:
            idk = "*<:RC_FRIENDS:1025209342674346097> Owner`s Friends*"
            ok.append(idk)
            makebadges(member.id, ok)
            embed1 = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Added `Owner's Friend` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed1)
        elif badge.lower() in ["early", "supporter", "support"]:
            idk = "*<a:early:1002225237292744784> Early Supporter*"
            ok.append(idk)
            makebadges(member.id, ok)
            embed6 = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Added `Early Supporter` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed6)

        elif badge.lower() in ["vip"]:
            idk = "*<a:durex_vip:1025212603909296129> Vip*"
            ok.append(idk)
            makebadges(member.id, ok)
            embed7 = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Added `VIP` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed7)

        elif badge.lower() in ["bug", "hunter"]:
            idk = "*<a:Krypton_1212:1002017580569084037> Bug Hunter*"
            ok.append(idk)
            makebadges(member.id, ok)
            embed8 = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Added `Bug Hunter` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed8)
        elif badge.lower() in ["all"]:
            idk = "*<:RC_OWNER:1025209930719969382> Owner\n<:jr_staff:1025210867987521557> Staff\n<a:_partner:1025211207566753914> Partner\n<:Krypton_spo:1025212082532122685> Sponsor\n<:RC_FRIENDS:1025209342674346097> Owner`s Friends\n<a:early:1002225237292744784> Early Supporter\n<a:durex_vip:1025212603909296129> Vip\n<a:Krypton_1212:1002017580569084037> Bug Hunter*"
            ok.append(idk)
            makebadges(member.id, ok)
            embedall = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Added `All` Badges To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embedall)
        else:
            hacker = discord.Embed(
                                   description="**Invalid Badge**",
                                   color=0x2f3136)
            
            await ctx.reply(embed=hacker)

    @_badge.command(name="remove",
                    help="Remove badges from a user.",
                    aliases=["re"])
    @commands.is_owner()
    async def badge_remove(self, ctx, member: discord.Member, *, badge: str):
        ok = getbadges(member.id)
        if badge.lower() in ["own", "owner", "king"]:
            idk = "*<:RC_OWNER:1025209930719969382> Owner*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed2 = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Removed `Owner` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed2)

        elif badge.lower() in ["staff", "support staff"]:
            idk = "*<:jr_staff:1025210867987521557> Staff*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed3 = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Removed `Staff` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed3)

        elif badge.lower() in ["partner"]:
            idk = "*<a:_partner:1025211207566753914> Partner*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed4 = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Removed `Partner` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed4)

        elif badge.lower() in ["sponsor"]:
            idk = "*<:Krypton_spo:1025212082532122685> Sponsor*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed5 = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Removed `Sponsor` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed5)

        elif badge.lower() in [
                "friend", "friends", "homies", "owner's friend"
        ]:
            idk = "*<:friends:993857133852495962> Owner's Friend*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed1 = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Removed `Owner's Friend` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed1)

        elif badge.lower() in ["early", "supporter", "support"]:
            idk = "*<a:early:1002225237292744784> Early Supporter*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed6 = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Removed `Early Supporter` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed6)

        elif badge.lower() in ["vip"]:
            idk = "*<a:durex_vip:1025212603909296129> Vip*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed7 = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Removed `VIP` Badge To {member}**",
                color=0x2f3136)
           
            await ctx.reply(embed=embed7)

        elif badge.lower() in ["bug", "hunter"]:
            idk = "*<a:Krypton_1212:1002017580569084037> Bug Hunter*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embed8 = discord.Embed(
                
                description=
                f"**Successfully Removed `Bug Hunter` Badge To {member}**",
                color=0x2f3136)
            
            await ctx.reply(embed=embed8)
        elif badge.lower() in ["all"]:
            idk = "*<:RC_OWNER:1025209930719969382> Owner\n<:jr_staff:1025210867987521557> Staff\n<a:_partner:1025211207566753914> Partner\n<:Krypton_spo:1025212082532122685> Sponsor\n<:RC_FRIENDS:1025209342674346097> Owner`s Friends\n<a:early:1002225237292744784> Early Supporter\n<a:durex_vip:1025212603909296129> Vip\n<a:Krypton_1212:1002017580569084037> Bug Hunter*"
            ok.remove(idk)
            makebadges(member.id, ok)
            embedall = discord.Embed(
                
                description=
                f"<:GreenTick:1029990379623292938> | **Successfully Removed `All` Badges From {member}**",
                color=0x2f3136)
            await ctx.reply(embed=embedall)
        else:
            hacker = discord.Embed(
                                   description="**Invalid Badge**",
                                   color=0x2f3136)
            await ctx.reply(embed=hacker)




    @commands.command()
    @commands.is_owner()
    async def dm(self, ctx, user: discord.User, *, message: str):
        """ DM the user of your choice """
        try:
            await user.send(message)
            await ctx.send(f"<:GreenTick:1029990379623292938> | Successfully Sent a DM to **{user}**")
        except discord.Forbidden:
            await ctx.send("This user might be having DMs blocked or it's a bot account...")           



    @commands.group()
    @commands.is_owner()
    async def change(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))
            
            
    @change.command(name="nickname")
    @commands.is_owner()
    async def change_nickname(self, ctx, *, name: str = None):
        """ Change nickname. """
        try:
            await ctx.guild.me.edit(nick=name)
            if name:
                await ctx.send(f"<:GreenTick:1029990379623292938> | Successfully changed nickname to **{name}**")
            else:
                await ctx.send("<:GreenTick:1029990379623292938> | Successfully removed nickname")
        except Exception as err:
            await ctx.send(err)



    @commands.command()
    @commands.is_owner()
    async def globalban(self, ctx, *, user: discord.User = None):
        if user is None:
            return await ctx.send(
                "You need to define the user"
            )
        for guild in self.client.guilds:
            for member in guild.members:
                if member == user:
                    await user.ban(reason="lund le lo")
               
        
