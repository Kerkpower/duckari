# duckari

A Hikari command handler made with love by ducks.

Currently Duckari is work in progress.

Documentation is WIP.

The wiki is no longer used as documentation.

NOT a Working example:

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

- commands
- everything other than listeners

### This is work in progress!
