from network import WLAN, STA_IF, AP_IF

class Network():

    def __init__(self):
        self.wlan = WLAN(STA_IF)
        self.ap = WLAN(AP_IF)

    def is_active(self):
        """Checking Active Module

        :return: boolean
        """
        print("Check WLAN...")

        if self.wlan.active() is False:
            print("WLAN Non Active...")
            self.wlan.active(True)

        else:
            print("WLAN Active...")
            return True

        return False

    def connect(self, essid, password):
        """Connect To Network

        Keyword Arguments
        :param essid: the name essid
        :param password: the password
        :return: boolean
        """
        if self.is_active():
            print("Connecting....")
            self.wlan.connect(essid, password)

            if self.wlan.isconnected():
                print("Connected...")
                return True

            else:
                print("Failed Connect...")

        else:
            self.is_active()

    def is_connected(self):
        """ Checking Connection

        :return: boolean
        """
        res = self.wlan.isconnected()

        if res :
            print("Network Connected")

        else:
            print("Network Disconnected")

        return res

    def status(self):
        """ Checking status connection

        :return: boolean
        """
        self.is_connected()
        print("Status : ", self.wlan.ifconfig())

    def activate_ap(self, essid):
        if self.ap.active():
            print('Access Point Active')
            self.ap.config(essid=essid, password='12345678')

        else:
            print('Access Point Non Active')
            self.ap.active(True)

    def deactivate_ap(self):
        self.ap.active(False)
        print('Deactivate Access Point')
