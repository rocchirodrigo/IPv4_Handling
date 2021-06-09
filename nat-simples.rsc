/interface bridge
add name=loopback_cgnat

/ip address
add address=131.221.142.96/30 interface=loopback_cgnat

/ip route
add dst-address=131.221.142.96/32 type=blackhole
add dst-address=131.221.142.97/32 type=blackhole
add dst-address=131.221.142.98/32 type=blackhole
add dst-address=131.221.142.99/32 type=blackhole

/ip firewall nat
add action=src-nat chain=srcnat src-address=100.75.0.0/24 to-addresses=131.221.142.96
add action=src-nat chain=srcnat src-address=100.75.1.0/24 to-addresses=131.221.142.97
add action=src-nat chain=srcnat src-address=100.75.2.0/24 to-addresses=131.221.142.98
add action=src-nat chain=srcnat src-address=100.75.3.0/24 to-addresses=131.221.142.99
