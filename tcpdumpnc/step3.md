### wireshark

Lets install wireshark for console (tshark)
`apt-get update -y`{{ execute }}
`apt-get install tshark -y`{{ execute }}
Enter yes when prompted.
`which tshark`{{ execute }}
/usr/bin/tshark

Lets capture some packets (stop after 30s ctrl-c)
`tcpdump -s 0 -i ens3 -w tcpdump.pcap {{ execute }}


`tshark -r tcpdump.pcap`{{ execute }}

