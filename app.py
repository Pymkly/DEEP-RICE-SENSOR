# import logging
#
# from sensorhandler import SensorHandler
# logging.basicConfig(
#     filename='sensor.log',
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )
# sensorhandler = SensorHandler()
#
# sensorhandler.start()
import uvicorn
from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse
# from datetime import datetime
import os
from api.routes.incoming_manager import router as incoming_manager_router
# import json


app = FastAPI()
QUEUE_DIR = "queue"
os.makedirs(QUEUE_DIR, exist_ok=True)

app.include_router(incoming_manager_router, prefix="/incoming")

@app.get("/")
async def ping():
    return "ok"

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0",
                port=8000, reload=True)