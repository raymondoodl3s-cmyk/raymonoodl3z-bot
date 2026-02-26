import random
import time
from database import get_user, update_points

async def daily(ctx):
    user = ctx.author.name
    reward = random.randint(50, 200)
    await update_points(user, reward)
    await ctx.send(f"{user} claimed daily reward of {reward} coins 💰")

async def gamble(ctx, amount: int):
    user = ctx.author.name
    if random.random() < 0.5:
        await update_points(user, amount)
        await ctx.send(f"🎉 {user} won {amount} coins!")
    else:
        await update_points(user, -amount)
        await ctx.send(f"💀 {user} lost {amount} coins!")

async def steal(ctx, amount: int, target: str):
    user = ctx.author.name
    outcome = random.random()

    if outcome < 0.45:
        await update_points(user, amount)
        await update_points(target, -amount)
        await ctx.send(f"😈 {user} stole {amount} from {target}")
    elif outcome < 0.85:
        await update_points(user, -amount)
        await ctx.send(f"🚨 {user} failed and lost {amount}")
    else:
        await update_points(user, -amount*2)
        await ctx.send(f"⛓ {user} went to jail and paid double!")
