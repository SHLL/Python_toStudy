import socket
import struct
from ctypes import *

class IP(Structure):
    _fields_=[('ihl',c_uint8,4),
              ('version',c_uint8,4),
              ('tos',c_uint8),
              ('len',c_uint16),
              ('id',c_uint16),
              ('offset',c_uint16),
              ('ttl',c_uint8),
              ('proto',c_uint8)
              ('sum',c_uint16),
              ('src',c_uint32),
              ('dst',c_uint32)]

    def __new__(self,socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init(self,socket_buffer:None):
        self.src_addr=socket.inet_ntoa(struct.pack('<L',self.src))
        self.dst_addr=socket.inet_ntoa(struct.pack('<L',self.dst))

sniffer=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

ip_header=IP(sniffer.recv(20))
print(ip_header.src_adr,ip_header.dst_addr)

