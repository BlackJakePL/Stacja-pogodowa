#include <Wire.h>
#include <Adafruit_BMP085.h>
#include "DHT.h"

#define DHTPIN 2     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
Adafruit_BMP085 bmp;
int maxHum = 60;
int maxTemp = 40;


DHT dht(DHTPIN, DHTTYPE);
void setup()
{
  Serial.begin(9600);
   dht.begin();
  
  // Jako parametr mozemy podav dokladnosc - domyslnie 3
  // 0 - niski pobór energii - najszybszy pomiar
  // 1 - standardowy pomiar
  // 2 - wysoka precyzja
  // 3 - super wysoka precyzja - najwolniejszy pomiar
  if (!bmp.begin(3))
  {
    Serial.println("Nie odnaleziono czujnika BMP085 / BMP180");
    while (1) {}
  }
}
 
void loop()
{
  // odczyt temperatury lub wilgotnosci zajmuje ok 250ms
  //odczyt wilgotnosci
  float humidity = dht.readHumidity();
  // Odczyt temperatury w stopniach celciusza
  float temp1 = dht.readTemperature();
  String mess ="";
  float presure = bmp.readPressure();
  float temp2 =bmp.readTemperature();
  float height =bmp.readAltitude();
  float realHeight = bmp.readAltitude(101920);
  float temp = (temp1 + temp2)/2;
  
  // Sprawdzanie poprawnosci odczytanych danych
  if (isnan(humidity) || isnan(temp1)) 
  {
    Serial.println("blad odczytu danych");
    return;
  }
    mess = String(temp)+"/"+String(humidity)+"/"+String(presure)+"/"+String(height)+"/"+String(realHeight)+"/";
    Serial.print(mess);
    delay(1000);
}
