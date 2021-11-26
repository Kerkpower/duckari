from hikariduck import duck
from hikariduck.command import SlashCommandArgument

bot = duck.Bot(prefix=None) # prefix is None because we are only using slash commands

@bot.slash_command(name="")
def lol():