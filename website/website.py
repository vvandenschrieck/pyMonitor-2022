from enum import Enum, auto

from probes import state_probes


class Status(Enum):
    UNKNOWN = auto()
    OK = auto()
    SLOW = auto()
    KO = auto()


class Website:
    def __init__(self, name, url):
        self.__name = name
        self.__url = url
        self.__probes = []
        self.__test_history = []
        self.__status = Status.UNKNOWN


    def test(self):
        test_result = [probe(self.__url) for probe in self.__probes]
        self.__test_history.append(test_result)
        self.__status = Status.OK if all(test_result) else Status.KO

    def add_probe(self, probe_fct):
        """Add a probe to this website.
        A probe is a function that returns True or False (TO BE UPDATED)
        """
        self.__probes.append(probe_fct)

    @property
    def status(self):
        return self.__status.name

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"Site {self.__name} : {self.__url} - Tests appliqués : {self.__probes}"


class WebsitesList():
    def __init__(self, filename):
        """Creates a list of Website objects based on the content of a file
            This file must contain one website per line, one line having 3 parameters separeted by ; :
                - The name of the site
                - The DNS name of the site
                - The list of test to apply, comma-separated.
            followed by ; then the DNS name of the site (no http/https), then
        """
        self._observers = []
        self.__sites = []
        probe_dict = {"ping": state_probes.test_status_with_ping,
                      "nmap": state_probes.test_port_443_with_nmap}

        with open(filename) as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                name, url, probes = line.split(";")
                site = Website(name, url)
                for probe in probes.split(","):
                    site.add_probe(probe_dict[probe])
                self.__sites.append(site)

    def __iter__(self):
        return iter(self.__sites)

    def test_all(self):
        for site in self.__sites :
            self.notify("Testing "+site.name+" ...")
            site.test()
            self.notify() # Update display after each test

    # Implementation of Observer pattern - Observable side - Not thread-safe!

    def notify(self, msg=""):
        """Alert the observers"""

        for observer in self._observers:
            observer.update(msg)

    def attach(self, observer):
        """If the observer is not in the list,
        append it into the list"""

        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """Remove the observer from the observer list"""

        try:
            self._observers.remove(observer)
        except ValueError:
            pass
