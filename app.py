import uvicorn
from fastapi import FastAPI, Request
import os
from api.routes.incoming_manager import router as incoming_manager_router
from api.routes.sender import router as sender_router
import logging

logging.basicConfig(
    filename='sensor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
app = FastAPI()
QUEUE_DIR = "queue"
os.makedirs(QUEUE_DIR, exist_ok=True)

app.include_router(incoming_manager_router, prefix="/incoming")
app.include_router(sender_router, prefix="/api")

@app.get("/")
async def ping():
    return "ok"

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0",
                port=8000, reload=True)