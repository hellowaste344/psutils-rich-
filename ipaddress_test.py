import ipaddress
ip = ipaddress.IPv4Address('192.168.1.172')
ip1 = ipaddress.IPV6LENGTH
print("total number of bits in the IPv4:", ip.max_prefixlen)
print("total number of bits in the IPv6:", ip1)

print("is multicast?", ip.is_multicast)
print("is private?", ip.is_private)
print("is global?", ip.is_global)
print("is loopback?", ip.is_loopback)
print("is reserved?", ip.is_reserved)

network = ipaddress.IPv4Network("192.168.0.0/16")
print("Network address of the network:", network.network_address)
print("Broadcast address:", network.broadcast_address)
print("Network mask:", network.netmask)
print("with netmask:", network.with_netmask)
print("with hostmask:", network.with_hostmask)
print("number of hosts:", network.num_addresses)
# print if the network is under (or overlaps) 
print(f"{network} overlaps 192.168.0.0/16:", network.overlaps(network))
print(f"{network} is subnet of 192.168.0.0/16:", network.subnet_of(network))
print(f"{network} is supernet of 192.168.0.0/16:", network.supernet_of(ipaddress.IPv4Network("192.168.0.0/16")))
print("compare the network with 192.168.0.0/16:", network.compare_networks(ipaddress.IPv4Network("192.168.0.0/16")))
