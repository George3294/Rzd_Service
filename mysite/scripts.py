import serial
import pigpio

serial_port = "COM5"
serial_baud = 9600
files = "arduino.csv"
ser = serial.Serial(serial_port, serial_baud)
while True:
    line = ser.readline()
    line = line.decode('utf-8')
    print(line)
    with open(files, "w", encoding="utf-8") as file:
        file.write(line)
