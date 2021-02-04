from .base import BaseDriver
from requests_html import HTMLSession


class SessionDriver(BaseDriver):
    driver_class = HTMLSession

    def __init__(self, headers, mount=None, **kwargs):
        super().__init__(**kwargs)
        self.driver.headers = headers
        self.driver.mount = mount
        self.response = None

    def get(self, url):
        self.response = self.driver.get(url)

    def get_page_source(self):
        text = self.response.text if self.response else ''
        return text

    def quit(self):
        self.driver.close()
