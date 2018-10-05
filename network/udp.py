from struct import unpack

class Udp(object):
    def __init__(self,data):
        self.source_port,self.dest_port=unpack("HH4x",data[:8])
        self.data=data[8:]
