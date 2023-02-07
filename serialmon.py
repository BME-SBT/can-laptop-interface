import serial

print("Serial monitor\n")

usb = input("Please give the USB port")
ser = serial.Serial(usb)
ser.baudrate = 115200

ser.write('monitor'.encode('utf-8'))
ser.flush()

print(ser.readline().decode('utf-8'))

ser.write('monitor'.encode('utf-8'))
ser.flush()

print(ser.readline().decode('utf-8'))

ser.write('monitor'.encode('utf-8'))
ser.flush()

print(ser.readline().decode('utf-8'))

ser.flush()

ser.write('exit'.encode('utf-8'))

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


