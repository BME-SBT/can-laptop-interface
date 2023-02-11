from PySide6.QtWidgets import QWidget, QApplication
import sys
import serial

app = QApplication(sys.argv)
window = QWidget()
window.show()

app.exec()

def main_menu():
    loop_go = True
    while  loop_go:
        in_num = input("Choose from the options below:\n\t1) Serial monitor\n\t2) Sending message\n\t3) Exit\n")
        match in_num:
            case "1":
                canBusMonitor()
            case "2":
                ser.write('send'.encode('utf-8'))
            case "3":
                loopGo = False
            case _:
                break
            

def canBusMonitor():
    ser.write('monitor'.encode('utf-8'))
    monitor_on = True
    while monitor_on:
        print(ser.readline().decode('utf-8'))
    


print("Serial monitor\n")

usb = input("Please give the USB port")
ser = serial.Serial(usb)
ser.baudrate = 115200

main_menu()

# ser.write('monitor'.encode('utf-8'))
# ser.flush()

# print(ser.readline().decode('utf-8'))

# ser.write('monitor'.encode('utf-8'))
# ser.flush()

# print(ser.readline().decode('utf-8'))

# ser.write('monitor'.encode('utf-8'))
# ser.flush()

# print(ser.readline().decode('utf-8'))

# ser.flush()

# ser.write('exit'.encode('utf-8'))

""" 
ser.write('monitor'.encode('utf-8'))

if ser.is_open:
    while input() != "exit":
        extended = ser.read()
        rtr = ser.read()
        id = ser.read(11)

        print("Recieved ")

        if extended:
            print("extended ")

        if rtr:
            print("RTR ")

        print("packet with id 0x" + id)

        if rtr:
            rtrlength = ser.read_until(" ")
            print(" and requested length " + rtrlength)
        else:
            length = ser.read_until(" ")
            print(" and length " + length + ser.readline + '\n')
        ser.write('exit'.encode('utf-8'))
else:
    print("Serial is not available on the requested port/")


 """


