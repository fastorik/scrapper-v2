from itemparser.inner import InnerItemParser
# from .base import BaseItemParser
import re


class AtafItemParser(InnerItemParser):
    price_attrs = {'class': 'slider-price'}
    name_attrs = {'class': 'slider-product'}
    url_attrs = None
    sizes_attrs = {'data-size': re.compile(r'\w+')}

    url_wrapping_tag = 'a'

    article_attrs = {'itemprop': 'sku'}

    img_wrapping_tag = 'img'
    img_url_attr = 'src'

    def parse_article(self, container):
        main_container = super().parse_article(container)
        return main_container['content']

