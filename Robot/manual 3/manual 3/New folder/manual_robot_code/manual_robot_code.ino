//Project : Manual Robot Baronas 2022
//Board   : Arduino Mega
//Author  : Helda Pratama

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
    if (key_r2) runningSpeed = 130;
    else runningSpeed = 80;
  }
  else if (key_r2) runningSpeed = 200;
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

  //Servo Drive
  if (key_square) {
    servoGripState = 160;
    delay(10);
  }
  if (key_cross) {
    servoGripState = 110;
    delay(10);
  }
  servoGrip.write(servoGripState);

  if (key_l1) {
    servoLift.write(1050); //1050
    delay(10);
  }
  else if (key_l2) {
    servoLift.write(1550);
    delay(10);
  }
  else {
    servoLift.write(1480);
    delay(10);
  }
}
