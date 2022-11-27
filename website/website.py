from enum import Enum, auto


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
