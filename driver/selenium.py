from .base import BaseDriver
from selenium.webdriver import Firefox, Chrome


class SeleniumDriver(BaseDriver):
    def get(self, url):
        self.driver.get(url)

    def get_page_source(self):
        return self.driver.page_source

    def quit(self):
        self.driver.quit()


class FirefoxDriver(SeleniumDriver):
    driver_class = Firefox


class ChromeDriver(SeleniumDriver):
    driver_class = Chrome
