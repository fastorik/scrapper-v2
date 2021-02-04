from concurrent.futures.thread import ThreadPoolExecutor
from scraper.mixins import SessionDriverMixin
from . import BaseScraper
from itemparser.sklep import SklepItemParser
# from driver.session import SessionDriver
# import requests


class SklepScraper(SessionDriverMixin, BaseScraper):
    start_url = 'https://sklepkoszykarza.pl/products/obuwie/category,2/item,72/page,1'
    url_pattern = 'https://sklepkoszykarza.pl/products/obuwie/category,2/item,72/page,{}'

    container_element_attrs = {'id': 'filter__products'}
    items_element_attrs = {'class': 'col-sm-6 col-md-4 col-xs-12 product'}
    pages_number_element_attrs = {'class': 'pagination__input'}

    item_parser = SklepItemParser

    # api_class = SessionDriver
    # api_kwargs = {
    #     'headers': {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    #     },
    #     'mount': requests.sessions.HTTPAdapter(max_retries=10)
    # }

    # def parse(self, executor=None):
    #     with ThreadPoolExecutor(max_workers=4) as executor:
    #         return super().parse(executor)

    def get_pages_container(self, container):
        container = super().get_pages_container(container)
        return container.find('span')
