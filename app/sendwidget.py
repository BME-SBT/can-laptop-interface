from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from scrolllabel import ScrollLabel
import serial
from datetime import datetime
import serial.tools.list_ports
import time

class SendWidget(QWidget):

    def __init__(self, app):
        QWidget.__init__(self)

        self.app = app
        self.ser = None

        send_layout = QVBoxLayout()

        # Setup labels and buttons

        label_send = QLabel("Sender View")
        label_basic_information = QLabel("Basic description in the future")
        label_port = QLabel("Port: ")
        self.lineedit_port = QLineEdit()

        label_id = QLabel("Id: ")
        self.lineedit_id = QLineEdit()
        # self.list_id.setEchoMode(QLineEdit.NoEcho)
        label_message = QLabel("Message: ")
        self.lineedit_message = QLineEdit()
        #self.lineedit_message.setEchoMode(QLineEdit.NoEcho)

        self.check_extended = QCheckBox("extended")
        self.check_rtr = QCheckBox("RTR")

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
        send_layout.addWidget(self.lineedit_id)
        send_layout.addWidget(self.check_extended)
        send_layout.addWidget(self.check_rtr)
        send_layout.addWidget(label_message)
        send_layout.addWidget(self.lineedit_message)
        send_layout.addWidget(btn_port)
        send_layout.addWidget(self.scrolllabel)
        send_layout.addWidget(self.btn_back)
        send_layout.addWidget(self.label_error)

        self.setLayout(send_layout)

    def port_number_button(self):
        newMsg = self.lineedit_message.text()
        if len(newMsg) > 8:
            self.write_error("Maximum message length is 8 characters!")
        else:
            try:
                usb = self.lineedit_port.text()
                self.ser = serial.Serial(usb, 115200)
                self.ser.write('send'.encode('utf-8'))
                time.sleep(0.01)
                self.sendPacket()
            except serial.SerialException:
                self.write_error("Invalid port added!")
    
    def sendPacket(self):
        printMsg = " Sent "
        canMsg = ""
        msg = self.lineedit_message.text()
        delimiter = ' '

        if self.check_extended.checkState():
            printMsg += "extended "
            canMsg += "1" + delimiter
        else:
            canMsg += "0" + delimiter

        if self.check_rtr.checkState():
            printMsg += "RTR "
            canMsg += "1" + delimiter
        else:
            canMsg += "0" + delimiter

        canMsg += self.lineedit_id.text() + delimiter + msg
        self.ser.write(canMsg.encode('utf-8'))
        self.ser.close()
        self.ser = None

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        printMsg += "packet with the id " + self.lineedit_id.text() + " and length " + str(len(self.lineedit_message.text())) + ":\n" + msg + "\n\n"
        self.sent_messages += current_time + printMsg
        self.scrolllabel.setText(self.sent_messages)



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