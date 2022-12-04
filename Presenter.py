class Presenter:
    """This class controls the console view
    author: V. Van den Schrieck
    date: November 2020
    """
    def __init__(self, sites):
        self.__sites = sites
        self.__sites.attach(self)
        self.__view = None

    def set_view(self, view_instance):
        self.__view = view_instance

    def test_all(self):
        """Called by the view, to be applied to the model"""
        self.__sites.test_all()

    def sites(self):
        """Returns a representation of the sites for the view"""
        view_sites = {}
        for site in self.__sites :
            view_sites[site.name] = site.status
        return view_sites

    def update(self, msg=""):
        """Implementation of Observer pattern - Observer side
        This method is called whenever the model is modified.
        """
        if msg:
            self.__view.msg(msg)
        else:
            self.__view.refresh()
