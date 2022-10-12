from fastapi import FastAPI

from app.api.v1 import words

app = FastAPI()

app.include_router(words.router)


@app.get("/")
async def read_root():
    return {"message": "cyolo home assignment."}
