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
            usb = self.lineedit_port.text()
            self.ser = serial.Serial(usb, 115200)
            # self.ser = serial.serial_for_url('loop://', timeout=1) # loopback for testing
            self.sendPacket()
        except serial.SerialException:
            self.write_error("Invalid port added!")
    
    def sendPacket(self):
        printMsg = ""
        msg = self.lineedit_message.text()
        ser = self.ser

        # Chechwether the id is valid
        id = int(self.lineedit_id.text())
        dlc = int(self.lineedit_dlc.text())
        # More profound validaion i the future
        if id > int("0xFFFFFFFF", base=16):
            self.write_error("Invalid id!")
        else:
            if len(msg) > dlc:
                self.write_error("Message is too long!")
            else:
                if dlc > 8:
                    self.write_error("DLC is must be between 0 and 8!")
                else:
                    ser.write(b'\xAA') #start of rame: 1 byte
                    timestamp = int((time.time() - self.sendStart) * 1000)
                    ser.write(pack('<I', timestamp)) #time stamp
                    ser.write(pack('<B', dlc))
                    ser.write(bytes(msg.encode('utf-8')))
                    ser.write(b'\xBB')
                    printMsg += f'Sent package with timestamp: {timestamp} and with the id: {id} and length: {dlc}\n{msg}\n\n'

        # while ser.in_waiting:   # print bytes to console for testing
        #     print(ser.read())

        ser.close()
        ser = None
        
        self.sent_messages += printMsg
        self.scrolllabel.setText(self.sent_messages)

    def update_measure(self, index):
        keys = list(self.sensor_manager.sensors.keys())
        sensor = self.sensor_manager.sensors[keys[index]]
        self.label_measure.setText(sensor.data_type.get_measure())

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