import requests
import os

queue = []

def search_youtube(query):
    key = os.getenv("YOUTUBE_API_KEY")
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q={query}&key={key}"
    r = requests.get(url).json()
    video_id = r["items"][0]["id"]["videoId"]
    return f"https://youtube.com/watch?v={video_id}"

async def add_song(ctx, *, query):
    link = search_youtube(query)
    queue.append(link)
    await ctx.send(f"🎵 Added: {link}")

async def show_queue(ctx):
    if not queue:
        await ctx.send("Queue empty.")
        return
    await ctx.send(f"Next song: {queue[0]}")
