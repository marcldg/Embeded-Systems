// This #include statement was automatically added by the Particle IDE.
#include <Adafruit_DHT_Particle.h>

// This #include statement was automatically added by the Particle IDE.
#include "Adafruit_DHT_Particle.h"

#define DHTPIN D2     // what pin we're connected to

#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

int led2 = D7;

void setup() 
{
	Serial.begin(9600); 
	Serial.println("DHTxx test!");
	Particle.publish("state", "DHTxx test start");

	dht.begin();
	delay(2000);
	
	// Here's the pin configuration, same as last time
    pinMode(led2, OUTPUT);
    
    // We are also going to declare a Particle.function so that we can turn the LED on and off from the cloud.
    Particle.function("led",ledToggle);
    
    // For good measure, let's also make sure both LEDs are off when we start:
    digitalWrite(led2, LOW);
}

void loop() 
{
// Read Humidity as a percentage
	float Humidity = dht.getHumidity();
// Read temperature as Celsius
	float Temperature = dht.getTempCelcius();
  
// Check if any reads failed and exit early (to try again).
	if (isnan(Humidity) || isnan(Temperature))
	{
		Serial.println("Failed to read from DHT sensor!");
		return;
	}

	Serial.print("Humid: "); 
	Serial.print(Humidity);
	Serial.print("% - ");
	Serial.print("Temp: "); 
	Serial.print(Temperature);
	Serial.print("*C ");
	Serial.println(Time.timeStr());
	
	Particle.publish("Temperature", String(Temperature), PRIVATE); // push data to our ThingSpeak Web IDE
	delay(5000);
}

int ledToggle(String command) 
{
    /* Particle.functions always take a string as an argument and return an integer.
    Since we can pass a string, it means that we can give the program commands on how the function should be used.
    In this case, telling the function "on" will turn the LED on and telling it "off" will turn the LED off.
    Then, the function returns a value to us to let us know what happened.
    In this case, it will return 1 for the LEDs turning on, 0 for the LEDs turning off,
    and -1 if we received a totally bogus command that didn't do anything to the LEDs.
    */

    if (command=="ons") 
    {
        digitalWrite(led2,HIGH);
        Particle.publish("Controller", String(1), PRIVATE);
        return 1;
    }
    else if (command=="onf") 
    {
        digitalWrite(led2,HIGH);
        Particle.publish("Controller", String(2), PRIVATE);
        return 1;
    }
    else if (command=="on") 
    {
        digitalWrite(led2,HIGH);
        Particle.publish("Controller", String(3), PRIVATE);
        return 1;
    }
    else if (command=="off") 
    {
        digitalWrite(led2,LOW);
        Particle.publish("Controller", String(0), PRIVATE);
        return 0;
    }
    else 
    {
        return -1;
    }
}