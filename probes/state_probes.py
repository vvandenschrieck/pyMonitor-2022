import platform
import subprocess


def test_status_with_ping(host):
    """
        Returns True if host (str) responds to a ping request.
        Implemented based on subprocess library
        """
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


if __name__ == "__main__":
    print(test_status_with_ping("www.google.com"))
