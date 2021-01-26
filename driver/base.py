from abc import ABC
from abc import abstractmethod


class BaseDriver(ABC):
    driver_class = None

    def __init__(self, **kwargs):
        self.driver = self.driver_class(**kwargs)

    @abstractmethod
    def get(self, url):
        pass

    @abstractmethod
    def quit(self):
        pass

    @property
    def page_source(self):
        return self.get_page_source()

    @abstractmethod
    def get_page_source(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()





