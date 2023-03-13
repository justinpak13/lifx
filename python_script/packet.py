import socket

def get_100(value: int) -> int:
    """This function is used to return the equivalent 16 bit representation of a scale of 0 - 100 
    used for both brightness, and saturation"""
    if value < 0:
        value = 0
    if value > 100:
        value = 100

    return socket.ntohs(65535 * value // 100) ^ 1 << 16


def get_hue(value: int) -> int:
    """Takes in a value between 1-360 to represent a hue in hsl form and converts it to the correct binary and returning it with little endian"""
    if value <= 1:
        value = 1
    if value > 360:
        value = 360

    return socket.ntohs(65535 * value // 360) ^ 1 << 16


def finalize_packet(header: int, payload: int) -> int:
    holder = 1
    holder = _concatenate_bits(holder, header)
    holder = _concatenate_bits(holder, payload)

    holder = _concatenate_bits(socket.ntohs(len(hex(holder)[3:]) // 2 + 2), holder)

    return holder


def _concatenate_bits(original_bits: int, new_bits: int) -> int:
    "Adds the new bits onto the end of the original bits. We ignore the first 3 of the new bits just cause that is what we use for placeholders"

    result = original_bits
    for i in bin(new_bits)[3:]:
        result = result << 1
        result = result | int(i)

    return result


def payload(hue: int =120, saturation: int = 100, brightness:int=100, kelvin:int=3800, transition:int=1024) -> int:

    # payload reserved
    holder = 1

    holder = _concatenate_bits(holder, 0b1 << 8)

    # hue
    holder = _concatenate_bits(holder, get_hue(hue))

    # saturation
    holder = _concatenate_bits(holder, get_100(saturation))

    # brightness
    holder = _concatenate_bits(holder, get_100(brightness))

    # kelvin
    # need to look into more- this also needs to be in little endian
    holder = _concatenate_bits(holder, socket.ntohs(3500) ^ 1 << 16)

    # # transition
    holder = _concatenate_bits(holder, 1024 ^ 1 << 24)
    holder = _concatenate_bits(holder, 0b1 << 8)

    return holder


def header() -> int:
    # binary field
    holder = 1

    # origin
    holder = _concatenate_bits(holder, 0b10000000000)

    # tagged
    holder = _concatenate_bits(holder, 0b11)

    # addressable
    holder = _concatenate_bits(holder, 0b11)

    # protocol
    holder = _concatenate_bits(holder, 0b101 << 10)

    # source
    holder = _concatenate_bits(holder, 0b1 << 32)

    # target
    holder = _concatenate_bits(holder, 0b1 << 64)

    # reserved
    holder = _concatenate_bits(holder, 0b1 << 48)

    # ack_required
    holder = _concatenate_bits(holder, 0b1 << 4)

    # res_required
    holder = _concatenate_bits(holder, 0b1 << 4)

    # protocol header
    holder = _concatenate_bits(holder, 0b1 << 64)

    # message type - choices listed in device messages. Example below is using SetColor
    holder = _concatenate_bits(holder, 102 ^ 1 << 8)
    holder = _concatenate_bits(holder, 0b1 << 16)

    # reserved message
    holder = _concatenate_bits(holder, 0b1 << 8)

    return holder


class Packet:
    """A class used to create and send packets for the lifx lightstrip"""

    def __init__(self, ip) -> None:
        self.ip = ip
        self.hue = 300 
        self.saturation = 0 
        self.brightness = 100
        self.status = 0

    def __repr__(self):
        return (f"""
        Status: {self.status}  
        Hue: {self.hue}
        Saturation: {self.saturation}
        Brightness: {self.brightness}
        """)

    def send_packet(self, code, port=56700):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(code), (self.ip, port))

    def on(self):
        on_packet = b"\x2a\x00\x00\x34\xb4\x3c\xf0\x84\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x75\x00\x00\x00\xff\xff\xe8\x03\x00\x00"
        self.send_packet(on_packet)
        self.status = 1

    def off(self):
        off_packet = b"\x2a\x00\x00\x34\xb4\x3c\xf0\x84\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x75\x00\x00\x00\x00\x00\xe8\x03\x00\x00"
        self.send_packet(off_packet)
        self.status = 0 

    def change_color(self, hue=300, saturation=0, brightness=100):
        self.send_packet(
            bytes.fromhex(
                hex(finalize_packet(header(), payload(hue, saturation, brightness)))[2:]
            )
        )


if __name__ == "__main__":
    x = Packet()
    print(x)