from data.sensor import Sensor
from data.data_types import *

class SensorManager:
    sensors = {
        # Protocol created by the legend Márk Bakonyi
        517: Sensor(517, THROTTLE_POSITION, "Throttle position"),
        525: Sensor(525, SWITCH_POSITION, "Switch positions(motor & dead mans's)"),
        530: Sensor(530, RPM, "Motor RPM"),
        536: Sensor(536, VOLTAGE, "Battery voltage"),
        544: Sensor(544, TEMPERATURE,"Battery temperature 1+2+3"),
        554: Sensor(554, TEMPERATURE, "Motor temperature"),
        562: Sensor(562, TEMPERATURE, "Motor controller temperature"),
        568: Sensor(568, SOC, "Battery SoC"),
        577: Sensor(577, TEMPERATURE, "MPPT temperature 1"),
        585: Sensor(585, TEMPERATURE, "MPPT temperature 2"),
        593: Sensor(593, TEMPERATURE, "MPPT temperature 3"),
        601: Sensor(601, TEMPERATURE, "MPPT temperature 4"),
        609: Sensor(609, TEMPERATURE, "MPPT temperature 5"),
        617: Sensor(617, TEMPERATURE, "MPPT temperature 6"),
        628: Sensor(628, TEMPERATURE, "Coolant temp"),
        643: Sensor(643, TEMPERATURE, "Foil 1 position"),
        652: Sensor(652, TEMPERATURE, "Foil 2 position"),
        659: Sensor(659, DISTANCE, "Height(from water level)"),
        656: Sensor(656, CURRENT, "Battery current"),
        665: Sensor(665, VOLTAGE, "MPPT charge voltage 1"),
        673: Sensor(673, VOLTAGE, "MPPT charge voltage 2"),
        681: Sensor(681, VOLTAGE, "MPPT charge voltage 3"),
        689: Sensor(689, VOLTAGE, "MPPT charge voltage 4"),
        697: Sensor(697, VOLTAGE, "MPPT charge voltage 5"),
        705: Sensor(705, VOLTAGE, "MPPT charge voltage 6"),
        713: Sensor(713, MCURRENT, "MPPT charge current 1"),
        721: Sensor(721, MCURRENT, "MPPT charge current 2"),
        729: Sensor(729, MCURRENT, "MPPT charge current 3"),
        737: Sensor(737, MCURRENT, "MPPT charge current 4"),
        745: Sensor(745, MCURRENT, "MPPT charge current 5"),
        753: Sensor(753, MCURRENT, "MPPT charge current 6"),
        762: Sensor(762, CURRENT, "Motor controller current"), #EZ
        770: Sensor(770, RPM, "Gearbox RPM"),
        778: Sensor(778, POWER, "Motor Power(W)"),
        788: Sensor(788, LEVEL, "Coolant level"),
        795: Sensor(795, TEMPERATURE, "Accubox air temperature"),
        806: Sensor(806, TEMPERATURE, "Solarbox air temperature"),
        810: Sensor(810, TEMPERATURE, "Motorbox air temperature"),
        823: Sensor(823, TEMPERATURE, "Telemetrybox air temperature"),
        828: Sensor(828, TEMPERATURE, "Ambient temperature"),
        836: Sensor(836, HEADING, "GPS time"), #EZ
        849: Sensor(849, ABSOLUTTIME, "RTC time"), #EZ
        852: Sensor(852, FLOW, "Coolant flow"),
        858: Sensor(858, DISTANCE, "Motor vibration"), #EZ
        868: Sensor(868, SPEED, "GPS speed"),
        876: Sensor(876, GPS_POSITION, "GPS position"),
        884: Sensor(884, ROLL_PITCH_DEGREE, "Roll"), #EZ
        892: Sensor(892, ROLL_PITCH_DEGREE, "Pitch"),
        900: Sensor(900, HEADING, "GPS heading"),
        908: Sensor(908, HEADING, "Magnetic heading"),
        916: Sensor(916, DEGREE, "Wind direction"),
        924: Sensor(924, SPEED, "Wind speed"),
        931: Sensor(931, RPM, "AccuboxFan RPM"),
        938: Sensor(938, RPM, "MotorboxFan RPM"),
        950: Sensor(950, RPM, "SolarboxFan RPM"),
        959: Sensor(959, RPM, "TelemetryboxFan RPM")
    }