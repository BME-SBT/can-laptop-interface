from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from scrolllabel import ScrollLabel
import serial
from datetime import datetime
import serial.tools.list_ports

class SendWidget(QWidget):

    def __init__(self, app):
        QWidget.__init__(self)

        self.app = app

        send_layout = QVBoxLayout()

        # Setup labels and buttons

        label_send = QLabel("Sender View")
        label_basic_information = QLabel("Basic description in the future")
        label_port = QLabel("Port: ")
        self.lineedit_port = QLineEdit()
        btn_port = QPushButton("Send to port")
        btn_port.clicked.connect(self.port_number_button)

        label_id = QLabel("Id: ")
        self.combo_id = QComboBox()
        # self.list_id.setEchoMode(QLineEdit.NoEcho)
        label_message = QLabel("Message: ")
        self.lineedit_message = QLineEdit()
        self.lineedit_message.setEchoMode(QLineEdit.NoEcho)

        # Initialization of the label showcasing the messages
        self.sent_messages = "Sent messages:\n\n"
        self.label_received_messages = QLabel(self.sent_messages)
        self.label_received_messages.setWordWrap(True)
        self.label_received_messages.setMinimumHeight(600)
        self.label_received_messages.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        
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
        send_layout.addWidget(btn_port)
        send_layout.addWidget(label_id)
        send_layout.addWidget(self.combo_id)
        send_layout.addWidget(label_message)
        send_layout.addWidget(self.lineedit_message)
        send_layout.addWidget(self.scrolllabel)
        send_layout.addWidget(self.btn_back)
        send_layout.addWidget(self.label_error)

        self.setLayout(send_layout)

    def port_number_button(self):
        try:
            usb = self.lineedit_port.text()
            self.ser = serial.Serial(usb, 115200)
            self.ser.write('send'.encode('utf-8'))
            self.monitor_running = True
        except serial.SerialException:
            self.write_error("Invalid port added!")
    
    def hide_error(self):
        self.label_error.hide()

    def write_error(self, message):
        self.label_error.setText(message)
        self.label_error.show()
        self.error_timer.start(2000)

    def back_pushed(self):
        self.app.main_layout.setCurrentIndex(0)

    def UiComponents(self): 
        # creating scroll label
        label = ScrollLabel(self)
 
        # setting text to the label
        label.setText(self.received_messages)
 
        # setting geometry
        label.setGeometry(100, 100, 200, 80)