import serial
import time
import datetime


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', dest='serial_port', type=str, default='/dev/ttyUSB0')
    parser.add_argument('-b', '--baud', dest='baud_rate', type=str, default=9600)
    parser.add_argument('-d', '--duration', dest='duration', type=int, default=0)

    args = parser.parse_args()

    if args.duration < 0:
        parser.error('Duration must be > 0')

    elif args.duration == 0:
        t_end = time.time() + 60

    elif args.duration > 0:
        t_end = time.time() + 60 * (60*args.duration)

    elif args.duration == 999:
        t_end = 2009305884

    ser = serial.Serial(args.serial_port, args.baud_rate, timeout=1)

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
