from serial import Serial
from time import sleep

if __name__ == "__main__":

    serial_port = "COM9"
    baudrate = 38400

    roboclaw = Serial(serial_port, baudrate, timeout=1)
    
    while True:
    
        roboclaw.write(bytes([94]))
        sleep(2)
        roboclaw.write(bytes([64]))
        sleep(2)
        roboclaw.write(bytes([32]))
        sleep(2)
        roboclaw.write(bytes([64]))
        sleep(2)
        
        roboclaw.write(bytes([223]))
        sleep(2)
        roboclaw.write(bytes([192]))
        sleep(2)
        roboclaw.write(bytes([160]))
        sleep(2)
        roboclaw.write(bytes([192]))
        sleep(2)
