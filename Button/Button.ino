/*
  Button
 
 Turns on and off a light emitting diode(LED) connected to digital  
 pin 13, when pressing a pushbutton attached to pin 2. 
 
 
 The circuit:
 * LED attached from pin 13 to ground 
 * pushbutton attached to pin 2 from +5V
 * 10K resistor attached to pin 2 from ground
 
 * Note: on most Arduinos there is already an LED on the board
 attached to pin 13.
 
 
 created 2005
 by DojoDave <http://www.0j0.org>
 modified 30 Aug 2011
 by Tom Igoe
 
 This example code is in the public domain.
 
 http://www.arduino.cc/en/Tutorial/Button
 */

// constants won't change. They're used here to 
// set pin numbers:
const int buttonPinDot = 2;     // the number of the pushbutton pin
const int buttonPinDash = 3;     // the number of the pushbutton pin
const int ledPinDot =  12;      // the number of the LED pin
const int ledPinDash =  11;      // the number of the LED pin
const int dotTime = 100;

#define buttonPressed HIGH
#define buttonOpen LOW

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPinDot, OUTPUT);
  pinMode(ledPinDash, OUTPUT);   
  // initialize the pushbutton pin as an input:
  pinMode(buttonPinDot, INPUT);   
  pinMode(buttonPinDash, INPUT); 
  Serial.begin(9600); 
}

void loop(){
  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  
  int pressedTime = 0;
  int startTime = 0;
  int pinBool = digitalRead(buttonPinDot);
  
  if (pinBool == LOW){
    delay(100);
    digitalWrite(ledPinDot, LOW);
    startTime = millis();
    while (pinBool == LOW) {
      if (digitalRead(buttonPinDot) == HIGH){
        pinBool = HIGH;
      }
    } 
  }
    
  pressedTime = millis() - startTime;
  if (pressedTime > dotTime){
    int bytesSent = Serial.write(".");
    Serial.print(pressedTime);
    startTime = 0;
  }
  delay(dotTime);
  
  
  if (digitalRead(buttonPinDash) == LOW) {     
    // turn LED on:    
    digitalWrite(ledPinDash, LOW); 
    int bytesSent = Serial.write("\n");
    delay(dotTime);
  }
  else {
    digitalWrite(ledPinDot, HIGH); 
    digitalWrite(ledPinDash, HIGH);
  }
}

