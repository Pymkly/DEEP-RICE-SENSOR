from sensor.wind.DHT22 import DHT22Sensor

print("hello world")

dht22 = DHT22Sensor(4)

print(f"DHT22 pi : {dht22.pin}")
try:
    humidity, temperature = dht22.read()
    print(f'Température = {temperature:.1f}°C')
    print(f'Humidité = {humidity:.1f}%')
except Exception as e:
    print(f"Exception : {e}")