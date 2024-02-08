from ipaddress import ip_network


for i in range(256):
    for j in ip_network(f'127.254.{i}.10/255.255.224.0', False):
        f = format(j, 'b')
        if f[:16].count('1') < f[16:].count('1'):
            break
    else:
        print(i)

