// This #include statement was automatically added by the Particle IDE.
#include <Adafruit_DHT_Particle.h>

// This #include statement was automatically added by the Particle IDE.
#include "Adafruit_DHT_Particle.h"

#define DHTPIN D2     // what pin we're connected to

#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() 
{
	Serial.begin(9600); 
	Serial.println("DHTxx test!");
	Particle.publish("state", "DHTxx test start");

	dht.begin();
	delay(2000);
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
	delay(10000);
}