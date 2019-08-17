# This file is executed on every boot (including wake-boot from deepsleep)
import gc
#import esp
#import uos, machine
#import webrepl
from networking import Network

gc.collect()
#esp.osdebug(None)
#uos.dupterm(None, 1) # disable REPL on UART(0)
#webrepl.start()

# Network Connection Setup
net = Network()

# Connect to Network
net.connect('Wifi kos', 'LANTA15ATU')