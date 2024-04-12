#include <Sleep_n0m1.h>
#include <EEPROM.h>
Sleep sleep;
unsigned long sleepTime; 
void setup() {
   Serial.begin(9600);
   Serial.print("Стол v1.2");
   sleepTime = 60000;
   pinMode(7, INPUT);
   pinMode(6, INPUT);
}

void loop() {
if(digitalRead(7) == LOW) {
  Serial.println("Alert");
  EEPROM.write(10, 1);
  delay(1000);
  EEPROM.write(10, 0);
}
if(digitalRead(6) == HIGH) {   
  sleep.pwrDownMode(); 
  sleep.sleepDelay(sleepTime); 
}
 
  
}