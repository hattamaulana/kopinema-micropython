from networking import Network
from usocketio import client as socketio
from uwebsockets import client as websockets


def _connect_to_websockets(url):
    with websockets.connect("ws://"+ url) as sockets:
        import os

        uname = os.uname()
        name = '{sysname} {release} {version} {machine}'.format(
            sysname=uname.sysname,
            release=uname.release,
            version=uname.version,
            machine=uname.machine,
        )

        sockets.send(name)
        print("> {}".format(name))

        greeting = sockets.recv()
        print("< {}".format(greeting))


def _connect_to_socketio(url):
    with socketio.connect(url) as sio:
        @sio.on('message')
        def on_message(res):
            print(res)


net = Network()
if net.is_connected():
    # _connect_to_<:target>('192.168.1.4:5000')
    #_connect_to_websockets('ws://192.168.1.4:5000')
     _connect_to_socketio('http://192.168.1.4:5000/')