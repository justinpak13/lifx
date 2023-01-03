def _concatenate_bits(original_bits, new_bits):
    "Adds the new bits onto the end of the original bits. We ignore the first 3 of the new bits just cause that is what we use for placeholders"

    result = original_bits
    for i in bin(new_bits)[3:]:
        result = result << 1
        result = result | int(i)

    return result


def header():
    # binary field 
    holder = 1

    # origin 
    holder = _concatenate_bits(holder, 0b100)
    
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

    #ack_required 
    holder = _concatenate_bits(holder, 0b1 << 4)

    #res_required 
    holder = _concatenate_bits(holder, 0b1 << 4)

    # protocol header 
    holder = _concatenate_bits(holder, 0b1 << 64)

    # message type - choices listed in device messages. Example below is using SetColor
    holder = _concatenate_bits(holder, 102 ^ 1 << 8)
    holder = _concatenate_bits(holder, 0b1 << 16)
    
    # reserved message 
    holder = _concatenate_bits(holder, 0b1 << 16)

    return holder

def payload(hue = 32767, saturation = 100, brightness = 100, kelvin = 3800, transition = 1024):

    # payload reserved 
    holder = 1 

    holder = _concatenate_bits(holder,0b1 << 8)

    # hue 

    # saturation

    # brightness 

    # kelvin 

    # transition 

def finalize_packet(header, payload):
    pass 

if __name__ == "__main__":
    pass 