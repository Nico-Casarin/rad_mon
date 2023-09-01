import serial
import time
import datetime

serial_port = '/dev/ttyUSB0'
baud_rate = '9600'
t_end = time.time() + 30 * (60*6)
ser = serial.Serial(serial_port, baud_rate, timeout=1)

try:
    while time.time() < t_end:
        line = ser.readline().decode('utf8').strip()
        timestamp = str(time.time())
        today = str(datetime.date.today())
        if (line):
            print(line)
            with open('%s.csv' % today, 'a') as pyfile:
                pyfile.write(line + ',' + timestamp + '\n')
    else:
        print("fine loop")
        ser.close()
except KeyboardInterrupt:
    print("stop")
    ser.close()
