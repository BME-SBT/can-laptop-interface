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
#define SOF 170

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
    // try to parse packet
  int packetSize = CAN.parsePacket();

  if (packetSize || CAN.packetId() != -1) {

    if (CAN.packetExtended()) {
      Serial.print("1");
    } else {
      Serial.print("0");
    }

    if (CAN.packetRtr()) {
      // Remote transmission request, packet contains no data
      Serial.print("1");
    } else {
      Serial.print("0");
    }

    // Padding after the can ID for unequivocally decodable messages
    Serial.print(delimiter);
    Serial.print(CAN.packetId(), HEX);
    Serial.print(delimiter);

    if (CAN.packetRtr()) {
      Serial.println(CAN.packetDlc());
    } else {
      Serial.print(packetSize);
      Serial.print(delimiter);
      while (CAN.available()) {
        Serial.print((char)CAN.read());
      }
    }

    Serial.println();
  } 
}

void canSendPacket() {
  int timestamp;
  int arb_id;
  int dlc;
  int payload;
  if(Serial.read() == SOF) {
    for(int i = 0; i < 4; ++i) {
      
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
  
    if(msg == "monitor") {
      canBusMonitor();
    } else if(msg = "send") {
      canSendPacket();
    }
  }
}
