# duckari

A Hikari command handler for people who love ducks.

Currently Duckari is work in progress.

Documentation is WIP.

The wiki is not longer used as documentation.

Working example:

```py
from duckari import duck

bot = duck.Bot(prefix="!") # prefix is None because we are only using slash commands

@bot.command()
async def lol(ctx):
    await ctx.send("hi")
token = ""
bot.run(token)
```

## Things that don't work yet

- slash commands
- ctx.say
- ctx.reply
- a lot of stuff
- event listener

### This is work in progress!
