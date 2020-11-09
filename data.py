import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def get_temperature_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
        pass

if __name__ == "__main__":
    while 1:
        a, b = get_temperature_humidity()
        print(a, b)
