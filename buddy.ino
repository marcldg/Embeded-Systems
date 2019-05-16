int led1 = D2;
int led2 = D3;

void setup() 
{
pinMode(led1,OUTPUT);
pinMode(led2,OUTPUT);

Particle.subscribe("Deakin_RIOT_SIT210_Photon_Buddy", myHandler);
}

void loop() 
{

}

void myHandler(const char *event, const char *data)
{
    if (strcmp(data,"wave")==0) {
        digitalWrite(led1,HIGH);
        delay(1000);
        digitalWrite(led1,LOW);
        delay(1000);
        digitalWrite(led1,HIGH);
        delay(1000);
        digitalWrite(led1,LOW);
        delay(1000);
        digitalWrite(led1,HIGH);
        delay(1000);
    }
    if (strcmp(data,"pat")==0)
    {
        digitalWrite(led2,HIGH);
        delay(2000);
        digitalWrite(led2,LOW);
        delay(2000);
        digitalWrite(led2,HIGH);
        delay(2000);
    }
}