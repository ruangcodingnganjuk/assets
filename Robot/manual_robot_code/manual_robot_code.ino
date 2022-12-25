//Project : Manual Robot Baronas 2022
//Author  : Helda Pratama
#include "hardware.h"
#include "motor.h"

void setup() {
  hardwareInit();
  myServo.attach(11);
//  myServo.write(0);
//  delay(1000);
  Serial.println("set0");
}

void loop() {
 
  ps2x.read_gamepad(false, vibrate);
  readAnalogStick();

  //Motor Drive
//   if (key_r1) {
//    if (key_r2) setMotor(250,250,250,250);
//    else setMotor(100,100,100,100);
//  }
//  else if (key_r2) setMotor(250,250,250,250);
//  else setMotor(100,100,100,100);

//  if (key_up || analog.ly > 30){ setMotor(80,80,80,80); Serial.println("biasa");}//2
////  else if (key_up && key_r1){setMotor (200,200,200,200); Serial.println("turbo");}
//  else if (key_down || analog.ly < -30) setMotor(-100,-100,-100,-100);//1  setMotor(motor2,motor1,motor4,3);
//  else if (key_left || analog.lx > 30) setMotor(100,-100,100,-100);//4
//  else if (key_right || analog.lx < -30)setMotor(-100,100,-100,90);//3
//  else if (analog.rx < -30)setMotor(80,80,-80,-80);//3
//  else if (analog.rx > 30)setMotor(-80,-80,80,80);//3
//  else setMotor(0,0,0,0);

//if (key_up && key_r1 ){
//    setMotor (200,200,200,200);
//    Serial.println("maju turbo");
//}
//else setMotor (0,0,0,0);
/*
*
*/
//setMotor(motor2,motor1,motor4,motor3)
if (key_up || analog.ly > 30){
  setMotor(70,70,75,70);
  Serial.println("maju");
  if (key_r1 && key_up || key_r1 && analog.ly > 30){
    setMotor(170,180,170,180);
    Serial.println("maju turbo");
  }
}
else if (key_down || analog.ly < -30){
    setMotor(-80,-70,-80,-70);
    Serial.println("mundur");
    if (key_r1 && key_down || key_r1 && analog.ly < -30){
    setMotor(-180,-180,-155,-155);
    Serial.println("mundur turbo");
  }
}
else if (key_left || analog.lx > 30){
    setMotor(85,-85,85,-85);
    Serial.println("kiri");
    if (key_r1 && key_left || key_r1 && analog.lx > 30){
    setMotor(185,-185,180,-180);
    Serial.println("kiri turbo");
  }
}
else if (key_right || analog.lx < -30){
    setMotor(-80,80,-80,65);
    Serial.println("kanan");
    if (key_r1 && key_right || key_r1 && analog.lx < -30){
    setMotor(-180,180,-180,160);
    Serial.println("kanan turbo");
  }
}
else if (analog.rx < -30)setMotor(80,80,-80,-80);//3
else if (analog.rx > 30)setMotor(-80,-80,80,80);//3
else if (key_l1){
//  myServo.write(45);
//  delay(0);
  //myServo.write(90);

//  delay(0);
  myServo.write(naik);
  
}

else setMotor(0,0,0,0);

//  if (analog.rx > 30) vphi = runningSpeed;
//  else if (analog.rx < -30) vphi = -runningSpeed;
//  else vphi = 0;

  //omniDrive(vx, vy, vphi);
}

/*
#include "hardware.h"
#include "motor.h"

void setup() {
  hardwareInit();
}

void loop() {
  ps2x.read_gamepad(false, vibrate);
  readAnalogStick();

  //Motor Drive
  if (key_r1) {
    if (key_r2) runningSpeed = 250;
    else runningSpeed = 250;
  }
  else if (key_r2) runningSpeed = 250;
  else runningSpeed = 50;

  if (key_up || analog.ly > 30) vx = runningSpeed;
  else if (key_down || analog.ly < -30) vx = -runningSpeed;
  else vx = 0;

  if (key_left || analog.lx > 30) vy = runningSpeed;
  else if (key_right || analog.lx < -30) vy = -runningSpeed;
  else vy = 0;

  if (analog.rx > 30) vphi = runningSpeed;
  else if (analog.rx < -30) vphi = -runningSpeed;
  else vphi = 0;

  omniDrive(vx, vy, vphi);
}
*/
