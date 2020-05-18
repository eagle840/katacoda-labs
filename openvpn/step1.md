Lets first update the server

`sudo apt update`     

`sudo apt upgrade`

install the openvpn package

`sudo apt install openvpn`

we'll be using a github article and script to for a better than default setup.   

https://github.com/angristan/openvpn-install

You can look through the aticle and customize the script as needed.   

`wget https://raw.githubusercontent.com/angristan/openvpn-install/master/openvpn-install.sh`

`chmod +x openvpn-install.sh`

#`sudo ./openvpn-install.sh`   
but we'll use the auto install feature   
`AUTO_INSTALL=y ./openvpn-install.sh`
Once complete you should have a new client.ovpn  file.   

If you get: 'a TUN is not available',   
`cd /dev`
`mkdir net`
`mknod net/tun c 10 200`
`cdmod 0666 /dev/net/tun`

