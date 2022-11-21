#!python3

import argparse
import cmd

from termcolor import colored

from website.utils import load_sites


class PyMonitorShell(cmd.Cmd):
    intro = 'Welcome to the PyMonitor shell.   Type help or ? to list commands.\n'
    prompt = '(PyMonitor) '
    __color = False
    __sites = []

    def __init__(self, filename, color=False):
        super().__init__()
        self.__sites = load_sites(filename)
        self.__color = color

    def do_display_all(self, arg):
        """Display sites status"""
        for site in self.__sites:
            if self.__color:
                result = colored("Accessible", "green") if site.status == "OK" else colored("Inaccessible", "red")
            else:
                result = "Accessible" if site.status == "OK" else "Inaccessible"
            print(f"{site.name} \t\t: \t\t {result}")

    def do_test_all(self, arg):
        """Test all sites then display their status"""
        for site in self.__sites:
            site.test()
        self.do_display_all(None)

    def do_bye(self, arg):
        'Exit program'
        print('Thank you for using PyMonitor')
        return True


if __name__ == '__main__':
    # Use parseargs to get params and options
    parser = argparse.ArgumentParser(description='Easy Websites Monitoring.')
    # File argument
    parser.add_argument('file', metavar='FILE', help="file containing the list of websites to monitor, one per line.", )
    # Activate text coloring
    parser.add_argument("-c", "--color", help="display colored test result", action="store_true")
    args = parser.parse_args()

    # Run cmdloop to get user commands
    PyMonitorShell(args.file, args.color).cmdloop()
