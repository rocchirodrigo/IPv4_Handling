from ipaddress import *

my_pool1 = IPv4Network('100.64.0.0/22')
my_pool2 = IPv4Network('45.11.11.0/28')

# loop through every ip in the network
for ip in my_pool1:
    print(ip)

# Divide the network into a subnet (/24 -> /27 networks)
my_pool_subnet = [subnet for subnet in my_pool1.subnets(prefixlen_diff=4)]
print(my_pool_subnet)

# Loop through 2 subnets  of different sizes
for (ip1, ip2) in zip(my_pool_subnet, my_pool2):
    print("{0} is routed globally as {1}".format(ip1, ip2))
