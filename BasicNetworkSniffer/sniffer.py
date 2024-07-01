from scapy.all import sniff

def capture_packets(interface, packet_count, callback):
    """
    Capture network packets on a specified interface.
    
    Args:
        interface (str): Network interface to capture packets on.
        packet_count (int): Number of packets to capture.
        callback (function): Function to call for each captured packet.
    """
    sniff(iface=interface, count=packet_count, prn=callback, store=0)
