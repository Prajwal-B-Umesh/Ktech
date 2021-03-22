import Adafruit_DHT
while True:
    humidity, temperature = Adafruit_DHT.read_retry(11,21)# GPIO21 and DHT 11
    print("Humidity = {} %; Temperature = {} C".format(humidity,temperature))

#Trials
