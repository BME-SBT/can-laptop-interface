from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from gui.scrolllabel import ScrollLabel
from data.sensor_manager import SensorManager
import serial
import serial.tools.list_ports
import time
from struct import *

class SendWidget(QWidget):

    def __init__(self, app):
        QWidget.__init__(self)

        self.app = app
        self.ser = None
        self.send_start = time.time()
        self.sensor_manager = SensorManager()
        self.sensor = self.sensor_manager.sensors.get(517)

        send_layout = QVBoxLayout()

        # Setup labels and buttons

        label_send = QLabel("Sender View")
        label_basic_information = QLabel("Basic description in the future")
        label_port = QLabel("Port: ")
        self.lineedit_port = QLineEdit()

        label_id = QLabel("Id: ")
        self.combo_id = QComboBox()
        for key in self.sensor_manager.sensors:
            self.combo_id.addItem(self.sensor_manager.sensors[key].name)
        self.combo_id.currentIndexChanged.connect(self.update_measure)
        label_message = QLabel("Message: ")
        self.lineedit_message = QLineEdit()
        self.label_measure = QLabel("")

        btn_port = QPushButton("Send")
        btn_port.clicked.connect(self.port_number_button)

        self.sent_messages = "Sent messages:\n\n"

        # Initialize the scrollable label
        self.scrolllabel = ScrollLabel(self)
        self.scrolllabel.setText(self.sent_messages)

        # Initialize the "back" button
        self.btn_back = QPushButton("Back")
        self.btn_back.clicked.connect(self.back_pushed)

        # Initialize the error label and its timer
        self.label_error = QLabel()
        self.label_error.setStyleSheet("background-color: red; border: 1px solid black;")
        self.label_error.setHidden(True)
        self.error_timer = QTimer()
        # self.error_timer.setSingleShot(True)
        self.error_timer.timeout.connect(self.hide_error)

        send_layout.addWidget(label_send)
        send_layout.addWidget(label_basic_information)
        send_layout.addWidget(label_port)
        send_layout.addWidget(self.lineedit_port)
        send_layout.addWidget(label_id)
        send_layout.addWidget(self.combo_id)
        send_layout.addWidget(label_message)
        send_layout.addWidget(self.lineedit_message)
        send_layout.addWidget(self.label_measure)
        send_layout.addWidget(btn_port)
        send_layout.addWidget(self.scrolllabel)
        send_layout.addWidget(self.btn_back)
        send_layout.addWidget(self.label_error)

        self.setLayout(send_layout)

    def port_number_button(self):
        try:
            # usb = self.lineedit_port.text()
            # self.ser = serial.Serial(usb, 115200)
            if self.ser is None:
                self.ser = serial.serial_for_url('loop://', timeout=1) # loopback for testing
            self.sendPacket()
        except serial.SerialException:
            self.write_error("Invalid port added!")
    
    def sendPacket(self):
        printMsg = "" # message printed on the gui
        msgInBytes = b''
        # try parsing the message
        try:
            start_of_frame = b'\xAA'
            msgInBytes += start_of_frame
            timestamp = pack('<i', (int(time.time() - self.send_start)))
            msgInBytes += timestamp
            print(timestamp)
            dlc = pack('<B', int(self.sensor.data_type.dlc))
            id = pack('<i', int(self.sensor.id))
            print(id)
            payload = self.sensor.data_type.to_raw(int(self.lineedit_message.text()))
            msgInBytes += payload
            end_of_frame = b'\xBB'
            msgInBytes += end_of_frame
            self.ser.write(start_of_frame)
            self.ser.write(timestamp)
            self.ser.write(dlc)
            self.ser.write(id)
            self.ser.write(payload)
            self.ser.write(end_of_frame)
            printMsg = f'Sent package with the timestamp: {timestamp[0]} from the sensor: {self.sensor.name} with the id: {self.sensor.id} and length {self.sensor.data_type.dlc} and message {self.lineedit_message.text()}:\n{msgInBytes}\n\n'
        except:
            self.write_error("Couldn't parse packet, message might be out of range!")

        # self.ser.close()
        # self.ser = None
        
        self.sent_messages += printMsg
        self.scrolllabel.setText(self.sent_messages)

    def update_measure(self, index):
        keys = list(self.sensor_manager.sensors.keys())
        self.sensor = self.sensor_manager.sensors[keys[index]]
        self.id = self.sensor.id
        self.label_measure.setText(self.sensor.data_type.get_measure())

    def hide_error(self):
        self.label_error.hide()

    def write_error(self, message):
        self.label_error.setText(message)
        self.label_error.show()
        self.error_timer.start(2000)

    def back_pushed(self):
        self.sent_messages = "Sent messages:\n\n"
        self.scrolllabel.setText(self.sent_messages)
        self.app.main_layout.setCurrentIndex(0)

    def UiComponents(self): 
        # creating scroll label
        label = ScrollLabel(self)
 
        # setting text to the label
        label.setText(self.received_messages)
 
        # setting geometry
        label.setGeometry(100, 100, 200, 80)