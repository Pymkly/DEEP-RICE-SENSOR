import json
import logging
import os

import requests

from api.utils.config import get_sensor_data_url, get_ref


class DataSender:
    def __init__(self, _server_url):
        self._server_url = _server_url + get_sensor_data_url()

    def send_data(self, _sensor):
        """
            Envoie les données au serveur via HTTP POST.
        """
        try:
            datas, _file_grp = _sensor.prepare_data()
            for i in range(len(datas)):
                data = datas[i]
                # data["ref"] = get_ref()
                print(data)
                response = requests.post(
                    self._server_url,
                    data=json.dumps(data),
                    headers={'Content-Type': 'application/json'}
                )
                if response.status_code == 200:
                    logging.info("Données envoyées avec succès.")
                    for _file in _file_grp[i]:
                        os.remove(_file)
                else:
                    logging.error(f"Échec de l'envoi des données. Code HTTP : {response.status_code}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Erreur de connexion au serveur : {e}")