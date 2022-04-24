import socket
from common_ports import ports_and_services


def get_ip(target):
    ip = ''
    try:
        ip = socket.gethostbyname(target)
    except:
        ip = target
    return ip


def get_hostname(target):
    host = ''
    try:
        host = socket.gethostbyaddr(target)[0]
    except:
        host = target
    return host


def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    ip = get_ip(target)
    host = get_hostname(target)
    ports = list(range(port_range[0], port_range[1]))
    v_str = '''Open ports for {host} ({ip})\nPORT     SERVICE\n'''.format(
        host=host, ip=ip)

    try:
        for p in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((ip, int(p)))

            if result == 0:
                open_ports.append(p)

            if verbose:
                v_str += str(p)
                if p in ports_and_services:
                    v_str += '      '
                    v_str += ports_and_services[p]
                v_str += '\n'

            s.close()
    except:
        if 'www.' in target:
            return 'Error: Invalid hostname'
        else:
            return 'Error: Invalid IP address'

    if verbose:
        return v_str

    return(open_ports)
