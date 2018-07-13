import discord
import bfd

with open('config.txt') as f:
    config = [g.strip('\r\n ') for g in f.readlines()]

bot_client = discord.Client()
bfd_client = bfd.Client(bot_client, config[1])

@bot_client.event
async def on_ready():
    print('Logged in as')
    print(bot_client.user.name)
    print(bot_client.user.id)
    print('------')

@bot_client.event
async def on_message(message):
    if message.content.startswith('!get'):
        id = message.content.split(" ")[-1]

        info = await bfd_client.get_bot(id)
        if info is None:
            await bot_client.send_message(message.channel, "Can't find this bot on BFD")
            return

        embed = discord.Embed(title="BotInfo")
        for key, value in info.as_dict().items():
            if key == "" or value == "":
                continue

            embed.add_field(name=key, value=str(value))

        await bot_client.send_message(message.channel, embed=embed)

    elif message.content.startswith('!post'):
        result = await bfd_client.post_count()

        await bot_client.send_message(message.channel, str(result))

bot_client.run(config[0])