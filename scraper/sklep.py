from . import BaseScraper
from itemparser.base import SklepItemParser


class SklepScraper(BaseScraper):
    start_url = 'https://sklepkoszykarza.pl/products/obuwie/category,2/item,72/page,1'
    url_pattern = 'https://sklepkoszykarza.pl/products/obuwie/category,2/item,72/page,{}'

    container_element_attrs = {'id': 'filter__products'}
    items_element_attrs = {'class': 'col-sm-6 col-md-4 col-xs-12 product'}
    pages_number_element_attrs = {'class': 'pagination__input'}

    item_parser = SklepItemParser

    def get_pages_container(self, container):
        container = super().get_pages_container(container)
        return container.find('span')
