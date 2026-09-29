import asyncio
from tortoise import Tortoise
from app.database.connections import TORTOISE_ORM

async def check_database():
    await Tortoise.init(config = TORTOISE_ORM)
    connection = Tortoise.get_connection("default")
    await connection.execute_query("SELECT 1")
    print("Connected")
    await Tortoise.close_connections()
asyncio.run(check_database())

