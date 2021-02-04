from concurrent.futures.thread import ThreadPoolExecutor
from itemparser.base import BaseItemParser
from bs4 import BeautifulSoup
# from functools import lru_cache


class InnerItemParser(BaseItemParser):
    inner_fields = ('article', )

    def __init__(self, items, scraper):
        super().__init__(items, scraper)
        self.inner_containers = self.get_inner_containers()

    def get_item_attrs(self, container, exclude=None):
        item_attrs = super().get_item_attrs(container, self.inner_fields)
        inner_attrs = self.get_inner_attrs(item_attrs['url'])

        return {**item_attrs, **inner_attrs}

    def get_inner_attrs(self, url):
        container = self.inner_containers[url]

        return {
            field: getattr(self, 'parse_' + field)(container)
            for field in self.inner_fields
        }

    def get_inner_containers(self):
        urls = self.get_inner_urls()

        with ThreadPoolExecutor(max_workers=10) as executor:
            raw_containers = executor.map(lambda x: (x, self.scraper.api.get_page_with_source(x)), urls)
            return {k: BeautifulSoup(container, 'html.parser') for k, container in raw_containers}

    def get_inner_urls(self):
        return (self.parse_url(item) for item in self.items)

