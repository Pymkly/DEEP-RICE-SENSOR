import json
import os

import serial

from api.sensor.basesensor import BaseSensor


def init_soil_sensor_by_info(_server_info):
    _port = _server_info['port']
    _baude_rate = int(_server_info['bauderate'])
    _type = _server_info['type']
    interval = _server_info['interval']
    _path = os.path.join("queue", _type)
    return SoilSensor(port=_port, _baude_rate=_baude_rate, _path=_path, _interval=interval)

class SoilSensor(BaseSensor):
    def __init__(self, port='/dev/serial0', _baude_rate=9600, _path='queue/NPK', _interval=600):
        super().__init__(_path=_path, _interval=_interval)
        self.ser = serial.Serial(
            port=port,
            baudrate=_baude_rate,
            # parity=serial.PARITY_NONE,
            # stopbits=serial.STOPBITS_ONE,
            # bytesize=serial.EIGHTBITS,
            timeout=2
        )

    # def read(self):
    #     self.ser.write(b'GET\n')
    #     response = self.ser.readline().decode().strip()
    #     try:
    #         data = json.loads(response)
    #         return data
    #     except json.JSONDecodeError:
    #         print("Erreur : réponse non valide.")
    #         return None