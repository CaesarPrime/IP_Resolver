#!/usr/bin/python

""" This is the resolver of the IP Resolver software , which resolves the ip addresses to their respective ISP's based on the
 network ips allocated for each of the ip addresses.
"""


def main():
    resolve_values('203.143.3.0', '203.143.0.0', 22)
    convert_to_binary(10)


def resolve_subnet(subnet_bits):
    ones = subnet_bits
    zeros = 32 - subnet_bits

    subnet = ""
    i = 0
    while i < ones:
        subnet += '1'
        i += 1

    j = 0
    while j < zeros:
        subnet += '0'
        j += 1

    return subnet


# match ips with network ips
def resolve_values(ip, net_ip, subnet):

    ip_numbers = ip.split('.')
    net_numbers = net_ip.split('.')

    ipv4_subnet = resolve_subnet(subnet)

    ip_binary = ""
    for i in ip_numbers:
        b = int(i)
        ip_binary += convert_to_binary(b)

    net_binary = ""
    for i in net_numbers:
        b = int(i)
        net_binary += convert_to_binary(b)

    print(ipv4_subnet)
    print(ip_numbers)
    print(ip_binary)
    print(net_binary)

    test_string = ""
    a = ip_binary
    b = ipv4_subnet
    for i in range(0, 32):

        test_string += str((int(a[i]) & int(b[i])))
        #print (a and b)

    print(test_string)

    if net_binary == test_string:
        return True
    else:
        return False


# to convert each ip address section to binary
def convert_to_binary(decimal):
    return (format(decimal, '#010b'))[2:]


# running the main script
if __name__ == '__main__':
    main()

# end of thr script
__author__ = "GWP Chamiekara"
__copyright__ = "Copyright 2017 , Sri Lanka CERT | CC Project"
__credits__ = ["Sri Lanka CERT | CC"]

__version__ = "1.0.1"
__maintainer__ = "Sri Lanka CERT | CC"
__email__ = "pasan@cert.gov.lk  "
__status__ = "Production"

