import json
import os
from http.client import responses

import Adafruit_DHT

from api.sensor.basesensor import BaseSensor

def init_dht22_by_info(_server_info):
    pin = _server_info['pin']
    pin = int(pin)
    type = _server_info['type']
    interval = _server_info['interval']
    _path = os.path.join("queue", type)
    return DHT22Sensor(pin=pin, _path=_path, _interval=interval)

class DHT22Sensor(BaseSensor):
    """
        Classe permettant de gérer le capteur DHT22 pour mesurer la température et l'humidité.

        Attributes:
            pin (int): Broche GPIO du Raspberry Pi utilisée pour connecter le capteur.
            sensor (object): Instance du capteur DHT22 issue de la bibliothèque Adafruit_DHT.
        """
    def __init__(self, pin, _path='queue/DHT22', _interval=600):
        super().__init__(_path=_path, _interval=_interval)
        print(self._path)
        """
            Initialise le capteur DHT22.

            Args:
                pin (int): Numéro de la broche GPIO à laquelle le capteur est connecté.
            """
        # self.pin = pin
        # self.sensor = Adafruit_DHT.DHT22

    #
    # def read(self):
    #     pass
    #     # Lecture des données du capteur avec tentative automatique de réessai en cas d'échec
    #     # humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
    #     # if humidity is not None and temperature is not None:
    #     #     return {"humidity": humidity, "temperature": temperature}


