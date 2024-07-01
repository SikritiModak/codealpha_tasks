import argparse
from sniffer import capture_packets
from packet_analyzer import analyze_packet, save_packet

def main():
    parser = argparse.ArgumentParser(description="Basic Network Sniffer")
    parser.add_argument("-i", "--interface", required=True, help="Network interface to capture packets on")
    parser.add_argument("-c", "--count", type=int, default=10, help="Number of packets to capture")
    parser.add_argument("-o", "--output", help="Output file to save packet information")

    args = parser.parse_args()

    def packet_callback(packet):
        analyze_packet(packet)
        if args.output:
            save_packet(packet, args.output)

    capture_packets(args.interface, args.count, packet_callback)

if __name__ == "__main__":
    main()
