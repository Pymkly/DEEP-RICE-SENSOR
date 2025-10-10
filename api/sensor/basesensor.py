import logging
from datetime import datetime, timedelta
import json
import os

def extract_sensor_params(_server_info):
    _type = _server_info['type']
    _interval = _server_info['interval']
    _path = os.path.join("queue", _type)
    return _path, _interval

class BaseSensor:
    def __init__(self, _path, _interval):
        self._path = _path
        self._interval = _interval

    def prepare_data(self):
        """
        Prépare les données en format dictionnaire.
        Utilise la méthode `read()` propre à chaque capteur.
        """
        return self.read()
        # data = self.read()
        # return {
        #     "type": self.__class__.__name__,  # Identifie le type de capteur
        #     "data": data,
        # }

    def read(self):
        files = sorted(os.listdir(self._path))
        logging.info(files)
        _responses = []
        _file_grp = []
        for file in files:
            _filepath = os.path.join(self._path, file)
            if os.path.isdir(_filepath):
                logging.info(_filepath)
                _resp_temp, _file_grp_temp = self.read_one_poto(_filepath)
                _responses.extend(_resp_temp)
                _file_grp.extend(_file_grp_temp)
        logging.info(_responses)
        logging.info(_file_grp)
        return _responses, _file_grp

    def read_one_poto(self, _path):
        files = sorted(os.listdir(_path))
        _responses = []
        next_time = None
        _file_grp = []
        _index = -1
        for file in files:
            if file.endswith(".json"):
                filepath = os.path.join(_path, file)
                # print(filepath)
                try:
                    with open(filepath, "r") as f:
                        data = json.load(f)
                        timestamp = datetime.fromisoformat(data.get("timestamp"))
                        if next_time is None or timestamp >= next_time:
                            _index += 1
                            _file_grp.append([filepath])
                            _responses.append(data)
                            next_time = timestamp + timedelta(seconds=self._interval)
                        else:
                            _file_grp[_index].append(filepath)
                except Exception as e:
                    raise Exception('Failed to get reading. Try again!')
        return _responses, _file_grp