
# 봉순#4888 : MASS DM BOT SOURCE
# Made with Open Source


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("Your Bot is working.")
    game = discord.Game('따라하기')
    await client.change_presence(status=discord.Status.online, activity=game)

#Send dm to "/dm {message}"
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id ==416903534160642049:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="따라하기 게임중")
                        embed.add_field(name="따라하기 게임중", value=msg, inline=True)
                        embed.set_footer(text=f"discord.gg/★★Invite Code★★")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzQyOTYxMjQyNTg2NDgwNjgw.XzNukw.Bmm4AR2tDzjSW4qCsXx7D1vwqhA')
