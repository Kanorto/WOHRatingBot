from fastapi import FastAPI

app = FastAPI(title="WOH Rating Web App")


@app.get("/")
async def root():
    return {"message": "WOH Rating Web App"}
