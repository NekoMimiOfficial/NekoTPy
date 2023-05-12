# NekoMimi Telegram Python Module
```
 ^ ^   NekoTPy API wrapper
=UwU=  This software is distributed without warranty
 w w   NekoMimi (c) 2023
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
( ) ctx wait for response: 60% [help]
(x) command queue
( ) wait queue: 20% [help]
(x) global event listener
( ) event parser: 70% [add other types of events]
(x) updater
( ) for once finally fix the GUID: 0%

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

# Contact info
Email: nekomimi@tilde.team  
Discord : NekoMimi#7225  
Reddit: @NekoMimiOfficial  
