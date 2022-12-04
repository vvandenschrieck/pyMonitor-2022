#!python3

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cmd
from termcolor import colored


class PyMonitorShell(cmd.Cmd):
    intro = 'Welcome to the PyMonitor shell.   Type help or ? to list commands.\n'
    prompt = '(PyMonitor) '
    __color = False
    __sites = []

    def __init__(self, pres, color=False):
        super().__init__()
        self.presenter = pres
        self.__color = color

    def do_display_all(self, arg):
        """Display sites status"""
        color = True
        for site, status in self.presenter.sites().items():
            if color:
                result = colored("Accessible", "green") \
                    if status == "OK" else colored("Inaccessible", "red")
            else:
                result = "Accessible" if status == "OK" else "Inaccessible"
            print(f"{site} \t\t: \t\t {result}")

    def do_test_all(self, arg):
        """Test all sites then display their status"""
        self.presenter.test_all()

    def do_bye(self, arg):
        'Exit program'
        print('Thank you for using PyMonitor')
        return True

    def refresh(self):
        """This method is used to present a coherent interface with other views.
        It is only a "proxy" for the do_test_all of this view, which can be renamed due to
        Cmd library conventions.
        """
        self.do_display_all(None)

    def msg(self,msg):
        print(msg)