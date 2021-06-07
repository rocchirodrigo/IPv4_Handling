/interface bridge
add name=loopback_cgnat

/ip address
add address=45.45.45.64/27 interface=loopback_cgnat

/ip route
add dst-address=45.45.45.64/32 type=blackhole
add dst-address=45.45.45.65/32 type=blackhole
add dst-address=45.45.45.66/32 type=blackhole
add dst-address=45.45.45.67/32 type=blackhole
add dst-address=45.45.45.68/32 type=blackhole
add dst-address=45.45.45.69/32 type=blackhole
add dst-address=45.45.45.70/32 type=blackhole
add dst-address=45.45.45.71/32 type=blackhole
add dst-address=45.45.45.72/32 type=blackhole
add dst-address=45.45.45.73/32 type=blackhole
add dst-address=45.45.45.74/32 type=blackhole
add dst-address=45.45.45.75/32 type=blackhole
add dst-address=45.45.45.76/32 type=blackhole
add dst-address=45.45.45.77/32 type=blackhole
add dst-address=45.45.45.78/32 type=blackhole
add dst-address=45.45.45.79/32 type=blackhole
add dst-address=45.45.45.80/32 type=blackhole
add dst-address=45.45.45.81/32 type=blackhole
add dst-address=45.45.45.82/32 type=blackhole
add dst-address=45.45.45.83/32 type=blackhole
add dst-address=45.45.45.84/32 type=blackhole
add dst-address=45.45.45.85/32 type=blackhole
add dst-address=45.45.45.86/32 type=blackhole
add dst-address=45.45.45.87/32 type=blackhole
add dst-address=45.45.45.88/32 type=blackhole
add dst-address=45.45.45.89/32 type=blackhole
add dst-address=45.45.45.90/32 type=blackhole
add dst-address=45.45.45.91/32 type=blackhole
add dst-address=45.45.45.92/32 type=blackhole
add dst-address=45.45.45.93/32 type=blackhole
add dst-address=45.45.45.94/32 type=blackhole
add dst-address=45.45.45.95/32 type=blackhole

/ip firewall nat
add action=src-nat chain=srcnat src-address=45.45.45.64 to-addresses=100.64.0.0/27
add action=src-nat chain=srcnat src-address=45.45.45.65 to-addresses=100.64.0.32/27
add action=src-nat chain=srcnat src-address=45.45.45.66 to-addresses=100.64.0.64/27
add action=src-nat chain=srcnat src-address=45.45.45.67 to-addresses=100.64.0.96/27
add action=src-nat chain=srcnat src-address=45.45.45.68 to-addresses=100.64.0.128/27
add action=src-nat chain=srcnat src-address=45.45.45.69 to-addresses=100.64.0.160/27
add action=src-nat chain=srcnat src-address=45.45.45.70 to-addresses=100.64.0.192/27
add action=src-nat chain=srcnat src-address=45.45.45.71 to-addresses=100.64.0.224/27
add action=src-nat chain=srcnat src-address=45.45.45.72 to-addresses=100.64.1.0/27
add action=src-nat chain=srcnat src-address=45.45.45.73 to-addresses=100.64.1.32/27
add action=src-nat chain=srcnat src-address=45.45.45.74 to-addresses=100.64.1.64/27
add action=src-nat chain=srcnat src-address=45.45.45.75 to-addresses=100.64.1.96/27
add action=src-nat chain=srcnat src-address=45.45.45.76 to-addresses=100.64.1.128/27
add action=src-nat chain=srcnat src-address=45.45.45.77 to-addresses=100.64.1.160/27
add action=src-nat chain=srcnat src-address=45.45.45.78 to-addresses=100.64.1.192/27
add action=src-nat chain=srcnat src-address=45.45.45.79 to-addresses=100.64.1.224/27
add action=src-nat chain=srcnat src-address=45.45.45.80 to-addresses=100.64.2.0/27
add action=src-nat chain=srcnat src-address=45.45.45.81 to-addresses=100.64.2.32/27
add action=src-nat chain=srcnat src-address=45.45.45.82 to-addresses=100.64.2.64/27
add action=src-nat chain=srcnat src-address=45.45.45.83 to-addresses=100.64.2.96/27
add action=src-nat chain=srcnat src-address=45.45.45.84 to-addresses=100.64.2.128/27
add action=src-nat chain=srcnat src-address=45.45.45.85 to-addresses=100.64.2.160/27
add action=src-nat chain=srcnat src-address=45.45.45.86 to-addresses=100.64.2.192/27
add action=src-nat chain=srcnat src-address=45.45.45.87 to-addresses=100.64.2.224/27
add action=src-nat chain=srcnat src-address=45.45.45.88 to-addresses=100.64.3.0/27
add action=src-nat chain=srcnat src-address=45.45.45.89 to-addresses=100.64.3.32/27
add action=src-nat chain=srcnat src-address=45.45.45.90 to-addresses=100.64.3.64/27
add action=src-nat chain=srcnat src-address=45.45.45.91 to-addresses=100.64.3.96/27
add action=src-nat chain=srcnat src-address=45.45.45.92 to-addresses=100.64.3.128/27
add action=src-nat chain=srcnat src-address=45.45.45.93 to-addresses=100.64.3.160/27
add action=src-nat chain=srcnat src-address=45.45.45.94 to-addresses=100.64.3.192/27
add action=src-nat chain=srcnat src-address=45.45.45.95 to-addresses=100.64.3.224/27
