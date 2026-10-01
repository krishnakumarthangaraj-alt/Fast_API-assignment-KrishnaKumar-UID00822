import os
from tortoise import Tortoise
from dotenv import load_dotenv
from app.configurations.database_config import HOST,DATABASE_USER,PORT, DATABASE


load_dotenv()

DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

TORTOISE_ORM = {
    "connections": {
        "default":{
            "engine" : "tortoise.backends.asyncpg",
            "credentials": {
                "host" : HOST,
                "port" : PORT,
                "user" : DATABASE_USER,
                "password" : DATABASE_PASSWORD,
                "database" : DATABASE,
            }
        }
    },
    "apps":{
        "models":{
            "models": ["app.models"],
            "default_connections": "default",
        }
    },
}


async def init_db():
    await Tortoise.init(config = TORTOISE_ORM)
async def close_db():
    await Tortoise.close_connections()