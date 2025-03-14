import Adafruit_DHT

class DHT22Sensor:
    """
        Classe permettant de gérer le capteur DHT22 pour mesurer la température et l'humidité.

        Attributes:
            pin (int): Broche GPIO du Raspberry Pi utilisée pour connecter le capteur.
            sensor (object): Instance du capteur DHT22 issue de la bibliothèque Adafruit_DHT.
        """
    def __init__(self, pin):
        """
            Initialise le capteur DHT22.

            Args:
                pin (int): Numéro de la broche GPIO à laquelle le capteur est connecté.
            """
        self.pin = pin
        self.sensor = Adafruit_DHT.DHT22

    def read(self):
        """
               Lit les données de température et d'humidité du capteur DHT22.

               Returns:
                   tuple: Un tuple contenant deux valeurs :
                       - humidity (float): Le pourcentage d'humidité mesuré.
                       - temperature (float): La température mesurée en degrés Celsius.

               Raises:
                   Exception: Si la lecture échoue, une exception est levée avec un message d'erreur.
               """
        # Lecture des données du capteur avec tentative automatique de réessai en cas d'échec
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humidity is not None and temperature is not None:
            return humidity, temperature
        raise Exception('Failed to get reading. Try again!')

