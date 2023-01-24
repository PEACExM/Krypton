from __future__ import annotations
from core import Astroz



#____________ Commands ___________

#####################3
from .commands.help import Help
from .commands.general import General
from .commands.music import Music
from .commands.moderation import Moderation
from .commands.anti import Security
from .commands.raidmode import Automod
from .commands.welcome import Welcomer
from .commands.fun import Fun
from .commands.Games import Games
from .commands.extra import Utility
from .commands.owner import Owner
from .commands.vcroles import Voice
from .commands.role import Server
from .commands.nsfw import Nsfw
from .commands.ignore import Ignore
from .commands.vanityroles import Vanityroles

#____________ Events _____________
from .events.antiban import antiban
from .events.antichannel import antichannel
from .events.antiguild import antiguild
from .events.antirole import antirole
from .events.antibot import antibot
from .events.antikick import antikick
from .events.antiprune import antiprune
from .events.antiwebhook import antiwebhook
from .events.antiping import antipinginv
from .events.antiemostick import antiemostick
from .events.antintegration import antintegration
from .events.antispam import AntiSpam
from .events.autoblacklist import AutoBlacklist
from .events.antiemojid import antiemojid
from .events.antiemojiu import antiemojiu
from .events.Errors import Errors
from .events.on_guild import Guild
from .events.autorole import Autorole2
from .events.greet2 import greet
from .events.voiceupdate import Vcroles2


##############33cogs#############
from .commands.anti1 import hacker1
from .commands.general1 import hacker11
from .commands.music1 import hacker111
from .commands.raidmode1 import hacker1111
from .commands.welcome1 import hacker11111
#from .commands.logging2 import hacker111111
from .commands.Nsfw2 import hacker1111111
from .commands.server import hacker11111111
from .commands.mod2 import hacker111111111
from .commands.games1 import hacker1111111111
from .commands.extra1 import hacker11111111111
from .commands.voice import hacker111111111111
from .commands.vcrole1 import hacker1111111111111








async def setup(bot: Astroz):
  await bot.add_cog(Help(bot))
  await bot.add_cog(General(bot))
  await bot.add_cog(Music(bot))
  await bot.add_cog(Moderation(bot))
  await bot.add_cog(Security(bot))
  await bot.add_cog(Automod(bot))
  await bot.add_cog(Welcomer(bot))
  await bot.add_cog(Fun(bot))
  await bot.add_cog(Games(bot))
  await bot.add_cog(Utility(bot))
  await bot.add_cog(Voice(bot))
  await bot.add_cog(Owner(bot))
  await bot.add_cog(Server(bot))
  await bot.add_cog(Nsfw(bot))
  await bot.add_cog(Vanityroles(bot))
  await bot.add_cog(Ignore(bot))

####################



  await bot.add_cog(hacker1(bot))
  await bot.add_cog(hacker11(bot))  
  await bot.add_cog(hacker111(bot))
  await bot.add_cog(hacker1111(bot))
  await bot.add_cog(hacker11111(bot))
  await bot.add_cog(hacker1111111(bot))
  await bot.add_cog(hacker11111111(bot))
  await bot.add_cog(hacker111111111(bot))
  await bot.add_cog(hacker1111111111(bot))
  await bot.add_cog(hacker11111111111(bot))  
  await bot.add_cog(hacker111111111111(bot))  
  await bot.add_cog(hacker1111111111111(bot))


    
###########################events################3
  
  await bot.add_cog(antiban(bot))
  await bot.add_cog(antichannel(bot))
  await bot.add_cog(antiguild(bot))
  await bot.add_cog(antirole(bot))
  await bot.add_cog(antibot(bot))
  await bot.add_cog(antikick(bot))
  await bot.add_cog(antiprune(bot))
  await bot.add_cog(antiwebhook(bot))
  await bot.add_cog(antipinginv(bot))
  await bot.add_cog(antiemostick(bot))
  await bot.add_cog(antintegration(bot))  
  await bot.add_cog(AntiSpam(bot))
  await bot.add_cog(AutoBlacklist(bot))
  await bot.add_cog(antiemojid(bot))
  await bot.add_cog(antiemojiu(bot))
  await bot.add_cog(Guild(bot))
  await bot.add_cog(Errors(bot))
  await bot.add_cog(Autorole2(bot))
  await bot.add_cog(greet(bot))
  await bot.add_cog(Vcroles2(bot))