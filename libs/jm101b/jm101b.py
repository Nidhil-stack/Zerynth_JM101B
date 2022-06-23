from bsp import board

import serial

class JM101B(serial):
    def __init__(self, port = SERIAL1, baudrate = 57600):
        serial.serial.__init__(self, port, 57600, STOPBIT_2, PARITY_NONE, BITSIZE_8, 0, 0, MODE_RS485_HALF_DUPLEX)
        sleep(200)


    def _getSerialNumber(self):
        print("Not implemented yet")

    def _commandStream(self, stream):
        print("Not implemented yet")

    def _sendCommand(self, command):
        buffer = bytearray([0xEF, 0x01, 0xFF, 0xFF, 0xFF, 0xFF, 0x01, 0x00, 0x04, 0x34, 0x00, 0x39])
        return self.write(buffer)
