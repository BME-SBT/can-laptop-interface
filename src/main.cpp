// Copyright (c) Sandeep Mistry. All rights reserved.
// Licensed under the MIT license. See LICENSE file in the project root for full license information.

#include <CAN.h>

void setup() {
  Serial.begin(115200);
  while (!Serial);

  SPI = MbedSPI(16,19,18);
  CAN.setClockFrequency(8E6);
  CAN.setSPIFrequency(250E4);
  CAN.setPins(17);
  

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
    Serial.print(" ");
    Serial.print(CAN.packetId(), HEX);
    Serial.print(" ");

    if (CAN.packetRtr()) {
      Serial.println(CAN.packetDlc());
    } else {
      Serial.print(packetSize);
      Serial.print(" ");
      while (CAN.available()) {
        Serial.print((char)CAN.read());
      }
    }

    Serial.println();
  } 
}

void canSendMsg() {

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
  delay(200);
  sendTestMassage2();
  canRecieve();
  delay(200);
  sendTestMessage3();
  canRecieve();
  delay(200);
}

void canBusMonitor() {
  while(Serial.readString() != "exit") {
    canRecieve();
    // canTest();
  }
}

void loop() {
  String msg;
  if(Serial.available()) {
    msg = Serial.readString();
  }

  if(msg == "monitor") {
    canBusMonitor();
  } else if(msg = "send") {
    canSendMsg();
  }
}