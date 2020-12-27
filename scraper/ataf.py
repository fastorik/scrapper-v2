from . import BaseScraper
from itemparser.base import AtafItemParser


class AtafScraper(BaseScraper):
    start_url = 'https://www.ataf.pl/pl/854-buty-do-koszykowki?&page=1'
    url_pattern = 'https://www.ataf.pl/pl/854-buty-do-koszykowki?&page={}'

    container_element_attrs = {'class': 'pcajax row'}
    items_element_attrs = {'class': 'col-md-6 col-lg-4 no-pad'}

    item_parser = AtafItemParser

    def get_pages_number(self, container):
        return 7
