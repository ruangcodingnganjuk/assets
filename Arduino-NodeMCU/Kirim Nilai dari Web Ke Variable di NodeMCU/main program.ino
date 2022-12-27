#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "your_ssid";
const char* password = "your_password";

const char* host = "worldtimeapi.org";

void setup() {
  Serial.begin(115200);
  delay(10);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  HTTPClient http;
  http.begin("http://" + String(host) + "/api/timezone/Asia/Jakarta"); // Specify the URL
  int httpCode = http.GET(); // Make the request

  if (httpCode > 0) { // Check for the returning code
    String payload = http.getString(); // Get the request response payload
    Serial.println(httpCode);
    Serial.println(payload);
  } else {
    Serial.println("Error on HTTP request");
  }

  http.end(); // Free the resources
  delay(5000);
}