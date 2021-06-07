from ipaddress import *

my_pool = IPv4Network('100.64.0.0/24')

# loop through every ip in the network
for ip in my_pool:
    print(ip)

# Divide the network into a subnet (/24 -> /27 networks)
my_pool_subnet = [subnet for subnet in my_pool.subnets(prefixlen_diff=3)]
print(my_pool_subnet)
