"""
NekoTPy Basic Bot
~~~~~~~~~~~~~~~~~

A basic Bot example to be ran on module execution.

:license: (c) 2024 NekoMimiOfficial Apache2
for more licensing info lookup the LICENSE
"""

class BotExample:
    def __init__(self, token: str):
        self.token = token

    def run(self):
        print("NekoTPy Bot")
        print("~~~~~~~~~~~")
        print("           ")
        print("No implementaion of the builtin bot yet.")
        print("please wait for version 1.1.8")
        exit(0)

TKN = input("TOKEN> ")
for i in range(140):
    print("  ")
bot = BotExample(TKN)
bot.run()
