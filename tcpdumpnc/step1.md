# Overview of tcpdump

tip!
try not to use the 'auto execute', but actually type the commands in, you'll retain the information for longer.   

hint:
ctrl-L refreshes the terminal, just like `clear`
you may need to run these with sudo needing on your setup

warning:
as usual, don't try on production systems unless you know what you're doing!

Lets check if you have tcpdump

`which tcpdump`{{ execute }}

/usr/sbin/tcpdump

And install  if not

`sudo apt install -y tcpdump`

Any time you need to break out of a cmd use ctrl-c, or click here:
`echo stop`{{ execute }}

### simple commands

 `tcpdump -h`{{execute}}

and lets see what interfaces are available on this machine

`tcpdump -D`{{ execute }}

since ens3 is our main interface, we'll be using the option `-i ens3`  or `-i 1`

lets capture the next 5 packets transvering ens3

`tcpdump -i ens3 -c 5`{{ execute }}

I don't want to see the dns entries

`tcpdump -i ens3 -c 5 -n`{{ execute }}

to really shorten up the output try `-q` minimum,  `-t` no time stamps

`tcpdump -i ens3 -c 5 -nqt`{{ execute }}


### Lets try some basic filters

Look for DNS traffic using UDP on port 53
`tcpdump -i ens3 udp -c 3 -nt -u port 53` {{ execute }}

Not getting any output? Try a ping in another terminal (remember that the system will cache the result so you'll need to ping another site to get a new dns request)
`ping www.bbc.com -c 4`{{ execute T2}}


Lets look for incoming traffic from host02
`tcpdump -i ens3  -c 3 -v -nt src host host02`{{ execute }}

And lets send a ping from host02
`ping host01 -c 4`{{ execute host02 }}

the more complex ones you should inc in "", so lets look for incoming traffic of type ssh.
`tcpdump -i ens3  -c 3 -v -nt "src host host02 || src port 22"`{{ execute }}

lets take a look at what sending in those ssh packets.

WIP COMPLETE LAST STATEMENT

You can always check the offical man page for more details:
(www.tcpdump.org)[https://www.tcpdump.org/manpages/tcpdump.1.html]

#### basic commands

WIP: BUT THE FOLLOWING ABOVE
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
  10. logical operaters AND = &&, OR = ||, NOT = !  