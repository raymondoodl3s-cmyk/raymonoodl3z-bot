import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def ai_reply(ctx, message):
    if os.getenv("AI_ENABLED") != "true":
        return

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": message}]
    )

    reply = response.choices[0].message.content[:400]
    await ctx.send(reply)
