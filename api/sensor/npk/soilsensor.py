from api.sensor.basesensor import BaseSensor, extract_sensor_params


def init_soil_sensor_by_info(_server_info):
    _path, _interval = extract_sensor_params(_server_info)
    return SoilSensor(_path=_path, _interval=_interval)

class SoilSensor(BaseSensor):
    def __init__(self, _path='queue/NPK', _interval=600):
        super().__init__(_path=_path, _interval=_interval)
