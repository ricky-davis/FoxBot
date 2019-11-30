"""
Main File to start FoxBot
"""
import datetime
import sys
import traceback
import discord

from custom_config import CustomConfig


DESCRIPTION = """
Hello! I am FoxBot. Ow Boy!
"""

class FoxBot(discord.Client):
    """
    FoxBot responds "ow boy" to certain things.
    """

    async def on_message(self, message):
        user_id = self.user.id
        base = [f'<@!{user_id}>', f'<@{user_id}>',\
            f'<@!185119394471477248>',f'<@185119394471477248>',\
            'ow boy','ow boi']

        mc = message.content.lower()
        if not message.author.bot:
            if (mc in base):
                await message.channel.send("ow boy")


if __name__ == "__main__":
    DISCORDBOT = FoxBot()
    DISCORDBOT.run(CustomConfig.botToken)
    