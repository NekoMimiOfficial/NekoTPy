# NekoMimi Telegram Python Module
```
 ^ ^   NekoTPy API wrapper         (Glameow used wrap!)
=UwU=  Better Telegram wrappers are a must lets NekoTPy
 w w   NekoMimi (c) 2024 Apache2 license, fair use only
```

<img src="./banner.png">

isn't it time to create a Telegram API wrapper that is a bit easier to write?  
that's what NekoTPy aims to do !  
NekoTPy boasts wonderful features that guarantee a faster and more powerful bot development experience, as the majority of Telegram bot API wrappers require you to manually add the command and setup a form of dispatcher, NekoTPy completely makes that syntax obsolete by using command wrapper decorators and context objects so adding a command can be as simple as.. well.. doing absolutley NOTHING! and sending files/getting IDs and arguments can all be done through 1 simple context object  
what about running the event listener? you just `.run()` it :) (more about it in the docs and also below in the examples)  
* NekoTPy's codebase is heavily inspired by Rapptz's Discord.py wrapper thus the operations are very similar  

docs are available [here](https://github.com/NekoMimiOfficial/NekoTPy/blob/main/Docs/README.md)  


# ToDo and Progress
-> current progress: Asyncio port  
* list found at [ToDo](https://github.com/NekoMimiOfficial/NekoTPy/blob/main/TODO.md) 

# botv2 example
```python
from NekoTPy.legacy import v2

Bot = v2.Bot(TOKEN)

@Bot.Command
def _ping(ctx):
    ctx.send("pong", mention=True)

Bot.run()
```
wait.. THAT'S IT?! THAT'S TINY!  
yes! NekoTPy's syntax is amazingly compact so creating and running a bot instance can be done in only 2 lines  

* More changes to come as the asyncio port progresses  

# Contact info
Email: `nekomimi@tilde.team`  
Discord : `nekomimiofficial`  
Reddit: `@NekoMimiOfficial`  
