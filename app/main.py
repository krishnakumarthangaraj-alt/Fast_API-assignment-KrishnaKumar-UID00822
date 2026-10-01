from fastapi import FastAPI
from app.database.connections import init_db, close_db


app = FastAPI()


@app.get("/")
async def health_check():
    return {"status": "ok"}