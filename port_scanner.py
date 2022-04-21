import socket


def get_ip(target):
    ip = ''
    try:
        ip = socket.gethostbyname(target)
    except:
        ip = target

    return ip


def get_open_ports(target, port_range, verbose=False):

    open_ports = []
    ip = get_ip(target)
    ports = list(range(port_range[0], port_range[1]))
    v_str = '''Open ports for {target} ({ip})\nPORT     SERVICE\n'''.format(
        target=target, ip=ip)

    for p in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((ip, int(p)))

        if result == 0:
            open_ports.append(p)

        if verbose:
            v_str += str(p) + '       ' + 'service\n'

        s.close()

    if verbose:
        print(v_str)

    return(open_ports)
