# Ports
from srcnat import input_addresses
from ipaddress import IPv4Network, ip_network


public_ip, private_ip = input_addresses()

public_pool = IPv4Network(public_ip)
private_pool = IPv4Network(private_ip)

list_public = list()
list_private = list()

for ip_public in public_pool:
    list_public.append(ip_public)
for ip_private in private_pool:
    list_private.append(ip_private)

last_port = 65535
first_port = 1024
range_ports = last_port - first_port
div = 32

for num in range(div, 0, -1):
    first_term = last_port + 1 - (num * (range_ports // div))
    second_term = first_term - 1 + (range_ports // div)
    # print(first_term, second_term, sep=" - ")

with open(file="spreadsheet-ips-ports.csv", mode='w') as outputFile:
    print("Portas", "Bloco Publico", "Bloco Privado", sep=',', file=outputFile)
    for num in range(div, 0, -1):
        first_term = last_port + 1 - (num * (range_ports // div))
        second_term = first_term - 1 + (range_ports // div)
        for looping in range(0, 15+1):
            print(first_term, second_term, sep='-', end=',', file=outputFile)
            print(list_public[looping % 16], list_private[looping], sep=',', end='\n', file=outputFile)
    for num2 in range(len(list_private)):
        pass
