import socket

ip_address = input("Target IP : ")
mac_addresses = input("MAC Addresses : ").split(" ")

single_magic_packet = "FF"

data = ""

for i in range(6):
    data += single_magic_packet + " "

data += ' '.join(mac_addresses)

print(ip_address)
print(' '.join(mac_addresses))
print(data)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(data.encode("utf-8"), (ip_address, 9))