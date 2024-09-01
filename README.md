# climate_change

##Идея для моего проекта:
#Создать страницу, где будут указаны основные проблемы ГП


import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import contextvars
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен и готов к работе')


@bot.command()
async def command_list(ctx):
    await ctx.send('definition, reasons, solutions, consequence')

@bot.command()
async def definition(ctx):
    await ctx.send("Global warming is the long-term warming of the planet's overall temperature. Though this warming trend has been going on for a long time, its pace has significantly increased in the last hundred years due to the burning of fossil fuels. As the human population has increased, so has the volume of fossil fuels burned.")    

@bot.command()
async def reasons(ctx):
    await ctx.send('''Here are some reasons, why is it happening:
                   Burning fossil fuels;
                   cutting down forests;
                   farming livestock.
                    Also Fluorinated gases are bad for our planet. They are found in air conditioners, aerosol sprays, refrigerators.
                   ''')
    

@bot.command()
async def solutions(ctx):
    await ctx.send('''The most popular measures against global warming:
                   Save energy at home. Much of our electricity and heat are powered by coal, oil and gas;
                   Walk, bike or take public transport;
                   Throw away less food.''')
    

@bot.command()
async def consequence(ctx):
    await ctx.send("Because of global warming people are getting sick and may die in the future. So, it is a serious problem.")





@bot.command()
async def command_list_ru(ctx):
    await ctx.send('definition_ru, reasons_ru, solutions_ru, consequence_ru')

@bot.command()
async def definition_ru(ctx):
    await ctx.send("Global warming is the long-term warming of the planet's overall temperature. Though this warming trend has been going on for a long time, its pace has significantly increased in the last hundred years due to the burning of fossil fuels. As the human population has increased, so has the volume of fossil fuels burned.")    

@bot.command()
async def reasons_ru(ctx):
    await ctx.send('''Here are some reasons, why is it happening:
                   Burning fossil fuels;
                   cutting down forests;
                   farming livestock.
                    Also Fluorinated gases are bad for our planet. They are found in air conditioners, aerosol sprays, refrigerators.
                   ''')
    

@bot.command()
async def solutions_ru(ctx):
    await ctx.send('''The most popular measures against global warming:
                   Save energy at home. Much of our electricity and heat are powered by coal, oil and gas;
                   Walk, bike or take public transport;
                   Throw away less food.''')
    

@bot.command()
async def consequence_ru(ctx):
    await ctx.send("Because of global warming people are getting sick and may die in the future. So, it is a serious problem.")

bot.run(DISCORD_TOKEN)
