import socket
IP = "192.168.86.28"

on = b"\x2a\x00\x00\x34\xb4\x3c\xf0\x84\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0d\x00\x00\x00\x00\x00\x00\x00\x00\x75\x00\x00\x00\xff\xff\xe8\x03\x00\x00"
off = b"\x2a\x00\x00\x34\xb4\x3c\xf0\x84\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x75\x00\x00\x00\x00\x00\xe8\x03\x00\x00"
port = 56700

code = """3100001402000000
d073d50013370000
0000000000000201
0000000000000000
66000000005555ff
ffffffac0d000000
00"""


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(on), (IP, port))
