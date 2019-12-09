## use both tcpdump and nc together



ts isp connections

ping  checking the timeouts for
    local gw
    8.8.8.8

    tracert 8.8.8.8

    check router for its, ISP ip and gw
    try pinging those 2 see timeout
    try pinging with '-l'  allows your to set size (what about fragmenst)

hopefully the tracert will return an ASN number
lookit up  - give websites
Try connecting to looking glass server and back tracert
try a speed test - give websites
ping while running speed test (to local asn router)


report to your isp,  request a 'line test'

## wireshark

Lets capture some packets (stop after 30s ctrl-c)
`tcpdump -s 0 -i ens3 -w tcpdump.pcap ; ping -c 5 8.8.8.8`{{ execute }}

NOT WORKING tcpdump -s0 -c 1000 -nn -w - not port 22 | tshark -k -i -

`tshark -r tcpdump.pcap` {{ execute }}


Lets install wireshark for console (tshark)
`apt-get update -y`{{ execute }}
`apt-get install tshark -y`{{ excute }}
Press `enter` when you see the purple screen
and check its installed
`which tshark`{{ execute }}
/usr/bin/tshark


