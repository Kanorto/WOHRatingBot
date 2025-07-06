from fastapi import FastAPI

from config import DEBUG

app = FastAPI(title="WOH Rating Web App", debug=DEBUG)


@app.get("/")
async def root():
    return {"message": "WOH Rating Web App"}
