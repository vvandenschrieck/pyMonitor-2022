import platform
import subprocess
import nmap
import socket
import logging

logger = logging.getLogger("pymonitor")


def test_status_with_ping(host):
    """
        Returns True if host (str) responds to a ping request.
        Implemented based on subprocess library
        """
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
    logger.info("Un test a été effectué avec ping sur le site " + host)
    return subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


def test_port_443_with_nmap(host):
    # Get IP from hostname
    ip = socket.gethostbyname(host)
    nm = nmap.PortScanner()
    nm.scan(ip, '443')
    return nm[ip].tcp(443)['state'] == "open"


if __name__ == "__main__":
    # print(test_status_with_ping("www.google.com"))
    print(test_port_443_with_nmap("localhost"))
