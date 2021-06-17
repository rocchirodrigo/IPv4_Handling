# Ports
from srcnat import input_addresses
from ipaddress import IPv4Network

public_ip, private_ip = input_addresses()

public_pool = IPv4Network(public_ip)
private_pool = IPv4Network(private_ip)

prefix_div = public_pool.prefixlen - private_pool.prefixlen
divisor = int(private_pool.num_addresses / public_pool.num_addresses)

list_public = list()
list_private = list()
list_ports = list()

for ip_public in public_pool:
    list_public.append(ip_public)
for ip_private in private_pool:
    list_private.append(ip_private)

last_port = 65535
first_port = 1024
range_ports = last_port - first_port  # 64000~
subdivision = range_ports // divisor

# Calculating port range and ips
for num in range(divisor, 0, -1):
    first_term = last_port - (num * subdivision) + 1
    second_term = last_port - ((num - 1) * subdivision)
    list_ports.append(str(first_term) + "-" + str(second_term))

with open(file="spreadsheet-ips-ports.csv", mode='w') as outputFile:
    print("Portas", "Bloco Publico", "Bloco Privado", sep=',', file=outputFile)
    # Printing into the file
    for num in range(0, len(list_private)):
        print(list_ports[num // len(list_public)], sep='-', end=',', file=outputFile)
        print(list_public[(num % len(list_public))], list_private[num], sep=',', end='\n', file=outputFile)
