from fastapi import FastAPI
import asyncio  
app = FastAPI()

@app.get("/wait")
async def wait():
    await asyncio.sleep(5)  
    return {"message": "Waited for 5 seconds!"}

