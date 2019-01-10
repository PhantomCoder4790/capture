import discord
from discord.ext import commands

class capture:
    
    def __init__(self, bot):
    	self.bot = bot


    @commands.command(pass_context=True)
    async def capture(self,ctx,user:discord.Member):
    	author = ctx.message.author
    	
       	if user.id == '131201930117513216':

            await self.bot.say(user.mention + " YOU HAVE AVOIDED CAPTURE FOR TOO LONG SCIENCEMANCER! PREPARE TO BE RESTRAINED!" + '\n' + "*Orders numerous Serving Clones to charge The Sciencemancer while guns appear from the walls and out of the arms of other clones, while others carry swords. A final barrage of clones appears running atop the other clones' heads armed with giant fists." + '\n' + "*Hundreds of Serving Clones after finally restraining dante using their limbs and killing other servingcloens for theirs tie their cybernetic limbs around " +user.mention + "'s body to a metal chair.*" + '\n' + "One Fully restrained Sciencemancer as requested.")
        
        else:
            await self.bot.say("As you wish. Capture shall begin." + '\n' + "*Orders over more Serving Clones to assist in capturing and restraining " + user.mention + "*" + '\n' + user.mention + " has been fully restrained."

def setup(bot):
   	bot.add_cog(capture(bot))