# This file is executed on every boot (including wake-boot from deepsleep)
import gc
import os
#import esp
#import uos, machine
#import webrepl

from usdcard import SDCard
from networking import Network
from machine import SPI, Pin

gc.collect()
#esp.osdebug(None)
#uos.dupterm(None, 1) # disable REPL on UART(0)
#webrepl.start()

sdcard = SDCard(SPI(1), Pin(15))
os.mount(sdcard, '/lib')

print(os.listdir())

# Network Connection Setup
# Connect to Network
net = Network()
net.connect('coffee', '11111111')