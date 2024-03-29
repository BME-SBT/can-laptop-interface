from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from gui.scrolllabel import ScrollLabel
from data.data_types import *
from data.sensor import *
from data.sensor_manager import *
from datetime import *
import serial
import serial.tools.list_ports
from struct import *

class MonitorWidget(QWidget):
    
    def __init__(self, app):

        QWidget.__init__(self)

        self.app = app
        self.sensor_manager = SensorManager()
        
        monitor_layout = QVBoxLayout()

        # Setup labels and buttons

        label_monitor = QLabel("Monitor view")
        label_basic_information = QLabel("Basic description in the future")
        label_port = QLabel("Port: ")
        self.lineedit_port = QLineEdit()
        btn_port = QPushButton("Show port")
        btn_port.clicked.connect(self.port_number_button)

        # Initialization of the label showcasing the messages
        self.received_messages = "Recieved messages:\n\n"
        
        # Initialize the scrollable label
        self.scrolllabel = ScrollLabel(self)
        self.monitor_running = False
        self.scrolllabel.setText(self.received_messages )
        self.timer = QTimer()
        self.timer.timeout.connect(self.monitoring)

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

        monitor_layout.addWidget(label_monitor)
        monitor_layout.addWidget(label_basic_information)
        monitor_layout.addWidget(label_port)
        monitor_layout.addWidget(self.lineedit_port)
        monitor_layout.addWidget(btn_port)
        monitor_layout.addWidget(self.scrolllabel)
        monitor_layout.addWidget(self.btn_back)
        monitor_layout.addWidget(self.label_error)

        self.setLayout(monitor_layout)

    def message_reader(self):
        print("a")
        ser = self.ser
        sensor: Sensor
        try:
            if ser.read(1) == (b'\xAA'): 
                timestamp = unpack("<I", ser.read(4))[0]
                dlc = unpack("<B", ser.read(1))[0]
                id = unpack("<I", ser.read(4))[0]
                sensor = SensorManager.sensors[id]
                payload = sensor.form_messagge(ser.read(int(dlc)))
                print(payload)
                end_of_frame = ser.read(1)
            else:
                self.write_error("Wrong package on serial")

            if end_of_frame != None:
                if end_of_frame == b'\xBB':
                    return f'{datetime.now()} Recieved package with the timestamp: {timestamp} from the sensor: {sensor.name} with the id: {sensor.id} and length {dlc}:\n {payload}\n\n'
                else:
                    self.write_error("Wrong package on serial")
                    return ""
        except:
            self.write_error("Wrong package on serial")
            return ""

    def port_number_button(self):
        try:
            usb = self.lineedit_port.text()
            self.ser = serial.Serial(usb, 115200)
            self.timer.start(1000)

            # self.ser = serial.serial_for_url('loop://', timeout=1) # loopback for testing with test message
            # ser = self.ser
            # ser.write(b'\xAA')
            # ser.write(b'\x66\x73\x00\x00')
            # ser.write(b'\x01')
            # ser.write(b'\x05\x02\x00\x00')
            # ser.write(b'\x01')
            # ser.write(b'\xBB')
        except serial.SerialException:
            self.write_error("Invalid port added!")


    def write_error(self, message):
        self.label_error.setText(message)
        self.label_error.show()
        self.error_timer.start(2000)
        
    
    def hide_error(self):
        self.label_error.hide()
        
    def monitoring(self):
        while self.ser.in_waiting:
            new_message = self.message_reader()
            print(new_message)
            self.received_messages += new_message
            print("w")
            self.scrolllabel.setText(self.received_messages)
            print("a")
    
    def back_pushed(self):
        self.app.main_layout.setCurrentIndex(0)
        self.received_messages = "Recieved messages:\n\n"
        self.scrolllabel.setText(self.received_messages)
        if 'ser' in locals():
            self.ser.close()
            self.ser = None
        self.monitor_running = False

    def UiComponents(self): 
        # creating scroll label
        label = ScrollLabel(self)
 
        # setting text to the label
        label.setText(self.received_messages)
 
        # setting geometry
        label.setGeometry(100, 100, 200, 80)