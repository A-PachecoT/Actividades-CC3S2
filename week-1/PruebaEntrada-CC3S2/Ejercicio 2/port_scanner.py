# Credits: gogasca in https://stackoverflow.com/questions/2535055/check-if-remote-host-is-up-in-python
import socket
from functools import partial
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
from errno import ECONNREFUSED

NUM_CORES = 4


def portscan(target, port):
    try:
        # Create Socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketTimeout = 5
        s.settimeout(socketTimeout)
        s.connect((target, port))
        print('port_scanner.is_port_opened() ' + str(port) + " is opened")
        return port
    except socket.error as err:
        if err.errno == ECONNREFUSED:
            return False


# Wrapper function that calls portscanner
def scan_ports(server=None, port=None, portStart=None, portEnd=None, **kwargs):
    p = Pool(NUM_CORES)
    ping_host = partial(portscan, server)
    if portStart and portStart:
        return filter(bool, p.map(ping_host, range(portStart, portStart)))
    else:
        return filter(bool, p.map(ping_host, range(port, port + 1)))


# Check if port is opened
def is_port_opened(server=None, port=None, **kwargs):
    print('port_scanner.is_port_opened() Checking port...')
    try:
        # Add More proccesses in case we look in a range
        pool = ThreadPool(processes=1)
        try:
            ports = list(scan_ports(server=server, port=int(port)))
            print("port_scanner.is_port_opened() Port scanner done.")
            if len(ports) != 0:
                print('port_scanner.is_port_opened() ' + str(len(ports)) + " port(s) available.")
                return True
            else:
                print('port_scanner.is_port_opened() port not opened: (' + port + ')')
                return False
        except Exception as e:
            raise

    except Exception as e:
        print(e)
        raise