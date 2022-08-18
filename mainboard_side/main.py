from lib.pycubed import cubesat
import time

""" add to pycubed.py __init__ function """
"""
# Initialize camera
try:
    self.cs_cam = digitalio.DigitalInOut(board.CS_CAM)
    self.cs_cam.direction = digitalio.Direction.OUTPUT
    self.cs_cam.value = True
except Exception as e:
    print('[ERROR][Camera]', e)
"""

""" spi: receive data from secondary """
spi = cubesat.spi
cs_cam = cubesat.cs_cam


while True:
    while not spi.try_lock():
        pass

    try:
        spi.configure(baudrate=19200, phase=0, polarity=0)
        cs_cam.value = False
        result = bytearray(10)
        spi.readinto(result)
        cs_cam.value = True
        print(result)
    finally:
        spi.unlock()
        time.sleep(1)


""" spi: send data to secondary
while not spi.try_lock():
    pass

try:
    spi.configure(baudrate=19200, phase=0, polarity=0)
    cs_cam.value = False
    spi.write(bytearray("Hello World\n"))
    cs_cam.value = True
finally:
    spi.unlock()
    time.sleep(5)
"""

