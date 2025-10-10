import logging
import os
import json
from datetime import datetime

class IncomingManager:
    def __init__(self, queue_dir="queue"):
        self.queue_dir = queue_dir
        os.makedirs(self.queue_dir, exist_ok=True)

        # Définitions des capteurs et leurs clés
        self.sensor_fields = {
            "DHT22": {"humidity", "temperature"},
            "NPK": {"N", "P", "K"},
            "WATER_LEVEL": {"level"},
        }

    def parse_and_save(self, ref: str, raw_data: dict):
        """
        Analyse les données entrantes, les sépare par type de capteur,
        puis les enregistre dans des fichiers distincts.
        """
        matched_data = self.prepare_data(raw_data)
        # Enregistre chaque bloc de données dans la file
        for sensor_type, data in matched_data.items():
            _path = os.path.join(self.queue_dir, sensor_type, ref)
            os.makedirs(_path, exist_ok=True)
            payload = {
                "type": sensor_type,
                "ref": ref,
                "data": data,
                "timestamp": datetime.utcnow().isoformat()
            }
            filename = f"{sensor_type}_{ref}_{datetime.utcnow().timestamp()}.json"
            filepath = os.path.join(_path, filename)
            try:
                with open(filepath, "w") as f:
                    json.dump(payload, f)
                # logging.info(f"Données enregistrées pour {sensor_type} dans {filepath}")
            except Exception as e:
                logging.error(f"Erreur en sauvegardant {sensor_type}: {e}")

    def  prepare_data(self, raw_data):
        matched_data = {}

        # On sépare les données en fonction des capteurs connus
        for sensor_type, expected_keys in self.sensor_fields.items():
            sensor_data = {k: self._to_float(raw_data[k]) for k in expected_keys if k in raw_data}
            if sensor_data:
                matched_data[sensor_type] = sensor_data
        return matched_data

    def _to_float(self, value):
        try:
            return float(value)
        except:
            return value
