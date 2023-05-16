// Copyright (c) Sandeep Mistry. All rights reserved.
// Licensed under the MIT license. See LICENSE file in the project root for full license information.

#include <CAN.h>
#include <string>

#define MISO 16 // Master in slave out
#define MOSI 19 // Master out slave in
#define SCK 18 // Serial clock
#define CS 17 // Serial chip select
#define CAN_CKFR 8E6 // Can clock frequency
#define CAN_SPIFR 250E4 // Can SPI frequency
#define SOFR 170 // Start of frame on can over serial
#define EOFR 187 // End of frame on can over serial

char bufferIn[8];
char bufferOut[8];

void setup() {
  Serial.begin(115200);
  while (!Serial);

  SPI = MbedSPI(MISO, MOSI, SCK);
  CAN.setClockFrequency(CAN_CKFR);
  CAN.setSPIFrequency(CAN_SPIFR);
  CAN.setPins(CS);
  pinMode(LED_BUILTIN, OUTPUT); // for testing

  // start the CAN bus at 250 kbps
  if (!CAN.begin(250E3)) {
    Serial.println("400");
    while (1);
  }

  CAN.loopback();
}

// makes the littleEndian  inBuffer's value to big endian in outbuffer
void bigToLittleEndian(int length) {
  for(int i = 0; i < length; ++i) {
    bufferOut[i]  = bufferIn[length - 1 - i];
  }
}

void littleToBigEndian(int length) {
  for(int i = 0; i < length; ++i) {
    bufferOut[length - 1 - i] = bufferIn[i];
  }
}

// Prints length character of the bufferOut to the serial
void printBufferToSerial(int length) {
  for (int i = 0; i < length; i++) {
    Serial.print(bufferOut[i]);
  }
  
}

int bufferOutToIntAsBigEndian(int length) {
  int ret = 0;
  for(int i = 0; i < length; ++i) {
    ret += bufferOut[i] << 8 * i;
  }
  return ret;
}

void canRecieve() {
  unsigned char packetSize = CAN.parsePacket();

  if (packetSize || CAN.packetId() != -1) {
    Serial.print(SOFR);
    Serial.print("\0\0\0\0"); // TIMESTAMP, not interpreted
    unsigned char dlc = CAN.packetDlc();
    Serial.print(dlc);
    // read id
    CAN.readBytes(bufferIn, 4);
    // print it on serial as little-endian
    bigToLittleEndian(4);
    printBufferToSerial(4);
    // read payload
    CAN.readBytes(bufferIn, dlc);
    bigToLittleEndian(dlc);
    printBufferToSerial(dlc);
    Serial.print(EOFR);
  }
}

void canSendPacket() {
  if(Serial.read() == SOFR) {
    unsigned int timeStamp = Serial.readBytes(bufferIn, 4); // TIMESTAMP, not used in our CAN protocol interpreted as a little-endian value
    unsigned int dlc = Serial.read();
    Serial.readBytes(bufferIn, 4);
    littleToBigEndian(4);
    int arb_id = bufferOutToIntAsBigEndian(4);
    CAN.beginExtendedPacket(arb_id, dlc, false);
    Serial.readBytes(bufferIn, dlc);
    littleToBigEndian(dlc);
    for(int i = 0; i < dlc; ++i) {
      CAN.write(bufferOut[i]);
    }
    CAN.endPacket();
  }
}

void sendTestMassage1() {
  CAN.beginPacket(0x12);
  CAN.write('h');
  CAN.write('e');
  CAN.write('l');
  CAN.write('l');
  CAN.write('o');
  CAN.endPacket();
}

void sendTestMassage2() {
  CAN.beginExtendedPacket(0xabcdef);
  CAN.write('w');
  CAN.write('o');
  CAN.write('r');
  CAN.write('l');
  CAN.write('d');
  CAN.endPacket();
}

void sendTestMessage3() {
  CAN.beginExtendedPacket(0x24);
  CAN.write('D');
  CAN.write('I');
  CAN.write('K');
  CAN.write('K');
  CAN.write('K');
  CAN.endPacket();
}

void canTest() {
  sendTestMassage1();
  canRecieve();
  delay(4000);
  sendTestMassage2();
  canRecieve();
  delay(6000);
  sendTestMessage3();
  canRecieve();
  delay(5000);
}

void loop() {
  if(Serial.available()) {  
    canSendPacket();
  }
  if(CAN.available()) {
    canRecieve();
  }
}
