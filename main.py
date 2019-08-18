from networking import Network
from websocket import client
import os


net = Network()

connection = net.is_connected()


def tesSocketIo(url):
    with client.connect(url) as socketio:
        uname = os.uname()
        name = '{sysname} {release} {version} {machine}'.format(
            sysname=uname.sysname,
            release=uname.release,
            version=uname.version,
            machine=uname.machine,
        )

        socketio.send(name)
        print("> {}".format(name))

        while True:
            greeting = socketio.recv()
            print("< {}".format(greeting))