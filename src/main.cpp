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

void canRecieve() {
  unsigned char packetSize = CAN.parsePacket();

  if (packetSize || CAN.packetId() != -1) {
    Serial.print(SOFR);
    Serial.print("\0\0\0\0"); // TIMESTAMP?? 
    Serial.print(CAN.packetDlc());
    Serial.print(CAN.packetId());
    unsigned char c = '\0';
    while(CAN.available()) {
      Serial.print(CAN.read());
    }
  }
}

void canSendPacket() {
  int timestamp = 0;
  int dlc = 0;
  int arb_id = 0;
  char payload[8];
  if(Serial.read() == SOFR) {
    for(int i = 0; i < 4; ++i) {
      timestamp += Serial.read() << i;
    }
    dlc = Serial.read();
    for(int i = 0; i < 4; ++i) {
      arb_id += Serial.read() << i;
    }
    for(int i = 0; i < dlc; ++i) {
      payload[i] = Serial.read();
    }
    if(Serial.read() != EOFR) {
      // HIBA TODO
    }

    // Becsomagolás és továbbküldés
    CAN.beginExtendedPacket(arb_id, dlc, false);
    for(int i = 0; i < dlc; ++i) {
      CAN.write(payload[i]);
    }
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

void canBusMonitor() {
  while(!Serial.available() || Serial.readString() != "exit") {
    canTest();
    if(CAN.available()) {
      canRecieve();
    }
  }
}

void loop() {
  if(Serial.available()) {
    String msg;
    msg = Serial.readString();
  
    canSendPacket();
    canRecieve();
  }
}
