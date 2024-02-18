import sys
from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def capture_packets(interface, count=10):
    print(f"Capturing {count} packets on interface {interface}...\n")
    sniff(iface=interface, prn=packet_callback, count=count)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python packet_capture.py <interface> [<count>]")
        sys.exit(1)

    interface = sys.argv[1]
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    capture_packets(interface, count)
