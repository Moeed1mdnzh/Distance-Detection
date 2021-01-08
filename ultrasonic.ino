int PingPin = 13;
int EchoPin = 11;

void setup(){
  
 pinMode(PingPin, OUTPUT);
 pinMode(EchoPin, INPUT);
 
 Serial.begin(9600);
}

void loop(){
  unsigned long duration, cm;
  
  digitalWrite(PingPin,LOW);
  delayMicroseconds(2);
  digitalWrite(PingPin,HIGH);
  delayMicroseconds(5);
  digitalWrite(PingPin, LOW);
  
  
  duration = pulseIn(EchoPin, HIGH);
  
  cm = (duration/29/2);
  
  Serial.println(cm);
  delay(100);
  
}
