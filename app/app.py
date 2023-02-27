from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from monitorwidget import MonitorWidget
from sendwidget import SendWidget
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Monitor")
        self.main_layout = QStackedLayout()

        self.menu_init()
        self.monitor_view_widget = MonitorWidget(self)
        self.send_view_widget = SendWidget(self)

        self.main_layout.addWidget(self.menu_view_widget)
        self.main_layout.addWidget(self.monitor_view_widget)
        self.main_layout.addWidget(self.send_view_widget)
        
        widget = QWidget()
        widget.setLayout(self.main_layout)

        self.main_layout.setCurrentIndex(0)
        self.setCentralWidget(widget)

        self.setGeometry(0,0, 600, 800)

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

        # Initialization of the widget of the menu
        self.menu_view_widget = QWidget()
        self.menu_view_widget.setLayout(menu_layout)

    def monitor_pushed(self):
        self.main_layout.setCurrentIndex(1)

    def send_msg_pushed(self):
        self.main_layout.setCurrentIndex(2)

app = QApplication(sys.argv)

window = MainWindow()

app.exec()