import serial

# XBee setting
serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600)

s.write("+++".encode())
char = s.read(2)
print("Enter AT mode.")
print(char.decode())

s.write("ATMY 0x123\r\n".encode())
char = s.read(3)
print("Set MY 0x123.")
print(char.decode())

s.write("ATDL 0x234\r\n".encode())
char = s.read(3)
print("Set DL 0x234.")
print(char.decode())

s.write("ATWR\r\n".encode())
char = s.read(3)
print("Write config.")
print(char.decode())

s.write("ATMY\r\n".encode())
char = s.read(4)
print("MY :")
print(char.decode())

s.write("ATDL\r\n".encode())
char = s.read(4)
print("DL : ")
print(char.decode())

s.write("ATCN\r\n".encode())
char = s.read(3)
print("Exit AT mode.")
print(char.decode())

# send to remote
s.write("abcd".encode())
line = s.read(5)
print('Get:', line.decode())

s.close()