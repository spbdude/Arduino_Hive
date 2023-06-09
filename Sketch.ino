#include "DHT.h" //Подключаем библиотеку.
#include <Servo.h>
#include "HX711.h"  

#define DHTPIN 2 // what digital pin we're connected to(Вывод к которому подключен датчик, в данном случае  пин D2)

#define DHTTYPE DHT21 // DHT 21 (AM2301) //Здесь выбираем какой у нас датчик.

Servo myservo;
HX711 scale;  
DHT dht(DHTPIN, DHTTYPE); 

float calibration_factor = 0.71;                             // вводим калибровочный коэффициент
float units;                                                  // задаём переменную для измерений в граммах
float ounces;                                                 // задаём переменную для измерений в унциях

void setup() {
 Serial.begin(9600); 
 myservo.attach(4);
dht.begin();                      
}

void loop() {


// Reading temperature or humidity takes about 250 milliseconds!
 // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
 float h = dht.readHumidity(); //читаем влажность
 // Read temperature as Celsius (the default)
 float t = dht.readTemperature(); // читаем температуру 
 // Read temperature as Fahrenheit (isFahrenheit = true)
 float f = dht.readTemperature(true); 

// Check if any reads failed and exit early (to try again).
 if (isnan(h) || isnan(t) || isnan(f)) {
 Serial.println("Failed to read from DHT sensor!"); //Проверка подключен ли датчик
 return;
 }
 if (h < 50.0){
   myservo.write(90);
 }
 if (h > 50.0){
   myservo.write(0);
 }
 float g = 45000;
 g = g + random(-50, 50);

 Serial.println(h);
 Serial.println(t);
 Serial.println(g);
 delay(10000);
}
