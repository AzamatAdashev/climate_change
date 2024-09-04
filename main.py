import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import time
from gtm import get_class
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0' 
import keras
import tensorflow as tf

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
    await ctx.send('definition, reasons, solutions, consequence, photo')

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
async def photo(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            if attachment.filename.endswitch('.jpg') or \
            attachment.filename.endswitch('.jpeg') or \
            attachment.filename.endswitch('.png'):
                image_path = f'./images/{attachment.filename}'    
                await attachment.save(image_path)
                msg = await ctx.send('Photo processing...')
                time.sleep(8)
                class_name, confidence_score = get_class(image_path, 
                                                         './gtm_model/keras_model.h5', 
                                                         './gtm_model/labels.txt', )
                await msg.delete()
                await ctx.send(f'With probability {confidence_score}% it is {class_name} for nature')

                os.remove(image_path)
            else:
                await ctx.send('You can only send jpg, jpeg, png') 
                return   
    else:
        await ctx.send('It seems you forgot to attach a photo')



@bot.command()
async def command_list_ru(ctx):
    await ctx.send('definition_ru, reasons_ru, solutions_ru, consequence_ru, photo_ru')

@bot.command()
async def definition_ru(ctx):
    await ctx.send("Глобальное потепление – это долгосрочное повышение общей температуры планеты. Хотя эта тенденция потепления продолжается уже давно, ее темпы значительно возросли за последние сто лет из-за сжигания ископаемого топлива. По мере увеличения численности населения увеличивался и объем сжигаемого ископаемого топлива.")    

@bot.command()
async def reasons_ru(ctx):
    await ctx.send('''Вот несколько причин, почему это происходит:
                   cжигание ископаемого топлива;
                   вырубка лесов;
                   выращивание домашнего скота.
                    Также фторированные газы вредны для нашей планеты. Они встречаются в кондиционерах, аэрозольных баллончиках, холодильниках.
                   ''')
    

@bot.command()
async def solutions_ru(ctx):
    await ctx.send('''Самые популярные меры против глобального потепления:
                   Экономьте энергию дома. Большая часть нашей электроэнергии и тепла вырабатывается за счет угля, нефти и газа;
                   Ходите пешком, ездите на велосипеде или пользуйтесь общественным транспортом;
                   Выбрасывайте меньше еды.''')
    

@bot.command()
async def consequence_ru(ctx):
    await ctx.send("Из-за глобального потепления люди болеют и могут умереть в будущем. Итак, это серьезная проблема.")



@bot.command()
async def photo_ru(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            if attachment.filename.endswitch('.jpg') or \
            attachment.filename.endswitch('.jpeg') or \
            attachment.filename.endswitch('.png'):
                image_path = f'./images/{attachment.filename}'    
                await attachment.save(image_path)
                time.sleep(8)
                msg = await ctx.send('Обработка фото...')
                class_name, confidence_score = get_class(image_path, 
                                                         './gtm_model/keras_model.h5', 
                                                         './gtm_model/labels.txt', )
                await msg.delete()
                await ctx.send(f'С вероятностью {confidence_score}% это {class_name} для природы')

                os.remove(image_path)
            else:
                await ctx.send('Вы можете отправить только jpg, jpeg, png') 
                return   
    else:
        await ctx.send('Кажется, вы забыли прикрепить фото')



bot.run(DISCORD_TOKEN)