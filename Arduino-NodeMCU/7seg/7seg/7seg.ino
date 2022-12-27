unsigned long count;

int jeda = 1;
int detik;
int menit = 59;
int jam = 12;
int code[] = {B00111111, B00000110, B01011011, B01001111, B01100110, B01101101, B01111101, B00000111, B01111111, B01101111};
void setup() {
  // put your setup code here, to run once:
  DDRA = B11111111;
  DDRC = B11111111;
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  //detik++;

  if (detik > 59) {
    detik = 0;
    menit++;
  }
  if (menit > 59) {
    menit = 0;
    jam++;
  }
  if (jam > 23) {
    jam = 0;
  }

  PORTA = code[jam / 10];
  hitung2(37);
  PORTA = code[jam % 10];
  hitung2(36);
  PORTA = code[menit / 10];
  hitung2(35);
  PORTA = code[menit % 10];
  hitung2(34);
  PORTA = code[detik / 10];
  hitung2(33);
  PORTA = code[detik % 10];
  hitung2(32);


}

void hitung2(int pin) {
  digitalWrite(pin, 1);
  delay(jeda);
  digitalWrite(pin, 0);
  if (millis() - count > 1000) {
    count = millis();
    detik++;
    Serial.println(count);
  }
}
