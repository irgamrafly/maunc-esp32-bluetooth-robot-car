#include "BluetoothSerial.h"

BluetoothSerial SerialBT;

// Motor kiri
#define IN1 25
#define IN2 27
#define ENA 18

// Motor kanan
#define IN3 26
#define IN4 33
#define ENB 19

#define MOTOR_SPEED 200

// Pengaturan jeda berhenti
unsigned long waktuStop = 0;
bool stopPending = false;

const unsigned long DELAY_STOP = 100;

// ========================
// BERHENTI
// ========================
void berhenti() {
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}

// ========================
// MAJU
// ========================
void maju() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);

  analogWrite(ENA, MOTOR_SPEED);
  analogWrite(ENB, MOTOR_SPEED);
}

// ========================
// MUNDUR
// ========================
void mundur() {
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
  delay(50);

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);

  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);

  analogWrite(ENA, MOTOR_SPEED);
  analogWrite(ENB, MOTOR_SPEED);
}

// ========================
// BELOK KIRI
// Kanan maju, kiri mundur
// ========================
void kiri() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);

  analogWrite(ENA, MOTOR_SPEED);
  analogWrite(ENB, MOTOR_SPEED);
}

// ========================
// BELOK KANAN
// Kiri maju, kanan mundur
// ========================
void kanan() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);

  analogWrite(ENA, MOTOR_SPEED);
  analogWrite(ENB, MOTOR_SPEED);
}

// ========================
// SETUP
// ========================
void setup() {
  Serial.begin(115200);

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENA, OUTPUT);

  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENB, OUTPUT);

  berhenti();

  SerialBT.begin("MAUNC_Robot_2");

  Serial.println("MAUNC Robot 2 siap!");
}

// ========================
// LOOP
// ========================
void loop() {

  // Membaca semua perintah Bluetooth yang tersedia
  while (SerialBT.available()) {

    char perintah = SerialBT.read();

    Serial.print("Perintah: ");
    Serial.println(perintah);

    switch (perintah) {

      case 'F':
      case 'T':
        stopPending = false;
        maju();
        break;

      case 'B':
        stopPending = false;
        mundur();
        break;

      case 'L':
        stopPending = false;
        kiri();
        break;

      case 'R':
        stopPending = false;
        kanan();
        break;

      case 'S':
      case 'X':
      case 'C':
      case 'A':
      case 'P':
        stopPending = true;
        waktuStop = millis();
        break;
    }
  }

  // Berhenti jika selama 100 ms
  // tidak ada perintah gerakan baru
  if (stopPending &&
      millis() - waktuStop >= DELAY_STOP) {

    berhenti();
    stopPending = false;
  }
}
