from api.sensor.basesensor import BaseSensor, extract_sensor_params


def init_water_level(_server_info):
    _path, _interval = extract_sensor_params(_server_info)
    return WaterLevelSensor(_path=_path, _interval= _interval)

class WaterLevelSensor(BaseSensor):
    def __init__(self, _path='queue/LEVEL', _interval=600):
        super().__init__(_path=_path, _interval=_interval)