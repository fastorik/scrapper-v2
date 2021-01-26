from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

from bs4 import BeautifulSoup
import re
from itertools import chain


class BaseScraper:
    container_element_attrs = None
    items_element_attrs = None
    pages_number_element_attrs = None
    start_url = None
    url_pattern = None
    item_parser = None
    api_class = None
    api_kwargs = {}

    def __init__(self):
        self.api = None  # TODO: user defined
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

    def parse(self, executor=None):
        map_ = executor.map if executor else map

        # with ThreadPoolExecutor(max_workers=4) as executor:
        with self.api_class(**self.api_kwargs) as self.api:
            items = map_(self.parse_page_items, self.pages)
            items = list(map(self.to_item_model, chain.from_iterable(items)))

        return items

    def to_item_model(self, container):
        # print(container)
        return self.item_parser(container).build_parsed_item()

    def parse_page_items(self, page_url):
        self.api.get(url=page_url)
        soup = self.selector(self.api.page_source, 'html.parser')  # TODO: user defined behaviour
        print(f'Parser name: {self.__class__.__name__}')
        print(soup)

        container = self.get_items_container(soup)

        return self.get_items(container)

    @property
    def pages(self):
        self.api.get(self.start_url)

        pages_number = self.get_pages_number(self.selector(self.api.page_source, 'html.parser'))

        print(f'Pages number: {pages_number}')
        return map(lambda x: self.url_pattern.format(x), range(1, pages_number+1))
