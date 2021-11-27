# hikari-duck
A Hikari command handler for people who love ducks.

Currently Hikari Duck is work in progress.

Working example:
```py
from hikariduck import duck

bot = duck.Bot(prefix="!") # prefix is None because we are only using slash commands

@bot.command()
async def lol(ctx):
    await ctx.send("hi")
token = "OTEzNDg2OTA2NTE0MzY2NDk1.YZ_M-g.-d4Ayr3eQFCL-GosACPC-cMrcKI"
bot.run(token)
```

## Things that don't work yet

- slash commands
- ctx.say
- ctx.reply
- a lot of stuff
- event listener

### This is work in progress!
