// Copyright (c) Sandeep Mistry. All rights reserved.
// Licensed under the MIT license. See LICENSE file in the project root for full license information.

#include <CAN.h>

void setup() {
  Serial.begin(115200);
  while (!Serial);

  Serial.println("CAN Reciever");
  SPI = MbedSPI(16,19,18);
  CAN.setClockFrequency(8E6);
  CAN.setSPIFrequency(2500000);
  CAN.setPins(17);
  

  // start the CAN bus at 500 kbps
  if (!CAN.begin(250E3)) {
    Serial.println("Starting CAN failed!");
    while (1);
  }
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

    Serial.print(CAN.packetId(), HEX);

    if (CAN.packetRtr()) {
      Serial.println(CAN.packetDlc());
    } else {
      Serial.print(packetSize);
      while (CAN.available()) {
        Serial.print((char)CAN.read());
      }
      Serial.println();
    }
  } 
}

void canBusMonitor() {
  String msg = "OK";

  while(msg == "OK") {
    canRecieve();
    msg = Serial.readString();
  }
}

void loop() {
  String msg;
  if(Serial.available()) {
    msg = Serial.readString();
  }

  if(msg == "monitor") {
    canBusMonitor();
  }
}