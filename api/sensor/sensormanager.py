from api.sensor.npk.soilsensor import SoilSensor, init_soil_sensor_by_info
from api.sensor.water_level.water_level_sensor import WaterLevelSensor, init_water_level
from api.sensor.wind.DHT22 import DHT22Sensor, init_dht22_by_info
import time
import logging
import json
import requests

from api.utils.config import get_ping_url

SENSOR_CLASSES = {
    "DHT22": [DHT22Sensor, init_dht22_by_info],
    "NPK": [SoilSensor, init_soil_sensor_by_info],
    "WATER_LEVEL": [WaterLevelSensor, init_water_level],
}


def ping():
    try:
        print("start ping")
        logging.info("start ping")
        response = requests.get(get_ping_url())
        print("end ping")
        logging.info("end ping")
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(e)
        logging.error(f"Erreur de connexion au serveur : {e}")
        return False


class SensorManager:
    def __init__(self, _data_sender):
        self.sensors = []
        self._data_sender = _data_sender
        self.next_send_time = {}

    def load_sensors(self, config_path='sensors_config.json'):
        """
        Charge les capteurs depuis un fichier JSON
        """
        try :
            with open(config_path, 'r') as file:
                sensor_config = json.load(file)
            for sensor_info in sensor_config:
                sensor_type = sensor_info['type']
                interval = int(sensor_info['interval'])
                if sensor_type in SENSOR_CLASSES:
                    sensor_instance = SENSOR_CLASSES[sensor_type][1](sensor_info)

                    self.add_sensor(sensor_instance, interval)
        except Exception as e:
            logging.error(f"Erreur lors du chargement du fichier JSON : {e}")


    def add_sensor(self, sensor, _interval):
        """
        Ajoute un capteur à la liste.
        """
        self.sensors.append((sensor, _interval))
        self.next_send_time[sensor] = time.time()

    def collect_data(self):
        # while True:
        #     check = ping()
        # if check :
        current_time = time.time()
        logging.info("Collecting data...")
        for sensor, interval in self.sensors:
            if current_time > self.next_send_time[sensor]:
                self._data_sender.send_data(sensor)
                logging.info(f"Sent data for {sensor}")
                self.next_send_time[sensor] = current_time + interval
        logging.info("Data collected.")
            # break




