from send_packet import send_packet

on = b"\x2a\x00\x00\x34\xb4\x3c\xf0\x84\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x75\x00\x00\x00\xff\xff\xe8\x03\x00\x00"
off = b"\x2a\x00\x00\x34\xb4\x3c\xf0\x84\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x75\x00\x00\x00\x00\x00\xe8\x03\x00\x00"
green = b"\x31\x00\x00\x34\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x66\x00\x00\x00\x00\x55\x55\xff\xff\xff\xff\xac\x0d\x00\x04\x00\x00"

packet = []
# Header 

# binary field
origin = "00"
tagged = "1"
addressable = "1"
protocol = bin(1024 ^ 1<<12)[3:]

source = "0" * 32
target = "0" * 64
reserved = "0" * 48

#may need to add more zeroes 
ack_required = "0" * 4
res_required = "0" * 4

protocol_header = "0" * 64

# message type - choices listed in device messages. Example below is using SetColor
message_type = bin(102 ^ 1 << 8)[3:] + "0"*16
reserved_message = "0"*16

# payload 
payload_reserved = "0" * 8
# hue goes on a scale of 1-65535. for green we will use 21845

hue = bin(32767 ^ 1 << 16)[3:]
# all ones for the 16 bits for max saturation. TODO Add functionality to adjust with integers and percentages 
saturation_value = 70
saturation = bin(65535 * saturation_value // 100 ^ 1 << 16)[3:]

# same thing for brightness 1 - 65535
brightness_value = 50
brightness = bin(65535 * brightness_value // 100 ^ 1 << 16)[3:]

# Kelvin - need to look into 
kelvin = bin(3800 ^ 1 << 16)[3:] # + "0" * 8
kelvin = kelvin[len(kelvin) // 2:] + kelvin[:len(kelvin) // 2] + "0" * 8

# number of miliseconds over which to perform the transition - set to 1024 for now because it is easy 
transition = bin(1024 ^ 1<<16)[3:] + "0" * 8

total = origin + tagged + addressable + protocol + source + target + reserved + ack_required + res_required + protocol_header + message_type + reserved_message + hue + saturation + brightness + kelvin + transition

# size 
size = bin(len(total) // 8 + 3)[2:] + "0" * 16

total = size + total

final = [total[i * 16:(i + 1) * 16] for i in range((len(total) + 16 - 1) // 16 )]
for i in final:
    packet.append(i[:8])
    packet.append(i[8:])


# send_packet(bytes.fromhex(hex(int("".join(packet),base=2))[2:]))
# print(hue)
# print(int(hue, base =2 ))
send_packet(off)