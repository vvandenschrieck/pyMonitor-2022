import os
import threading

from Presenter import Presenter

from shell.ShellView import PyMonitorShell
from gui.GUIView import GUIView
from website import website


if __name__ == '__main__':
    # # Use parseargs to get params and options
    # parser = argparse.ArgumentParser(description='Easy Websites Monitoring.')
    # # File argument
    # parser.add_argument('file', metavar='FILE',
    #                     help="file containing the list of websites to monitor, one per line.", )
    # # Activate text coloring
    # parser.add_argument("-c", "--color", help="display colored test result",
    #                     action="store_true")
    # args = parser.parse_args()

    # Load model
    sites = website.WebsitesList("data/sites.txt")

    # Launch view and presenter for ConsoleUI
    shell_pres = Presenter(sites)
    shell_view = PyMonitorShell(shell_pres, True)
    shell_pres.set_view(shell_view)
    x = threading.Thread(target=shell_view.cmdloop, args=(1,))
    x.start()
    #shell_view.cmdloop()
    # Lauch view and presenter for GUI
    gui_pres = Presenter(sites)
    gui_view = GUIView(gui_pres)
    gui_pres.set_view(gui_view)
    gui_view.run()
