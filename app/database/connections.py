from tortoise import Tortoise
TORTOISE_ORM = {
    "connections": {
        "default":{
            "engine" : "tortoise.backends.asyncpg",
            "credentials": {
                "host" : "localhost",
                "port" : 5432,
                "user" : "restaurant_usr",
                "password" : "restaurant123",
                "database" : "restaurant_db",
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
    