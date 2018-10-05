import struct
from binascii import hexlify
class Ethernet(object):
    def __init__(self,data):
       source_addr,dest_addr,self.prototype=struct.unpack('!6s6sH',data[:14])
       self.source_addr=self.mac_format(source_addr)
       self.dest_addr=self.mac_format(dest_addr)
       self.data=data[14:]
    def mac_format(self,addr):
        return ":".join(map("{:02x}".format,addr))





# THIS CODE IS FOR SELF INFORMATION#
#":".join("{:02x}".format(i) for i in b'\x00\x0c)M#\x14')
#'00:0c:29:4d:23:14'

#":".join(map("{:02X}".format,b'\x00\x0c)M#\x14'))
#'00:0C:29:4D:23:14'

#THIS TOW LINE OF CODES SHOWES HOW TO WORK WITH FUNCTIONS
#WHITCH REQUERS AN ITEARABLE PARAMET

#Note: i have to review on unicodeing and struct#
