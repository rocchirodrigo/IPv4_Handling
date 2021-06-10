# Generates separate .csv files for IP Control spreadsheet.
from ipaddress import IPv4Network, ip_network

isp_name = "MY-ISP"
network_radio = IPv4Network('192.168.1.0/24')
network_enlace = IPv4Network('10.0.0.0/24')
network_pppoe = IPv4Network('100.64.0.0/23')
network_public_ip = IPv4Network('22.22.22.0/29')

subnet_radio = list(ip_network(str(network_radio.with_prefixlen)).subnets(new_prefix=26))
subnet_enlace = list(ip_network(str(network_enlace.with_prefixlen)).subnets(new_prefix=26))
subnet_pppoe = list(ip_network(str(network_pppoe.with_prefixlen)).subnets(new_prefix=24))
subnet_public_ip = list(ip_network(str(network_public_ip.with_prefixlen)).subnets(new_prefix=31))

with open("ip-radios.csv", mode='w') as outputfile:
# Radios
    print("{0} - Rádios".format(isp_name), file=outputfile)
    print("Faixa de IP:, {0}".format(network_radio), file=outputfile)
    print(file=outputfile)
    print("IP,nome,login,senha," * 4, file=outputfile)
    for (ip1, ip2, ip3, ip4) in zip(subnet_radio[0], subnet_radio[1], subnet_radio[2], subnet_radio[3]):
        print("{0},,,, {1},,,, {2},,,, {3}".format(ip1, ip2, ip3, ip4), file=outputfile)

with open("ip-enlace.csv", mode='w') as outputfile:
# Enlaces
    print("{0} - Enlaces".format(isp_name), file=outputfile)
    print("Faixa de IP:, {0}".format(network_radio), file=outputfile)
    print(file=outputfile)
    print("IP,nome,login,senha," * 4, file=outputfile)
    for (ip1, ip2, ip3, ip4) in zip(subnet_enlace[0], subnet_enlace[1], subnet_enlace[2], subnet_enlace[3]):
        print("{0},,,, {1},,,, {2},,,, {3}".format(ip1, ip2, ip3, ip4), file=outputfile)

with open("ip-pppoe.csv", mode='w') as outputfile:
# PPPOEs
    print("{0} - PPPOEs".format(isp_name), file=outputfile)
    print("Faixa de IP:, {0}".format(network_pppoe), file=outputfile)
    print(file=outputfile)
    print("IP,nome,login,senha," * 2, file=outputfile)
    for (ip1, ip2) in zip(subnet_pppoe[0], subnet_pppoe[1]):
        print("{0},,,, {1},,,,".format(ip1, ip2), file=outputfile)

with open("ip-public-ip.csv", mode='w') as outputfile:
# Public IPs
    print("{0} - IPs Públicos".format(isp_name), file=outputfile)
    print("Faixa de IP:, {0}".format(network_public_ip), file=outputfile)
    print(file=outputfile)
    print("IP,Uso,Observações," * 4, file=outputfile)
    for (ip1, ip2, ip3, ip4) in zip(subnet_public_ip[0], subnet_public_ip[1], subnet_public_ip[2], subnet_public_ip[3]):
        print("{0},,, {1},,, {2},,, {3}".format(ip1, ip2, ip3, ip4), file=outputfile)