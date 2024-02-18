# Packet-Sniffer
This is a simple Python script that uses the Scapy library to capture and analyze network packets on a specified interface.

To run this script, you'll need to have Scapy installed. You can install it via pip:
```bash
pip install scapy
```
How to use the script:
```bash
python packet_capture.py <interface> [<count>]
```
Replace <interface> with the name of the network interface you want to capture packets from (e.g., "eth0" for Ethernet, "wlan0" for Wi-Fi).
You can optionally specify the number of packets to capture (default is 10). The script will start capturing packets and print out basic information about each packet as it's captured. You can customize the packet_callback function to your liking/needs to perform more advanced analysis or processing on the captured packets as needed.
