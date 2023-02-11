from PySide6.QtWidgets import QVBoxLayout, QApplication, QMainWindow, QWidget, QPushButton, QStackedLayout, QLabel, QLineEdit
import sys
import serial

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
        self.btn_back = QPushButton("Back")
        self.btn_back.clicked.connect(self.back_pushed)

        monitor_layout.addWidget(label_monitor)
        monitor_layout.addWidget(label_basic_information)
        monitor_layout.addWidget(label_port)
        monitor_layout.addWidget(self.lineedit_port)
        monitor_layout.addWidget(btn_port)
        monitor_layout.addWidget(self.label_received_messages)
        monitor_layout.addWidget(self.btn_back)

        #setup the widget of the monitor view
        self.monitor_view_widget = QWidget()
        self.monitor_view_widget.setLayout(monitor_layout)

    def port_number_button(self):
        usb = self.lineedit_port.text()
        self.ser = serial.Serial(usb)
        self.ser.baudrate = 115200
        self.ser.write('monitor'.encode('utf-8'))
        
    
    async def monitor_loop(self):
        while self.monitor_running == True:
            if self.ser.bytesize > 0:
                self.received_messages += self.ser.readline().decode('utf-8')
                self.label_received_messages.setText(self.received_messages)
                print(self.received_messages)

    
    def monitor_pushed(self):
        self.main_layout.setCurrentIndex(1)
        
    
    def send_msg_pushed(self):
        print()
    
    def back_pushed(self):
        self.main_layout.setCurrentIndex(0)
        self.ser.write('exit'.encode('utf-8'))
        self.monitor_running = False


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()