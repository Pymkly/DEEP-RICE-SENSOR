from api.sensor.sensormanager import SensorManager
from api.serveraccess.dataSender import DataSender
import time

from api.utils.config import get_global_config, get_server_url


class SensorHandler:
    def __init__(self):
        self.interval = 0
        self.init_interval()
        self.data_sender = DataSender(get_server_url())
        self.sensor_manager = SensorManager(self.data_sender)
        self.sensor_manager.load_sensors()

    def init_interval(self):
        global_config = get_global_config()
        self.interval = int(global_config["sensor_collect_interval"])

    def send_data(self):
        self.sensor_manager.collect_data()

    def start(self):
        while True:
            self.send_data()
            time.sleep(self.interval)
