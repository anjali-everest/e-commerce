from fastapi import FastAPI
from routes.item_router import item_router

app = FastAPI()

app.include_router(item_router)


@app.get("/hello")
async def root():
    return {"message": "Hello World"}
