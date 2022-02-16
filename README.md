# discordtownlistpy

~~This is an unofficial Python API Wrapper for the [Discord TownList (bot list)](https://townlist.xyz/).~~

**Update: The discord bot list is gone, and this package remains as a template for those attempting similar projects**

For your information, the site was based on an old version of vcodes.

## Posting Server Count

```py
import discordtownlistpy as dtl

...

dtl.postGuildCount(len(bot.guilds), "<YOUR_API_TOKEN>")
```

## Retrieving Bot Data

```py
import discordtownlistpy as dtl

...

@bot.command()
async def botstats(ctx, bot_id):
    bot_data = await returnBotData(bot_id)
    ...
```

