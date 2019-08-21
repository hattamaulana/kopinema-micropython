import socket
from time import sleep


class Server:
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        self._socket.bind(socket.getaddrinfo('0.0.0.0', 80)[0][-1])
        self._socket.listen(5)

    def listen(self, net):
        while True:
            con, addr = self._socket.accept()
            req = con.recv(1024)
            req = str(req)

            try:
                req = req.split('HTTP')[0].split('?')[1]
                req = req.split('&')
                sid = req[0].split('=')[1].replace('+', ' ').strip()
                pwd = req[1].split('=')[1].strip()

                net.connect(sid, pwd)
                sleep(2)

                if net.is_connected():
                    status = "success"
                    con.send('{"status": "' + status + '"}')
                    con.close()

                else:
                    status = 'error'
                    con.send('{"status": "' + status + '"}')
                    con.close()

            except:
                print('Parse Error')
                break
