import socket

def send_packet(code, IP = "192.168.86.28", port = 56700):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes(code), (IP, port))

