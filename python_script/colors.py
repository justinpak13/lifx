import socket


def _concatenate_bits(original_bits, new_bits):
    "Adds the new bits onto the end of the original bits. We ignore the first 3 of the new bits just cause that is what we use for placeholders"

    result = original_bits
    for i in bin(new_bits)[3:]:
        result = result << 1
        result = result | int(i)

    return result


def get_100(value):
    """This function is used to return the equivalent 16 bit representation of a scale of 0 - 100 
    used for both brightness, and saturation"""
    if value < 0:
        value = 0
    if value > 100:
        value = 100

    return socket.ntohs(65535 * value // 100) ^ 1 << 16


def get_hue(value):
    """Takes in a value between 1-360 to represent a hue in hsl form and converts it to the correct binary and returning it with little endian"""
    if value <= 1:
        value = 1
    if value > 360:
        value = 360

    return socket.ntohs(65535 * value // 360) ^ 1 << 16


def header():
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


def payload(hue=120, saturation=100, brightness=100, kelvin=3800, transition=1024):

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


def finalize_packet(header, payload):
    holder = 1
    holder = _concatenate_bits(holder, header)
    holder = _concatenate_bits(holder, payload)

    holder = _concatenate_bits(socket.ntohs(len(hex(holder)[3:]) // 2 + 2), holder)

    return holder


if __name__ == "__main__":
    from send_packet import send_packet

    send_packet(
        (
            bytes.fromhex(
                hex(
                    finalize_packet(
                        header(), payload(hue=300, saturation=0, brightness=100)
                    )
                )[2:]
            )
        )
    )

