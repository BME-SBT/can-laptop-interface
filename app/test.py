from struct import *
import serial
import time
ser = serial.serial_for_url('loop://', timeout=1)
# ser.write(b'\xAA')
# ser.write(b'\x66\x73\x00\x00')
# ser.write(b'\x08')
# ser.write(b'\x01\x00\x00\x00')
# ser.write(b'\x11\x22\x33\x44\x55\x66\x77\x88')
# ser.write(b'\xBB')
# start_of_frame = ser.read(1)

# if start_of_frame == (b'\xAA'): 
#     timestamp = unpack("<I", ser.read(4))
#     print(timestamp[0])
#     dlc = unpack("<B", ser.read(1))
#     print(dlc[0])
#     id = unpack("<I", ser.read(4))
#     print(id[0])
#     payload = []
#     payload = ser.read(int(dlc[0])).hex()
#     print(payload)
#     end_of_frame = ser.read(1)
#     print(end_of_frame.hex())
# else:
#     print("something went wrong ")

# if end_of_frame != None:
#     if end_of_frame == b'\xBB':
#         print(f'{timestamp[0]} {id[0]} {payload}')
#     else:
#         print("something went wrong")

# print(pack('<I', 123012))
# print(int("0XFF", base=16))

# time1 = time.time()

# time.sleep(1.5)
# timestamp = int((time.time() - time1) * 1000)
# print(timestamp)
# print(pack('<I', timestamp))
