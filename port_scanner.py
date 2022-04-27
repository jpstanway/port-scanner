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


def get_verbose_output(host, ip):
    v_str = ''
    if host[0].isnumeric():
        v_str = '''Open ports for {host}\nPORT     SERVICE'''.format(host=host)
    else:
        v_str = '''Open ports for {host} ({ip})\nPORT     SERVICE'''.format(
            host=host, ip=ip)
    return v_str


def get_verbose_spacing(port):
    total = 9
    space = ' '
    return (total - len(str(port))) * space


def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    ip = get_ip(target)
    host = get_hostname(target)
    ports = list(range(port_range[0], port_range[1] + 1))
    v_str = get_verbose_output(host, ip)

    try:
        for p in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((ip, int(p)))

            if result == 0:
                open_ports.append(p)

                if verbose and p in ports_and_services:
                    v_str += '\n'
                    v_str += str(p)
                    v_str += get_verbose_spacing(p)
                    v_str += ports_and_services[p]

            s.close()
    except socket.gaierror:
        if target[0].isnumeric():
            return 'Error: Invalid IP address'
        else:
            return 'Error: Invalid hostname'

    if verbose:
        return v_str

    return(open_ports)
