import socket
import binascii

def wol():
    ip_address = input("Target IP : ")
    mac_addresses = input("MAC Addresses : ").split(" ")
    magic_packet = binascii.unhexlify("FF") * 6
    data = magic_packet

    for mac in mac_addresses:
        data = data + binascii.unhexlify(mac.replace('.', ''))

    print(ip_address)
    print(data)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(data, (ip_address, 9))

wol()