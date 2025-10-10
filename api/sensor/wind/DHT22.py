from api.sensor.basesensor import BaseSensor, extract_sensor_params


def init_dht22_by_info(_server_info):
    _path, _interval = extract_sensor_params(_server_info)
    return DHT22Sensor(_path=_path, _interval=_interval)

class DHT22Sensor(BaseSensor):

    def __init__(self, _path='queue/DHT22', _interval=600):
        super().__init__(_path=_path, _interval=_interval)
