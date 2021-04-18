from discord.ext import commands
import os
import traceback
import diceSearchAndCalc as dice
from discord.ext.commands.errors import MissingRequiredArgument
from discord.ext.commands.errors import CommandNotFound
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
percent = 0.3
memberList = []
emotionTable = ["共感/不信", "友情/怒り", "愛情/妬み", "忠誠/侮蔑", "憧憬/劣等感", "狂信/殺意"]
botSentences = ["コマンド間違えてるニャ！　気を付けるニャ！",
                "コマンドが違うニャ！",
                "また間違えてるのニャ！",
                "それは違うニャ！",
                "ニャー！　間違ってるのニャ！",
                "ほら、間違えてるのニャ"]


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    #print(type(error))
    #print(error_msg)
    if type(error) == CommandNotFound:
        await ctx.send(f"{ctx.author.mention} そのコマンドは無いのニャ！")
    elif type(error) == MissingRequiredArgument:
        await ctx.send(f"{ctx.author.mention} コマンドが足りないニャ！")
    else:
        messageDice = random.randint(0,len(botSentences)-1)
        await ctx.send(f"{ctx.author.mention} {botSentences[messageDice]}")
         

@bot.command()
async def r(ctx, arg):
    if ctx.author.bot:
        return

    result = dice.replaceAndCalc(arg, ctx.author.id)
    reply = f"{ctx.author.mention} {result}"
    await ctx.send(reply)
    
@bot.command()
async def neko(ctx):
    await ctx.send("ニャーア♪")
    

    
@bot.command()
async def kitaiti(ctx):
    if ctx.author.id == 632853740159762435:
        await ctx.send("AAAAAAA")
    await ctx.send(f"{ctx.author.mention}**2D6** => 4(2+2) => **4**")
    
@bot.command()
async def ote(ctx):
    if random.random() >= percent:
        await ctx.send(f"{ctx.author.mention}ニャ（ぽふ）")
    else:
        await ctx.send(f"{ctx.author.mention}ニャ（ぷい）")
    
@bot.command()
async def okawari(ctx):
    if random.random() >= percent:
        await ctx.send(f"{ctx.author.mention}ニャ（ぺふ）")
    else:
        await ctx.send(f"{ctx.author.mention}ニャ（ぷい）")

@bot.command()
async def et(ctx):
    id = ctx.author.id
    if id == 495201006209073152:#モノアイ
        await ctx.send(f"{ctx.author.mention} **3** => 愛情/愛情")
    elif id == 452400598692659202:#正方形
        await ctx.send(f"{ctx.author.mention} **0** => 気まぐれ/おもちゃ")
    elif id == 543824507178057742:#サイア
        await ctx.send(f"{ctx.author.mention} **7** => 君には星見は/微笑まない")
    else:
        dice = random.randint(1,6)
        await ctx.send(f"{ctx.author.mention} **{dice}** => `{emotionTable[dice-1]}`")

@bot.command()
async def リガルは美少女(ctx):
    await ctx.send(f"{ctx.author.mention} それは違うのニャ！")

bot.run(token)
