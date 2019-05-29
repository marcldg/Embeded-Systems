import Adafruit_DHT
import requests
import json
import RPi.GPIO as GPIO
import time
import re

while True:
    req = None
    JsonResult = None

    GPIO.setmode(GPIO.BCM)
    gpio = 17
    pins = [22, 27]
    SleepTime = 1.5

    for i in pins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)
    
    reqcontrol = requests.get("https://api.thingspeak.com/channels/783985/feeds.json?api_key=1P8XMLCFU7TM89I9")
    #print(req.text)

    JsonResult = json.loads((reqcontrol.text))
    #print(JsonResult['feeds'])

    feeds = JsonResult['feeds']

    switch = feeds[-1]
    switchvalue = float(switch['field1'])
    print(switchvalue)

    if(switchvalue == 0):
        print('Artificial Lighting OFF !')

    elif(switchvalue == 3):
        print('Artificial Lighting ON !')
        GPIO.output(22, GPIO.LOW)
        print('TOP PANEL ON')
        GPIO.output(27, GPIO.LOW)
        print('BOTTOM PANEL ON')
    
    elif(switchvalue == 1 or switchvalue == 2):

        if(switchvalue == 1):
            print('Using Sensors For System Automation')

        # Set sensor type : DHT11
        sensor=Adafruit_DHT.DHT11

        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

        req = requests.get("https://api.thingspeak.com/channels/749312/feeds.json?api_key=WC2CING2DB1OQNAN")
        #print(req.text)

        JsonResult = json.loads((req.text))
        #print(JsonResult['feeds'])

        feeds = JsonResult['feeds']

        lastindex = feeds[-1]
        ExternalTemperature = float(lastindex['field1'])

        if(switchvalue == 2):
            print(' Using Forecasted Temperature For System Automation')
            
            reqhtml = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=BSKMINZ5DZPNVKEZ")
            #print(req.text)

            forecast = re.findall(r'<nobr>(.*?)°C</nobr>', str(reqhtml.text))

            ftemp = forecast[-1]
            forecastTemperature = float(ftemp)

            ExternalTemperature = forecastTemperature
        
        if(temperature > ExternalTemperature):
            GPIO.output(22, GPIO.LOW)
            print('TOP PANEL ON')
            GPIO.output(27, GPIO.LOW)
            print('BOTTOM PANEL ON')
            print('INTERNAL : Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            print('EXTERNAL :')
            print(ExternalTemperature)
            time.sleep(SleepTime)
            GPIO.cleanup()
        else:
            GPIO.output(22, GPIO.HIGH)
            print('TOP PANEL OFF')
            GPIO.output(27, GPIO.HIGH)
            print('BOTTOM PANEL OFF')
            print('INTERNAL : Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            print('EXTERNAL :')
            print(ExternalTemperature)
            GPIO.cleanup()

            #print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            #print(lastindex['field1'])
        
        
