
int photoresistor = A0;
// This is where your photoresistor or phototransistor is plugged in.
int analogvalue;
// Here we are declaring the integer variable analogvalue, which we will use later to store the value of the photoresistor or phototransistor.
void setup() 
{
    pinMode(photoresistor, INPUT);
    
     // We are going to declare a Particle.variable() here so that we can access the value of the photosensor from the cloud.
    Particle.variable("analogvalue", &analogvalue, INT);
    // This is saying that when we ask the cloud for "analogvalue", this will reference the variable analogvalue in this app, which is an integer variable.
}

void loop() 
{
     // check to see what the value of the photoresistor or phototransistor is and store it in the int variable analogvalue
    analogvalue = analogRead(photoresistor);
    
    // This prints the value to the USB debugging serial port (for optional debugging purposes)
    Serial.printlnf("%d", analogvalue);

    // This delay is just to prevent overflowing the serial buffer, plus we really don't need to read the sensor more than
    // 10 times per second (100 millisecond delay)
    delay(100);
    
}