import struct
class Ipv4(object):
    def __init__(self,data):
        version_headerLenth=data[0]
        self.version=version_headerLenth>>4
        self.header_lenth=(version_headerLenth&15)*4
        self.tos,self.total_lenth,self.ttl,self.proto,source_addr,dest_addr=struct.unpack("!1xBH4xBB2x4s4s",data[:20])
        self.source_addr=self.ip_format(source_addr)
        self.dest_addr=self.ip_format(dest_addr)
        self.data=data[20:]
    def ip_format(self,addr):
        return ".".join(map(str,addr))









