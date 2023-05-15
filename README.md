# NekoMimi Telegram Python Module
```
 ^ ^   NekoTPy API wrapper           (Glameow used wrap!)
=UwU=  This software is distributed without any warranty.
 w w   NekoMimi (c) 2023 in collab with The NekOS Project
```

isn't it time to create a Telegram API wrapper that is a bit easier to write?  
that's what NekoTPy aims to do !  
_sorry NekoTPy isnt async ready atm_  
NekoTPy boasts wonderful features that guarantee a faster and more powerful bot development experience, as the majority of Telegram bot API wrappers require you to manually add the command and setup a form of dispatcher, NekoTPy completely makes that syntax obsolete by using command wrapper decorators and context objects so adding a command can be as simple as.. well.. doing absolutley NOTHING! and sending files/getting IDs and arguments can all be done through 1 simple context object  
what about running the event listener? you just `.run()` it :) (more about it in the docs and also below in the examples)  

docs are available [here](https://github.com/NekoMimiOfficial/NekoTPy/blob/main/Docs/README.md)  


# ToDo and Progress
```
(x) updater and event listener
( ) v2 async updater: 0%
(x) botv1(idiotic)
( ) botv2(multiP): 70%
( ) botv3(async): 0%
```
botv1 list
```
(x) send
(x) updater
(x) basic context object
(x) each command has its own event listener [don't ask]
(x) fixed update offset
(x) fixed update poll size
(x) temporary global update ID fix

hey.. this was just a proof of concept
```

botv2 list
```
(x) ctx constants
(x) ctx send
(x) ctx upload
(x) ctx get file
(x) ctx sendPhoto
(x) ctx keyboard markup
( ) ctx wait for response: 99% [testing required]
(x) command queue
( ) wait queue: 99% [testing required]
(x) global event listener
(D) event parser: 70% [add other types of events] [dropped for v3]
(x) updater
( ) for once finally fix the GUID: 99% [testing required]

once again I'm not proud of this but it's another improvement
```

botv3 list
```
( ) async command queue
( ) async event queue
( ) for once finally create a clean context object
( ) ctx constants [includes IDs and args and file IDs]
( ) ctx send [includes markup and keyboard and docs and photo etc]
( ) ctx link
( ) ctx wait for response
( ) main updater object
( ) event parser
( ) event context
( ) send message event
( ) user join event
( ) user leave event
( ) moar events
( ) yet again even a cleaner GUID system

things should start to look cleaner in this version
```

# botv2 example
```python
from NekoTPy import v2

Bot = v2.Bot(TOKEN)

@Bot.Command
def _ping(ctx):
    ctx.send("pong", mention=True)

Bot.run()
```
wait.. THAT'S IT?! THAT'S TINY!  
yes! NekoTPy's syntax is amazingly compact so creating and running a bot instance can be done in only 2 lines  
I like to also add a `Bot.stop()` in a `while input() == "stop"` loop or after an `input()` since the event listener is a different process than your main code process that way you can do things while your bot is running like for example running a stat monitor using botv1 features or making a simple bot shell which is what I did  
so you can add this code to the end of the file and expand on what you want it to do  
```python
com = input(">")
while not com.startswith("quit"):
    pass #write your simple shell here
    com = input(">")
Bot.stop()
```

# Contact info
Email: nekomimi@tilde.team  
Discord : NekoMimi#7225  
Reddit: @NekoMimiOfficial  
