from enum import Enum
import struct


class NumberType(Enum):
    FLOAT = '>f'
    DOUBLE = '>d'
    INT = '>i'
    UNSIGNED_INT = '>I'
    SHORT = '>h'
    UNSIGNED_SHORT = '>H'
    CHAR = '>b'
    UNSIGNED_CHAR = '>B'


class DataType:
    def __init__(self, number_type: NumberType, resolution, unit, dlc):
        self.number_type = number_type
        self.resolution = resolution
        self.unit = unit
        self.dlc = dlc

    def get_value(self, data):
        return struct.unpack(self.number_type.value, data)[0] / self.resolution

    def get_text_value(self, data):
        val = self.get_value(data)
        return f"{val} {self.unit}"

    def to_raw(self, value):
        return struct.pack(self.number_type.value, int((value / self.resolution)))
    
    def get_measure(self):
        return f"{self.unit}"


RPM = DataType(NumberType.SHORT, 1, '1/min', 2)
TEMPERATURE = DataType(NumberType.SHORT, 0.1, '°C', 2)
CURRENT = DataType(NumberType.SHORT, 0.1, 'A', 2)
MCURRENT = DataType(NumberType.SHORT, 1, 'mA', 2)
VOLTAGE = DataType(NumberType.SHORT, 0.01, 'V', 2)
SOC = DataType(NumberType.UNSIGNED_SHORT, 0.1, '%', 2)
THROTTLE_POSITION = DataType(NumberType.CHAR, 1, '%', 1)
SWITCH_POSITION = DataType(NumberType.UNSIGNED_CHAR, 1, '', 1)
GPS_POSITION = DataType(NumberType.FLOAT, 0.01, '°', 8)
SPEED = DataType(NumberType.SHORT, 0.1, 'km/h', 2)
ROLL_PITCH_DEGREE = DataType(NumberType.CHAR, 1, '°', 1)
HEADING = DataType(NumberType.UNSIGNED_SHORT, 1, 'sec', 2)
ABSOLUTTIME = DataType(NumberType.UNSIGNED_INT, 1, 'sec', 4)
POWER = DataType(NumberType.INT, 1, 'mW', 4)
ACCELERATION = DataType(NumberType.CHAR, 1, 'm/s^2', 1)
FLOW = DataType(NumberType.CHAR, 1, 'L\sec', 1)
DISTANCE = DataType(NumberType.SHORT, 1, 'mm', 2)
LEVEL = DataType(NumberType.CHAR, 1, '%', 1)
PERCENT = DataType(NumberType.SHORT, 0.1, '%', 2)
DEGREE = DataType(NumberType.SHORT, 0.1, '°', 2)