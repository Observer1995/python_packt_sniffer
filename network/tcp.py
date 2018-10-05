from struct import unpack
class Tcp(object):
    def __init__(self,data):
        self.source_port,self.dest_port=unpack("!HH16x",data[:20])
        self.data=data[20:]
