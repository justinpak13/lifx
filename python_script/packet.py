import socket

class Packet:
    """A class used to create and send packets for the lifx lightstrip"""

    def __init__(self) -> None:
        with open("ip.txt", "r") as f:
            self.ip = f.read()

    def send_packet(self, code, port = 56700):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(code), (self.ip, port))

    def on(self):
        on_packet =  b"\x2a\x00\x00\x34\xb4\x3c\xf0\x84\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x75\x00\x00\x00\xff\xff\xe8\x03\x00\x00"
        self.send_packet(on_packet)

    def off(self):
        off_packet = b"\x2a\x00\x00\x34\xb4\x3c\xf0\x84\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x75\x00\x00\x00\x00\x00\xe8\x03\x00\x00"
        self.send_packet(off_packet)

if __name__ == "__main__":
    x = Packet()
    x.off()