from fastapi import FastAPI
from app.database.connections import init_db, close_db


app = FastAPI()

@app.on_event("startup")
async def startup():
    print("Started")
    await init_db()

@app.on_event("shutdown")
async def shutdown():
    await close_db()

@app.get("/health")
async def health_check():
    return {"status": "ok"}