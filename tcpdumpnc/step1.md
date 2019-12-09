# Overview of tcpdump

tip!
try not to use the 'auto execute', but actually type the commands in, you'll retain the information for longer.

hint:
ctrl-L refreshes the terminal
you may need to run these with sudo needing on your setup

Lets check if you have tcpdump

`$ which tcpdump`
/usr/sbin/tcpdump

And install  if not
`sudo apt install -y tcpdump`

Any time you need to break out of a cmd, click here:
`echo stop`{{ execute }}

### simple commands

 `tcpdump -h`{{execute}}

and lets see what interfaces are available on this machine

`tcpdump -D`{{ execute }}

since ens3 is our main interface, we'll be using the option `-i ens3`  or -i 1

lets capture the next 5 packets transvering ens3

`tcpdump -i ens3 -c 5`{{ execute }}

I don't want to see the dns entries

`tcpdump -i ens3 -c 5 -n`{{ execute }}

to really shorten up the output try `-q` minimum,  `-t` no time stamps


### Lets try some basic filters
the more complex ones you should inc in ""

`tcpdump -i ens3 -c 20 -nt port 22`{{ execute }}

You can always check the offical man page for more details:
`https://www.tcpdump.org/manpages/tcpdump.1.html`

### basic commands

```
 tcpdump    
    -D  # list the available interfaces
    -i <int name>  or any
    -c<#>  number of packets to capture
    -n      do not look up dns
    -s<#>   capture this much of a packet   max: 65335 just header: 64   0: max
    -S      do not show seq numbers, first capture shows complete seq num, rest show relipahte
    -e      show macs\' 
    -XX     more pkt detail   -A    more compact   -v -vv -vvv  -K ignore tcpdump collection errors
    -q      minimum output
    -t      no time,  -tt -ttttt max time info
    -w <filename.pcap>   # capture into a file, -v to show \ of pkts capture while in progress
    -r <file>   read file
    ```

### filters

  1. host \<ip> or <dns name>
  2. net <cidr addr eg 10.0.0.0/24>
  3. [srx | dst] [host | net | other?]
  4. port <ip>  
  5. and | or   complex filters should be in  "" or ''
  6. tcp        protocol
  7. ether host <mac>    to filter my mac
  8. tcp udp      ipv6
  9. you can also filer on flags (see man)