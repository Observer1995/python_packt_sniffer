from struct import unpack
class Icmp(object):
    def __init__(self,data):
        self.type,self.code=unpack("!BB2x",data[:4])
        
