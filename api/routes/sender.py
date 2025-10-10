import logging

from sensorhandler import SensorHandler
sensorhandler = SensorHandler()
from fastapi import APIRouter

router = APIRouter()

@router.get("/collect_data")
async def collect_data():
    try:
        sensorhandler.send_data()
        return {"status": "success"}
    except Exception as e:
        logging.error(e)
        return {"status": "error", "message": str(e)}