from PySide6.QtWidgets import *
#from PySide6 import QtCore, QtGui
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
import serial
from datetime import datetime

# class for scrollable label
class ScrollLabel(QScrollArea):
 
    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
 
        # making widget resizable
        self.setWidgetResizable(True)
 
        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)
 
        # vertical box layout
        lay = QVBoxLayout(content)
 
        # creating label
        self.label = QLabel(content)
 
        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
 
        # making label multi-line
        self.label.setWordWrap(True)
 
        # adding label to the layout
        lay.addWidget(self.label)
 
    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Monitor")
        self.main_layout = QStackedLayout()

        self.menu_init()
        self.monitor_init()
        #self.send_msg_init()

        self.main_layout.addWidget(self.menu_view_widget)
        self.main_layout.addWidget(self.monitor_view_widget)
        
        widget = QWidget()
        widget.setLayout(self.main_layout)

        self.main_layout.setCurrentIndex(0)
        self.setCentralWidget(widget)

        self.show()
    
    def menu_init(self):
        #setup the menu view
        menu_layout = QVBoxLayout()

        #define menu buttons
        btn_monitor = QPushButton("Serial Monitor")
        btn_monitor.clicked.connect(self.monitor_pushed)

        btn_send_msg = QPushButton("Send Message")
        btn_send_msg.clicked.connect(self.send_msg_pushed)

        menu_layout.addWidget(btn_monitor)
        menu_layout.addWidget(btn_send_msg)

        #widget of the menu
        self.menu_view_widget = QWidget()
        self.menu_view_widget.setLayout(menu_layout)

    def monitor_init(self):
        #setup the monitor view
        monitor_layout = QVBoxLayout()

        #setup labels and buttons
        label_monitor = QLabel("Monitor view")
        label_basic_information = QLabel("Basic description in the future")
        label_port = QLabel("Port: ")
        self.lineedit_port = QLineEdit()
        btn_port = QPushButton("Show port")
        btn_port.clicked.connect(self.port_number_button)

        self.received_messages = "Recieved messages:\n\n"
        self.label_received_messages = QLabel(self.received_messages)
        self.label_received_messages.setWordWrap(True)
        self.label_received_messages.setMinimumHeight(600)
        self.label_received_messages.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        
        self.scrolllabel = ScrollLabel(self)
        self.monitor_running = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.monitoring)
        self.timer.start(1000)

        self.btn_back = QPushButton("Back")
        self.btn_back.clicked.connect(self.back_pushed)

        monitor_layout.addWidget(label_monitor)
        monitor_layout.addWidget(label_basic_information)
        monitor_layout.addWidget(label_port)
        monitor_layout.addWidget(self.lineedit_port)
        monitor_layout.addWidget(btn_port)
        monitor_layout.addWidget(self.scrolllabel)
        monitor_layout.addWidget(self.btn_back)

        #setup the widget of the monitor view
        self.monitor_view_widget = QWidget()
        self.monitor_view_widget.setLayout(monitor_layout)

    def port_number_button(self):
        usb = self.lineedit_port.text()
        self.ser = serial.Serial(usb)
        self.ser.baudrate = 115200
        self.ser.write('monitor'.encode('utf-8'))
        self.monitor_running = True
        

    def monitor_pushed(self):
        self.main_layout.setCurrentIndex(1)
        
    def monitoring(self):
        if(self.monitor_running == True):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            new_message = current_time + ' ' + self.ser.readline().decode('utf-8') + '\n'
            self.received_messages += new_message
            self.scrolllabel.setText(self.received_messages)

    def send_msg_pushed(self):
        print()
    
    def back_pushed(self):
        self.main_layout.setCurrentIndex(0)
        self.received_messages = "Recieved messages:\n\n"
        self.scrolllabel.setText(self.received_messages)
        self.ser.write('exit'.encode('utf-8'))
        self.monitor_running = False

    def UiComponents(self): 
        # creating scroll label
        label = ScrollLabel(self)
 
        # setting text to the label
        label.setText(self.received_messages)
 
        # setting geometry
        label.setGeometry(100, 100, 200, 80)


app = QApplication(sys.argv)

window = MainWindow()

app.exec()