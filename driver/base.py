class BaseDriver:
    driver_class = None

    def __init__(self, **kwargs):
        self.driver = self.driver_class(**kwargs)

    def get(self, url):
        pass

    def quit(self):
        pass

    @property
    def page_source(self):
        return self.get_page_source()

    def get_page_source(self):
        pass





