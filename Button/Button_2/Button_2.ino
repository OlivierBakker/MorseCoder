#define ditLed 11
#define newLed 12

const int debounceTime = 10;
boolean switchState = true;
boolean oldState = switchState;
long startTime = 0;
void setup(){
  
 pinMode(2, INPUT);
 pinMode(3, INPUT);
 pinMode(ditLed, OUTPUT);
 pinMode(newLed, OUTPUT);
 digitalWrite(ditLed,HIGH);
 digitalWrite(newLed,HIGH);
 Serial.begin(115200);
}



void loop()
{  
  switchState = digitalRead(2);
  
  if(switchState!=oldState)
  {
    oldState=switchState;
    
    delay(debounceTime);    
 
    Serial.print("State: ");
    Serial.print(switchState);
    Serial.print(" Time: ");
    Serial.println(millis() - startTime);
    startTime = millis();
  }
      
     
}
  
