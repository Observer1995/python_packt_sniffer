from struct import unpack
import socket
class Arp(object):
    def __init__(self,data):
        self.hardware_type,self.protocol_type,self.hardware_address_length,self.protocol_address_length,sha,spa,tha,tpa=unpack("!HHBB2x6s4s6s4s",data[:28])
        self.sha=self.mac_format(sha)
        self.spa=self.ip_format(spa)
        self.tha=self.mac_format(tha)
        self.tpa=self.ip_format(tpa)
    def mac_format(self,addr):
        return ":".join(map("{:02x}".format,addr))
    def ip_format(self,addr):
        return ".".join(map(str,addr))
        
