import socket
import struct
from binascii import hexlify
from network import Ethernet
from network import Ipv4
from network import Arp
from network import Icmp
from network import Tcp
from network import Udp
import sys
#0x003 defines all packets
try:
    server=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.ntohs(0x003))
except:
    pass
    sys.exit()
def main():
    while True:
        pkt=server.recvfrom(2048)
        eth=Ethernet(pkt[0])
        print(':::::.... Ethernet Header ...::::')
        print('\n\tDest mac {} Source mac {}'.format(eth.source_addr,eth.dest_addr))  
        prototype=socket.ntohs(eth.prototype)

        pkt=eth.data
        if prototype==8:
            print("\t::::... IP Header ...::::")
            ipv4=Ipv4(pkt)
            pkt=ipv4.data
            print("\n\tsource_ip: {} \n\tdest ip {}".format(ipv4.source_addr,ipv4.dest_addr))
            print('\n\t\tipversion {}\n\t\theader_lenth {}\n\t\ttype_of_service {}\n\t\ttotal_lenth {}\n\t\tTTL {}\n\t\tprotocol {}'.format(ipv4.version,ipv4.header_lenth,ipv4.tos,ipv4.total_lenth,ipv4.ttl,ipv4.proto))
            
            # icmp header
            
            if ipv4.proto==1:
                icmp=Icmp(pkt)
                print("\t\t::::... Icmp Header ...::::")
                print("\n\t\t\ttype {} code {}".format(icmp.type,icmp.code))
                
            #tcp header
                
            elif ipv4.proto==6:
                print("\t\t::::.... TCP header ...::::")
                tcp=Tcp(pkt)
                print("\n\t\t\tsource port {} dest port {} ".format(tcp.source_port,tcp.dest_port))
                print("\t\tData",tcp.data)
                
            # udp header
            
            elif ipv4.proto==17:
                udp=Udp(pkt)
                print("\t\t::::.... Udp Header ...::::")
                print("\n\t\t\tsource port {} dest port {}".format(udp.source_port,udp.dest_port))
                print("\t\tData",udp.data)
                
        #arp header
                
        elif prototype==1544:
            print("\t::::... Arp Header ...::::")
            arp=Arp(pkt)
            print("\n\tsender_mac_address {} target mac address {}".format(arp.sha,arp.tha))
            print("\n\t\sender ip address {} target ip address {}".format(arp.spa,arp.tpa))
            print("\n\t\tHawrware_type {}\n\t\tPotoyocol type {}\n\t\tHardwarde_address_length {}\n\t\tProtocol_address_length {}".format(arp.hardware_type,arp.protocol_type,arp.hardware_address_length,arp.protocol_address_length))



if __name__=="__main__":
    main()



    
