from data.data_types import *

class Sensor:
    def __init__(self, id: int, data_type: DataType, name: str):
        self.id = id
        self.id = id
        self.name = name
        self.data_type = data_type

    def form_messagge(self, data):
        retData = self.data_type.get_text_value(data)
        return