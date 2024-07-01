from scapy.all import *

def analyze_packet(packet):
    """
    Analyze a captured packet.
    
    Args:
        packet (scapy.packet.Packet): The packet to analyze.
    """
    if IP in packet:
        ip_layer = packet[IP]
        print(f"[+] New Packet: {ip_layer.src} -> {ip_layer.dst}")
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"    [TCP] {tcp_layer.sport} -> {tcp_layer.dport}")
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"    [UDP] {udp_layer.sport} -> {udp_layer.dport}")
    else:
        print("[!] Non-IP Packet")

def save_packet(packet, filename):
    """
    Save packet information to a file.
    
    Args:
        packet (scapy.packet.Packet): The packet to save.
        filename (str): The file to save the packet information.
    """
    with open(filename, 'a') as f:
        f.write(str(packet) + '\n')
