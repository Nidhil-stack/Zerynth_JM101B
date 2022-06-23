###############################################################################
# Hello Zerynth
###############################################################################

# Welcome to the first and simplest Zerynth example.
# Let's just loop forever by printing something to the standard output,
# in this case, the USB serial port (open the device console to view the output)

# loop forever

from libs.jm101b import JM101B

fingerPrint = JM101B()

buffer = fingerPrint._sendCommand(0x01)

for i in buffer:
    print(i)



