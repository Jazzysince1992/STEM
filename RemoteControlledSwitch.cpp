// C++ code
//
#include <IRremote.h>
int pinIR=7;
int bulb1=6;
int bulb2=5;
int bulb3=4;
int remoteValue;
void setup()
{
	pinMode(pinIR,INPUT);
  	IrReceiver.begin(pinIR);
  	Serial.begin(9600);
  	pinMode(bulb1,OUTPUT);
   	pinMode(bulb2,OUTPUT);
  	pinMode(bulb3,OUTPUT);
}

void loop()
{
  if (IrReceiver.decode()){
	remoteValue = IrReceiver.decodedIRData.command;
    Serial.println(remoteValue);
    IrReceiver.resume();
    if (remoteValue==0){
    digitalWrite(bulb1,LOW);
    digitalWrite(bulb2,LOW);
    digitalWrite(bulb3,LOW);
    }
    else if (remoteValue==16){
    digitalWrite(bulb1,!digitalRead(bulb1));
    }
    else if (remoteValue==17){
    digitalWrite(bulb2,!digitalRead(bulb2));
    }
    else if (remoteValue==18){
    digitalWrite(bulb3,!digitalRead(bulb3));
    }

  }
}