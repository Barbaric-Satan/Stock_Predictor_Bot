import discord

from discord.ext import commands


client = commands.Bot(command_prefix = '^')


class MyClient(discord.Client):
    async def on_ready(self):
        print('logged in as: %s' % client.user.name)
        print('ID is:', client.user.id)


    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    async def karthik(self):
        print("This line is added by karthik")

client = MyClient()

client.run('ODk3MDA0NDk2NDQ4ODExMDc5.YWPWiQ.F3JhILhRcKy0I3Rx-4Be6Lpf5Bs')