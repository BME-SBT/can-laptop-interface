from PySide6.QtWidgets import *
#from PySide6 import QtCore, QtGui
from PySide6.QtGui import *
from PySide6.QtCore import *
from scrolllabel import ScrollLabel
import sys
import serial
from datetime import datetime
import serial.tools.list_ports

class MonitorWidget(QWidget):
    
    def __init__(self, app):

        QWidget.__init__(self)

        app = app
        
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
        self.label_received_messages = QLabel(self.received_messages)
        self.label_received_messages.setWordWrap(True)
        self.label_received_messages.setMinimumHeight(600)
        self.label_received_messages.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        
        # Initialize the scrollable label
        self.scrolllabel = ScrollLabel(self)
        self.monitor_running = False
        self.scrolllabel.setText(self.received_messages )
        self.timer = QTimer()
        self.timer.timeout.connect(self.monitoring)
        self.timer.start(1000)

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
        msg = self.ser.readline().decode('utf-8').split()
        extended = msg[0][0] == "1"
        rtr = msg[0][1] == "1"
        id = msg[1]
        len = msg[2]
        ret = ""
        
        if msg == "400":
            ret += "Starting of the CAN bus failed!"
        else:
            ret += "Recieved "
            if extended:
                ret += "extended "
            if rtr:
                ret += "RTR "
            
            ret += f"packet with the id 0x{id}"

            if rtr:
                ret += f" and requested length {len}"
            else:
                can_msg = msg[3]
                ret += f" and length {len}:\n {can_msg}\n\n"

        return ret

    def port_number_button(self):
        try:
            usb = self.lineedit_port.text()
            self.ser = serial.Serial(usb, 115200)
            self.ser.write('monitor'.encode('utf-8'))
            self.monitor_running = True
        except serial.SerialException:
            self.write_error("Invalid port added!")


    def write_error(self, message):
        self.label_error.setText(message)
        self.label_error.show()
        self.error_timer.start(2000)
        
    
    def hide_error(self):
        self.label_error.hide()
        
    def monitoring(self):
        if(self.monitor_running == True):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            new_message = current_time + ' ' + self.message_reader() + '\n'
            self.received_messages += new_message
            self.scrolllabel.setText(self.received_messages)
    
    def back_pushed(self):
        self.app.main_layout.setCurrentIndex(0)
        self.received_messages = "Recieved messages:\n\n"
        self.scrolllabel.setText(self.received_messages)
        try:
            self.ser.write('exit'.encode('utf-8'))
        except:
            pass
        self.monitor_running = False

    def UiComponents(self): 
        # creating scroll label
        label = ScrollLabel(self)
 
        # setting text to the label
        label.setText(self.received_messages)
 
        # setting geometry
        label.setGeometry(100, 100, 200, 80)