# Simple src-nat implementation
from math import log2
from ipaddress import IPv4Network, ip_network


def welcome_text():
    print("*" * 21)
    print("**src-nat generator**")
    print("*" * 21)
    print()


def input_addresses():
    """
    Get a valid public and private pool
    :return: both pools unpacked
    """
    while True:
        pool_public = input("Type a valid public network pool with prefix: ")
        if IPv4Network(pool_public).is_global:
            break
        else:
            print("This is a private network!")

    while True:
        pool_private = input("Type a valid private network pool with prefix: ")
        if not IPv4Network(pool_private).is_global:
            break
        else:
            print("This is a public ip!")
    return pool_public, pool_private


welcome_text()
public_ip, private_ip = input_addresses()

public_pool = IPv4Network(public_ip)
private_pool = IPv4Network(private_ip)

# New subnet mask calculation
prefix_div = public_pool.prefixlen - private_pool.prefixlen
divisor = private_pool.num_addresses / public_pool.num_addresses
expo = log2(divisor)
new_mask = int(32 - expo)

private_subnet = list(ip_network(str(private_pool.with_prefixlen)).subnets(new_prefix=new_mask))
index = 0  # needed to loop through the private subnets

# Writing code on the file
with open(file="nat-simples.rsc", mode='w') as output_file:
    # loopback
    print("/interface bridge", file=output_file)
    print("add name=loopback_cgnat", file=output_file)
    print(file=output_file)

    # ip address declaration
    print("/ip address", file=output_file)
    print("add address={0} interface=loopback_cgnat".format(public_pool.with_prefixlen), file=output_file)

    # blackhole routes for protection
    print(file=output_file)
    print("/ip route", file=output_file)
    for ip in public_pool:
        print("add dst-address={0}/32 type=blackhole".format(ip), file=output_file)

    # src-nat rules
    print(file=output_file)
    print("/ip firewall nat", file=output_file)
    for (ip1, ip2) in zip(private_subnet, public_pool):
        print("add action=src-nat chain=srcnat src-address={0} to-addresses={1}".format(ip1, ip2),
              file=output_file)

print("src-nat stored in the file: {}".format(output_file.name))
