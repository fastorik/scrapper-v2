from .base import BaseItemParser
import re


class SklepItemParser(BaseItemParser):
    price_attrs = {'class': 'ps pricebox'}
    name_attrs = {'class': 'n'}
    url_attrs = None
    sizes_attrs = {'data-size': re.compile(r'\w+')}
    article_attrs = {'class': 's'}

    url_wrapping_tag = 'a'
    img_wrapping_tag = 'img'

    img_url_attr = 'data-echo'
