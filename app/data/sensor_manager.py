from data.sensor import Sensor
from data_types import *

class SensorManager:
    sensors = {
        00000010101: Sensor(00000010101, THROTTLE_POSITION, "Throttle position"),
        00000110101: Sensor(00000110101, , "Switch positions(motor & dead mans's)"),
        00001010010: Sensor(00001010010, , "Motor RPM"),
        00001110000: Sensor(00001110000, , "Battery voltage"),
        00010010000: Sensor(00010010000, , ),
        00010110010: Sensor(00010110010, , ),
        00011010010: Sensor(00011010010, , ),
        00011110000: Sensor(00011110000, , ),
        00100010001: Sensor(00100010001, , ),
        00100110001: Sensor(00100110001, , ),
        00101010001: Sensor(00101010001, , ),
        00101110001: Sensor(00101110001, , ),
        00110010001: Sensor(00110010001, , ),
        00110110001: Sensor(00110110001, , ),
        00111010100: Sensor(00111010100, , ),
        00111111011: Sensor(00111111011, , ),
        01000011100: Sensor(01000011100, , ),
        01000111011: Sensor(01000111011, , ),
        01001010000: Sensor(01001010000, , ),
        01001110001: Sensor(01001110001, , ),
        01010010001: Sensor(01010010001, , ),
        01010110001: Sensor(01010110001, , ),
        01011010001: Sensor(01011010001, , ),
        01011110001: Sensor(01011110001, , ),
        01100010001: Sensor(01100010001, , ),
        01100110001: Sensor(01100110001, , ),
        01101010001: Sensor(01101010001, , ),
        01101110001: Sensor(01101110001, , ),
        01110010001: Sensor(01110010001, , ),
        01110110001: Sensor(01110110001, , ),
        01111010001: Sensor(01111010001, , ),
        01111110010: Sensor(01111110010, , ),
        10000010010: Sensor(10000010010, , ),
        10000110010: Sensor(10000110010, , ),
        10001010100: Sensor(10001010100, , ),
        10001110011: Sensor(10001110011, , ),
        10010010110: Sensor(10010010110, , ),
        10010110010: Sensor(10010110010, , ),
        10011010111: Sensor(10011010111, , ),
        10011110100: Sensor(10011110100, , ),
        10100010100: Sensor(10100010100, , ),
        10100111001: Sensor(10100111001, , ),
        10101010100: Sensor(10101010100, , ),
        10101110010: Sensor(10101110010, , ),
        10110010100: Sensor(10110010100, , ),
        10110110100: Sensor(10110110100, , ),
        10111010100: Sensor(10111010100, , ),
        10111110100: Sensor(10111110100, , ),
        11000010100: Sensor(11000010100, , ),
        11000110100: Sensor(11000110100, , ),
        11001010100: Sensor(11001010100, , ),
        11001110100: Sensor(11001110100, , ),
        11010010011: Sensor(11010010011, , ),
        11010110010: Sensor(11010110010, , ),
        11011010110: Sensor(11011010110, , ),
        11011110111: Sensor(11011110111, , )
    }






Battery temperature 1+2+3
Motor temperature
Motor controller temperature
Battery SoC
MPPT temperature 1
MPPT temperature 2
MPPT temperature 3
MPPT temperature 4
MPPT temperature 5
MPPT temperature 6
Coolant temp
Foil 1 position
Foil 2 position
Height(from water level)
Battery current
MPPT charge voltage 1
MPPT charge voltage 2
MPPT charge voltage 3
MPPT charge voltage 4
MPPT charge voltage 5
MPPT charge voltage 6
MPPT charge current 1
MPPT charge current 2
MPPT charge current 3
MPPT charge current 4
MPPT charge current 5
MPPT charge current 6
Motor controller current
Gearbox RPM
Motor Power(W)
Coolant level
Accubox air temperature
Solarbox air temperature
Motorbox air temperature
Telemetrybox air temperature
Ambient temperature
GPS time
RTC time
Coolant flow
Motor vibration
GPS speed
GPS position
Roll
Pitch
GPS heading
Magnetic heading
Wind direction
Wind speed
AccuboxFan RPM
MotorboxFan RPM
SolarboxFan RPM
TelemetryboxFan RPM
