from .base import BaseItemParser
import re


class AtafItemParser(BaseItemParser):
    price_attrs = {'class': 'slider-price'}
    name_attrs = {'class': 'slider-product'}
    url_attrs = None
    sizes_attrs = {'data-size': re.compile(r'\w+')}

    url_wrapping_tag = 'a'
