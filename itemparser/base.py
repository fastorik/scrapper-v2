from model.clothes import Sneaker
from .decorators import attr_error_catcher
from itertools import starmap, repeat


class BaseItemParser:
    price_attrs = None
    name_attrs = None
    url_attrs = None
    sizes_attrs = None
    article_attrs = None

    url_wrapping_tag = None
    img_wrapping_tag = None

    img_url_attr = None

    item_model = Sneaker

    def __init__(self, items, scraper):
        self.items = items
        self.scraper = scraper
        self.setup()

    def setup(self):
        for key in filter(lambda x: 'attrs' in x, self.__class__.__dict__):  # TODO: names to variables
            setattr(self, key, {'attrs': self.__class__.__dict__[key]})

        for attr in self._main_attrs():
            setattr(self, attr.__name__, attr_error_catcher(attr))

    def parse_name(self, container):
        return container.find(**self.name_attrs).get_text()

    def parse_price(self, container):
        return container.find(**self.price_attrs).get_text()

    def parse_url(self, container):
        return container.find(self.url_wrapping_tag)['href']

    def parse_sizes(self, container):
        return [item.get_text() for item in container.find_all(**self.sizes_attrs)]
        # return list(map(lambda x: x.get_text(), container.find_all(**self.sizes_attrs)))

    def parse_image_url(self, container):
        return container.find(self.img_wrapping_tag)[self.img_url_attr]

    def parse_article(self, container):
        return container.find(**self.article_attrs)

    def get_item_attrs(self, container, exclude=None):
        attrs = {
            attr.__name__[len('parse_'):]: attr(container)
            for attr in self._main_attrs()
            if not exclude or attr.__name__[len('parse_'):] not in exclude
        }

        return attrs

    def get_parsed_item(self, container):
        item_attrs = self.get_item_attrs(container)

        return self.item_model(**item_attrs)

    def get_parsed_items(self):
        containers = self.get_containers()
        items = [self.get_parsed_item(container) for container in containers]

        return items

    def get_containers(self):
        return self.items

    def _main_attrs(self):
        attrs = list(starmap(getattr, list(zip(repeat(self), filter(lambda x: 'parse_' in x, dir(self))))))
        return attrs
