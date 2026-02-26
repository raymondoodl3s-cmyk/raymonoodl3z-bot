import aiosqlite

DB_NAME = "bot.db"

async def setup():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            points INTEGER DEFAULT 100,
            jailed INTEGER DEFAULT 0,
            jail_until INTEGER DEFAULT 0
        )
        """)
        await db.commit()

async def get_user(username):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT * FROM users WHERE username=?", (username,))
        row = await cursor.fetchone()
        if row:
            return row
        await db.execute("INSERT INTO users (username) VALUES (?)", (username,))
        await db.commit()
        return (username, 100, 0, 0)

async def update_points(username, amount):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        INSERT INTO users(username, points)
        VALUES (?, ?)
        ON CONFLICT(username)
        DO UPDATE SET points = points + ?
        """, (username, amount, amount))
        await db.commit()
