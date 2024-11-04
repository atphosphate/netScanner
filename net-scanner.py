import scapy.all as scapy
import optparse

#1)arp_request
#2)broadcast
#3)response

def get_info():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-r","--range", dest="ip_adress", help="Range of local IP addresses")
    (user_input, arguments) = parse_object.parse_args()
    return user_input

def scan(ip_range):
    arp_request_packet = scapy.ARP(pdst=ip_range)
    #scapy.ls(scapy.ARP())
    arp_broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combined_packet = arp_broadcast_packet/arp_request_packet
    return scapy.srp(combined_packet, timeout=1)


(answered_list, unanswered_list) = scan(get_info().ip_adress)
answered_list.summary()
