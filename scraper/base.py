from selenium.webdriver import Firefox
from bs4 import BeautifulSoup
import re
from itertools import chain


class BaseScraper:
    container_element_attrs = None
    items_element_attrs = None
    pages_number_element_attrs = None
    start_url = None
    url_pattern = None

    def __init__(self):
        self.api = Firefox()  # TODO: user defined
        self.selector = BeautifulSoup
        self.setup()

    def setup(self):
        for key in filter(lambda x: 'element_attrs' in x, self.__class__.__dict__):  # TODO: names to variables
            setattr(self, key, {'attrs': self.__class__.__dict__[key]})

    def get_items_container(self, container):
        return container.find(**self.container_element_attrs)

    def get_items(self, container):
        return container.find_all(**self.items_element_attrs)

    def get_pages_container(self, container):
        return container.find(**self.pages_number_element_attrs)

    def clean_pages_number(self, container):
        return int(re.search(r'\d+', container.get_text()).group(0))

    def get_pages_number(self, container):
        pages_container = self.get_pages_container(container)
        pages_number = self.clean_pages_number(pages_container)

        return pages_number

    def parse(self):
        items = map(self.parse_page_items, self.pages)
        items = list(chain.from_iterable(items))

        self.api.quit()

        return items

    def parse_page_items(self, page_url):
        self.api.get(url=page_url)
        soup = self.selector(self.api.page_source, 'html.parser')  # TODO: user defined behaviour

        container = self.get_items_container(soup)

        return self.get_items(container)

    @property
    def pages(self):
        self.api.get(self.start_url)

        pages_number = self.get_pages_number(self.selector(self.api.page_source, 'html.parser'))

        print(pages_number)
        return map(lambda x: self.url_pattern.format(x), range(1, pages_number+1))
