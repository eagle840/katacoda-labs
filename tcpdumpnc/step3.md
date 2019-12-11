### wireshark

Lets install wireshark for console (tshark)
`apt-get update -y`{{ execute }}

WIP: get a purple prompt!
`apt-get install tshark -y`{{ execute }}
Enter yes when prompted.


`which tshark`{{ execute }}
/usr/bin/tshark

Lets capture some packets (stop after 30s ctrl-c)

`tcpdump -i ens3 -c 5 -w tcpdump.pcap`{{ execute }}

And take a look through tshark
`tshark -r tcpdump.pcap`{{ execute }}

WIP Remove finiah json

