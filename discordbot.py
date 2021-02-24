from discord.ext import commands
import os
import traceback
import diceSearchAndCalc as dice

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await checkMissCount(ctx)

async def checkMissCount(ctx):
    #print(memberList)
    await removeList()
    idNumber = ctx.author.id
    ontime = time.time()
    if not memberList:
        memberList.append([idNumber, 0, ontime])
        await ctx.send(f"{ctx.author.mention}{botSentences[memberList[0][1]]}")
    else:
        for item in memberList:
            if idNumber == item[0]:
                if ontime - item[2] <= limitTime:
                    item[2] = ontime
                    item[1] += 1
                    if item[1] >= len(botSentences):
                        item[1] = 0
                else:
                    item[2] = ontime
                    item[1] = 0
                
                await ctx.send(f"{ctx.author.mention}{botSentences[item[1]]}")
                return
            
        memberList.append([idNumber, 0, ontime])
        await ctx.send(f"{ctx.author.mention}{botSentences[item[1]]}")
        
async def removeList():
    removeNum = []
    for i in range(len(memberList)):
        if time.time() - memberList[i][2] >= limitTime:
            removeNum.append(i)
            
    for i in removeNum:
        memberList.pop(i)                

@bot.command()
async def r(ctx, arg):
    if ctx.author.bot:
        return

    result = dice.replaceAndCalc(arg)
    reply = f"{ctx.author.mention}{result}"
    await ctx.send(reply)
    
@bot.command()
async def neko(ctx):
    await ctx.send("ニャー")
    
@bot.command()
async def Rigal(ctx):
    rigal = "<@632853740159762435>"
    await ctx.send(f"{rigal}は美少女")
    
@bot.command()
async def kitaiti(ctx):
    await ctx.send(f"{ctx.author.mention}**2D6** => 4(2+2) => **4**")


bot.run(token)
