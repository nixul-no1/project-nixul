import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

channel_id = 123456789  # 구매후기 채널

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id == channel_id:
        await message.add_reaction('❤️')  # 후기메세지 이모티콘
        await message.reply("후기를 남겨주셔서 감사합니다! 앞으로도 만족스러운 서비스를 제공할 수 있도록 노력하겠습니다.")  # 구매후기 답장 메세지

    await bot.process_commands(message)

bot.run('봇토큰')
