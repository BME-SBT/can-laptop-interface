from data.sensor import Sensor
from data_types import *

class SensorManager:
    sensors = {
        00000010101: Sensor(00000010101, THROTTLE_POSITION, "Throttle position"),
        00000110101: Sensor(00000110101, SWITCH_POSITION, "Switch positions(motor & dead mans's)"),
        00001010010: Sensor(00001010010, RPM, "Motor RPM"),
        00001110000: Sensor(00001110000, VOLTAGE, "Battery voltage"),
        00010010000: Sensor(00010010000, TEMPERATURE,"Battery temperature 1+2+3"),
        00010110010: Sensor(00010110010, TEMPERATURE, "Motor temperature"),
        00011010010: Sensor(00011010010, TEMPERATURE, "Motor controller temperature"),
        00011110000: Sensor(00011110000, SOC, "Battery SoC"),
        00100010001: Sensor(00100010001, TEMPERATURE, "MPPT temperature 1"),
        00100110001: Sensor(00100110001, TEMPERATURE, "MPPT temperature 2"),
        00101010001: Sensor(00101010001, TEMPERATURE, "MPPT temperature 3"),
        00101110001: Sensor(00101110001, TEMPERATURE, "MPPT temperature 4"),
        00110010001: Sensor(00110010001, TEMPERATURE, "MPPT temperature 5"),
        00110110001: Sensor(00110110001, TEMPERATURE, "MPPT temperature 6"),
        00111010100: Sensor(00111010100, TEMPERATURE, "Coolant temp"),
        00111111011: Sensor(00111111011, TEMPERATURE, "Foil 1 position"),
        01000011100: Sensor(01000011100, TEMPERATURE, "Foil 2 position"),
        01000111011: Sensor(01000111011, DISTANCE, "Height(from water level)"),
        01001010000: Sensor(01001010000, CURRENT, "Battery current"),
        01001110001: Sensor(01001110001, VOLTAGE, "MPPT charge voltage 1"),
        01010010001: Sensor(01010010001, VOLTAGE, "MPPT charge voltage 2"),
        01010110001: Sensor(01010110001, VOLTAGE, "MPPT charge voltage 3"),
        01011010001: Sensor(01011010001, VOLTAGE, "MPPT charge voltage 4"),
        01011110001: Sensor(01011110001, VOLTAGE, "MPPT charge voltage 5"),
        01100010001: Sensor(01100010001, VOLTAGE, "MPPT charge voltage 6"),
        01100110001: Sensor(01100110001, MCURRENT, "MPPT charge current 1"),
        01101010001: Sensor(01101010001, MCURRENT, "MPPT charge current 2"),
        01101110001: Sensor(01101110001, MCURRENT, "MPPT charge current 3"),
        01110010001: Sensor(01110010001, MCURRENT, "MPPT charge current 4"),
        01110110001: Sensor(01110110001, MCURRENT, "MPPT charge current 5"),
        01111010001: Sensor(01111010001, MCURRENT, "MPPT charge current 6"),
        01111110010: Sensor(01111110010, CURRENT, "Motor controller current"), #EZ
        10000010010: Sensor(10000010010, RPM, "Gearbox RPM"),
        10000110010: Sensor(10000110010, POWER, "Motor Power(W)"),
        10001010100: Sensor(10001010100, LEVEL, "Coolant level"),
        10001110011: Sensor(10001110011, TEMPERATURE, "Accubox air temperature"),
        10010010110: Sensor(10010010110, TEMPERATURE, "Solarbox air temperature"),
        10010110010: Sensor(10010110010, TEMPERATURE, "Motorbox air temperature"),
        10011010111: Sensor(10011010111, TEMPERATURE, "Telemetrybox air temperature"),
        10011110100: Sensor(10011110100, TEMPERATURE, "Ambient temperature"),
        10100010100: Sensor(10100010100, HEADING, "GPS time"), #EZ
        10100111001: Sensor(10100111001, ABSOLUTTIME, "RTC time"), #EZ
        10101010100: Sensor(10101010100, FLOW, "Coolant flow"),
        10101110010: Sensor(10101110010, DISTANCE, "Motor vibration"), #EZ
        10110010100: Sensor(10110010100, SPEED, "GPS speed"),
        10110110100: Sensor(10110110100, GPS_POSITION, "GPS position"),
        10111010100: Sensor(10111010100, ROLL_PITCH_DEGREE, "Roll"), #EZ
        10111110100: Sensor(10111110100, ROLL_PITCH_DEGREE, "Pitch"),
        11000010100: Sensor(11000010100, HEADING, "GPS heading"),
        11000110100: Sensor(11000110100, HEADING, "Magnetic heading"),
        11001010100: Sensor(11001010100, DEGREE, "Wind direction"),
        11001110100: Sensor(11001110100, SPEED, "Wind speed"),
        11010010011: Sensor(11010010011, RPM, "AccuboxFan RPM"),
        11010110010: Sensor(11010110010, RPM, "MotorboxFan RPM"),
        11011010110: Sensor(11011010110, RPM, "SolarboxFan RPM"),
        11011110111: Sensor(11011110111, RPM, "TelemetryboxFan RPM")
    }