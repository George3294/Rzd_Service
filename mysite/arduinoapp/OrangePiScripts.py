import Adafruit_DHT
import time

# Установка порта, на котором датчик подключен
sensor_pin = 4


# Бесконечный цикл
while True:
    # Чтение данных с датчика
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, sensor_pin)

    # Проверка, были ли данные прочитаны успешно
    if humidity is not None and temperature is not None:
        print('Temperature: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')

    # Задержка в 2 секунды перед следующим чтением
    time.sleep(2)