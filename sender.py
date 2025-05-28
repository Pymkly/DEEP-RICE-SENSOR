import logging

from sensorhandler import SensorHandler
logging.basicConfig(
    filename='sensor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
sensorhandler = SensorHandler()

sensorhandler.start()